import os
import pathlib
import argparse
import pandas as pd
import numpy as np

from jinja2 import Environment, select_autoescape, FileSystemLoader
from langcodes import Language
from typing import Dict, Any

import datasets
import analyze_dataset
from benchmarks import BENCHMARKS, INTERESTED_LANGUAGES


jinja_env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape())


def get_alpha3(l, remove_latn_lang_ext):
  try:
    lang = Language.get(l)
    if not remove_latn_lang_ext and lang.script:
      return lang.to_alpha3() + "_" + lang.script
    else:
      return lang.to_alpha3()
  except:
    return 'unk'

def read_results(dataset_name, benchmark_name='fasttext', lang_dtype='str', remove_latn_lang_ext=True):
  if remove_latn_lang_ext:
    results_path = os.path.join('results', dataset_name, benchmark_name, 'results.csv')
  else:
    results_path = os.path.join('results', dataset_name, benchmark_name, 'results_latn.csv')
  results = pd.read_csv(results_path, sep=',', index_col=0, names=['detected_lang', 'detected_prob'])
  # langdetect/pycld2 returns nan for small number of rows. We'll just convert them to strings
  results['detected_lang'] = results['detected_lang'].astype(str).astype("category")
  results['detected_lang_alpha3'] = results['detected_lang'].apply(lambda x: get_alpha3(l=x.replace('__label__', ''), remove_latn_lang_ext=remove_latn_lang_ext)).astype(lang_dtype)
  return results

def accuracy(results_df):
  correct = (results_df['alpha3'] == results_df['detected_lang_alpha3']).astype(int)
  return correct.mean()

def get_stats_per_language(results):
  langs = results['alpha3'].unique().tolist()
  class_metrics = {}
  for lang in langs:
    tp = (results['alpha3'] == lang) & (results['detected_lang_alpha3'] == lang)
    fp = (results['alpha3'] != lang) & (results['detected_lang_alpha3'] == lang)
    tn = (results['alpha3'] != lang) & (results['detected_lang_alpha3'] != lang)
    fn = (results['alpha3'] == lang) & (results['detected_lang_alpha3'] != lang)
    precision = tp.sum() / (tp.sum() + fp.sum())
    recall = tp.sum() / (tp.sum() + fn.sum())
    f1 = tp.sum() / (tp.sum() + (fp.sum() + fn.sum()/2))
    class_metrics[lang] = dict(
      sentences_count=tp.sum()+fn.sum(),
      precision=precision,
      recall=recall,
      tp=tp.sum(),
      fp=fp.sum(),
      tn=tn.sum(),
      fn=fn.sum(),
      f1=f1,
    )

  stats_per_language = pd.DataFrame.from_records(data=list(class_metrics.values()), index=list(class_metrics.keys()))
  stats_per_language.index.name = 'language_alpha3'
  stats_per_language = stats_per_language.reset_index()

  # assign the language
  stats_per_language['language'] = stats_per_language['language_alpha3'].apply(analyze_dataset.get_language_name)

  # sort by sentences count and set the index to be row number
  stats_per_language.sort_values(['sentences_count'], ascending=False, inplace=True)
  stats_per_language = stats_per_language.reset_index()
  stats_per_language.index += 1

  return stats_per_language[['language_alpha3', 'language', 'sentences_count', 'precision', 'recall', 'f1', 'tp', 'fp', 'tn', 'fn']]

def md_link(text, url):
  return f"[{text}]({url})"

def create_dataset_results_table(dataset_name, metrics_per_benchmark):
  link_base = "https://github.com/Yubi2Community/YubiAI/blob/benchmark/benchmark/results/"

  for benchmark_name, row in metrics_per_benchmark.items():
    per_language_link = os.path.join(link_base, dataset_name, benchmark_name, f"classification_performance.md#metrics-per-language")
    acc_link = os.path.join(link_base, dataset_name, benchmark_name, f"classification_performance.md")
    supported_languages_link = os.path.join(link_base, dataset_name, benchmark_name, f"classification_performance.md#supported-languages")

    row['per_language_link'] = md_link("See metrics", per_language_link)
    row['agg_accuracy'] = md_link(row['agg_accuracy'], acc_link)
    row['supported_languages'] = md_link(row['supported_languages'], supported_languages_link)

  df = pd.DataFrame.from_records([{'name':k, **v} for k, v in metrics_per_benchmark.items()])
  df.columns=['Library', 'Supported languages', '# sentences supported', 'Aggregated accuracy', 'Per language metrics']
  return df

def write_md(template_name: str, template_ctx: Dict[str, Any], path: str):
    tmpl = jinja_env.get_template(f'{template_name}.md')
    rendered = tmpl.render(template_ctx)
    with open(path, 'w') as fd:
      fd.write(rendered)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Write aggregated results files.')
  parser.add_argument('--dataset', '-d', type=str, choices=datasets.names(), required=True)
  parser.add_argument('--timings_prefix', '-t', type=str, default='', help='Prefix of the times.npy file')
  parser.add_argument("--timings", type=bool, nargs='?', const=True, default=False, help='Analyze timings')
  parser.add_argument("--correctness", type=bool, nargs='?', const=True, default=False, help='Analyze correctness')
  #parser.add_argument("-r", type=bool, nargs='?', const=True, default=False, help='Analyze correctness')
  parser.add_argument("--remove_latn_lang_ext", '-r', action='store_true', help="Combining Latn Sentences with Normal Languages.")
  args = parser.parse_args()

  dataset_name = args.dataset
  timings_prefix = args.timings_prefix
  dataset = datasets.get(dataset_name)

  metrics_per_benchmark = {}

  for benchmark_name in BENCHMARKS.keys():
    benchmark_results_path = pathlib.Path('results') / dataset_name / benchmark_name
    print()
    if not benchmark_results_path.exists():
      print(f"Skipping {benchmark_name}. Results files not found on {benchmark_results_path}")
      continue

    if args.correctness:
      print(f"Analyzing {benchmark_name} results on {dataset_name}...")

      supported_languages = [Language.get(lang) for lang in BENCHMARKS["yubilangdetect-v1"]['supported_languages_alpha3']]
      if args.remove_latn_lang_ext:
        supported_languages_list_str = ", ".join(f"{lang.to_alpha3()} ({lang.display_name()})" for lang in supported_languages if not lang.script)
      else:
        supported_languages_list_str = ", ".join(f"{lang.to_alpha3()} ({lang.display_name()})" if not lang.script else f"{lang.to_alpha3()}_Latn ({lang.display_name()})" for lang in supported_languages)

      print(f"Reading results...")
      results = read_results(dataset_name, benchmark_name, lang_dtype=dataset.dtypes['alpha3'], remove_latn_lang_ext=args.remove_latn_lang_ext)
      supported_langs = BENCHMARKS[benchmark_name]['supported_languages_alpha3']
      interested_langs = BENCHMARKS["yubilangdetect-v1"]['supported_languages_alpha3']
      dataset_subset = datasets.get_supported_dataset_subset(dataset, supported_languages=interested_langs, remove_latn_lang_ext=args.remove_latn_lang_ext)
      print(f"Merging with dataset...")
      joined_results = pd.merge(dataset_subset, results, left_index=True, right_index=True, how="left", validate="one_to_one")

      print(f"Calculating accuracy...")
      aggregated_accuracy = accuracy(joined_results)
      print(f"Calculating metrics per language...")
      stats_per_language = get_stats_per_language(joined_results)
      dataset_supported_pct = "{:.2f}%".format(100. * len(dataset_subset) / len(dataset))

      metrics_per_benchmark[benchmark_name] = {
        'supported_languages': len(supported_langs),
        'supported_dataset': f"{len(dataset):,} ({dataset_supported_pct})",
        'agg_accuracy': "{:.2f}%".format(100. * aggregated_accuracy),
      }

      # assemble the md file and write it
      template_ctx = dict(
        benchmark_name=benchmark_name,
        dataset_name=dataset_name,
        dataset_len=len(dataset_subset),
        dataset_supported_pct=dataset_supported_pct,
        supported_languages_count=len(supported_languages),
        supported_languages_list_str=supported_languages_list_str,
        accuracy="{:.2f}%".format(100. * aggregated_accuracy),
        stats_per_language=stats_per_language.to_markdown(floatfmt=".3f"),
      )
      if args.remove_latn_lang_ext:
        results_path = os.path.join('results', dataset_name, benchmark_name, 'classification_performance.md')
      else:
        results_path = os.path.join('results', dataset_name, benchmark_name, 'classification_performance_latn.md')
      print(f"Dumping classification performance analysis to {results_path}")
      write_md('classification_performance', template_ctx=template_ctx, path=results_path)

    if args.timings:
      times = np.load(os.path.join('results', dataset_name, benchmark_name, f'{timings_prefix}times.npy'))
      template_ctx = dict(
        benchmark_name=benchmark_name,
        dataset_name=dataset_name,
        latency_avg=np.mean(times) / 10**6,
        latency_std=np.std(times) / 10**6,
        latency_p50=np.quantile(times, [0.5])[0] / 10**6,
        latency_p90=np.quantile(times, [0.9])[0] / 10**6,
        latency_p95=np.quantile(times, [0.95])[0] / 10**6,
        latency_p99=np.quantile(times, [0.99])[0] / 10**6,
        throughput=10**9/np.mean(times),
      )

      results_path = os.path.join('results', dataset_name, benchmark_name, f'{timings_prefix}speed_performance.md')
      print(f"Dumping latency/throughput analysis to {results_path}")
      write_md('speed_performance', template_ctx=template_ctx, path=results_path)

  print(f"Creating aggregated table for {dataset_name}")
  if args.remove_latn_lang_ext:
    agg_table_path = os.path.join('results', dataset_name, 'results.md')
  else:
    agg_table_path = os.path.join('results', dataset_name, 'results_latn.md')
  df = create_dataset_results_table(dataset_name, metrics_per_benchmark)
  template_ctx = dict(
    dataset_name=dataset_name,
    results_table=df.to_markdown(floatfmt=".3f", index=False)
  )
  write_md('dataset_results', template_ctx=template_ctx, path=agg_table_path)
  print(f"Written in {agg_table_path}")
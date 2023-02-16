import argparse
import os

import datasets
from langcodes import Language


def get_language_name(alpha3):
  try:
    return Language.get(alpha3).display_name()
  except:
    print(f"Failed to get name for language '{alpha3}'")
    return "--"


def get_stats_table(df):
  df = df.copy()
  df['text_len'] = df['text'].str.len()

  # calculate stats (count, pct, mean(text_len)) per language, sorted by count DESC
  counts = df.groupby('alpha3').agg({'text_len': ['count', 'mean']}).reset_index()
  counts.columns = ['alpha3', 'sentences', 'mean_len']
  counts['dataset_percentage'] = (counts['sentences'] / counts['sentences'].sum() * 100).apply(lambda x: "{:.2f}%".format(x))
  counts.sort_values(['sentences'], ascending=False, inplace=True)
  counts.reset_index(inplace=True)
  counts.index += 1

  # assign language name
  counts['language'] = counts['alpha3'].apply(get_language_name)
  return counts[['alpha3', 'language', 'sentences', 'dataset_percentage', 'mean_len']]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Write aggregated results files.')
  parser.add_argument('--dataset', '-d', type=str, choices=datasets.names(), required=True)
  args = parser.parse_args()

  print(f"Dumping stats for dataset {args.dataset}")

  ds = datasets.get(args.dataset)
  stats_df = get_stats_table(ds)

  with open(os.path.join('datasets', args.dataset, 'stats.md'), 'w') as fd:
    stats_df.to_markdown(fd, index=True)

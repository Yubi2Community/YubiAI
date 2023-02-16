import re, json
from argparse import ArgumentError
from glob import glob

import pandas as pd
from langcodes import Language
from pathlib import Path

PATTERN = r"[!\"#$%&\\'()*+,\-./:;<=>?@\[\]^_`{|}~a-zA-Z0-9 ]+"
RE_COMPILE = re.compile(PATTERN)
EN_PATTERN = r"[!\"#$%&\\'()*+,\-./:;<=>?@\[\]^_`{|}~0-9 ]+"
EN_RE_COMPILE = re.compile(EN_PATTERN)

def check_data(text, lang_code, allowed_ratio=0.75):
  try:
    if  lang_code != 'eng' and (not lang_code.endswith("Latn")):
        matched = RE_COMPILE.findall(str(text))
    else:
        matched = EN_RE_COMPILE.findall(text)
    matched_str = "".join(matched)
    len_ratio = len(matched_str)/len(text)
    return len_ratio <= allowed_ratio
  except Exception as e:
    return False

__DATASETS = {}

def normalize_lang(lang):
  if lang.startswith("tr_"):
    lang = f"{lang[-2:]}_Latn"
  return lang

def get_alpha3(lang):
  l = Language.get(normalize_lang(lang))
  try:
    if l.script:
      return l.to_alpha3() + "_" + l.script
    return l.to_alpha3()
  except:
    return None


def dataset(load_fn):
  __DATASETS[load_fn.__name__] = load_fn
  return load_fn


def get(name):
  name = name.replace('-', '_')
  if name in __DATASETS:
    return __DATASETS[name]()
  raise ArgumentError(f"Unkown dataset {name}")

def read_txt_data(fn):
    with open(fn, 'r') as txtf:
        data = txtf.read().strip("\n").split("\n")
    return data

def names():
  return [name.replace('_', '-') for name in __DATASETS.keys()]


@dataset
def tatoeba_sentences_2021_06_05():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05/sentences.csv'
  ds = pd.read_csv(dataset_path, sep='\t', index_col=0, names=['language', 'text'], dtype={'language': 'category'})
  ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
  ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
  return ds


@dataset
def tatoeba_sentences_2021_06_05_common_48():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05-common-48/sentences.csv'
  ds =  pd.read_csv(dataset_path, index_col=0, names=['language', 'text'], dtype={'language': 'category'})
  ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
  ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
  return ds


@dataset
def open_subtitles_v2018_100k_per_lang():
  dataset_files = 'datasets/open-subtitles-v2018-100k-per-lang/*.txt'
  dfs = []
  for f in glob(dataset_files):
    sentences = open(f, encoding='utf-8').readlines()
    language = re.split('[\./]', f)[-2]
    data = dict(
      text=sentences,
      language=language,
    )
    dfs.append(pd.DataFrame(data=data))

  big_df = pd.concat(dfs).reset_index().drop('index', axis=1)
  big_df['language'] = big_df['language'].astype("category")
  big_df['alpha3'] = big_df['language'].apply(get_alpha3).astype("category")
  big_df = big_df[big_df.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
  return big_df

@dataset
def yubi_benchmark_dataset_v1():
  dataset_path = 'datasets/yubi_benchmark_dataset/benchmark.csv'
  ds = pd.read_csv(dataset_path, dtype={'language': 'category'})
  ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
  ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
  return ds

@dataset
def yubi_benchmark_dataset_v2():
  dataset_path = 'datasets/yubi_benchmark_dataset_v2/benchmark_v2.csv'
  ds = pd.read_csv(dataset_path, dtype={'alpha3': 'category'})
  ds['alpha3'] = ds['alpha3'].apply(get_alpha3).astype("category")
  ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
  return ds

@dataset
def yubi_benchmark_dataset_v2_full():
    text_file = 'datasets/yubi_benchmark_dataset_v2_full/test.txt'
    label_file = 'datasets/yubi_benchmark_dataset_v2_full/test.label'
    
    test_data = read_txt_data(text_file)
    label_data = read_txt_data(label_file)
    
    ds = pd.DataFrame({"text":test_data, "language":label_data})
    ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
    ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    return ds

@dataset
def yubi_benchmark_dataset_v2_full_gt2():
    text_file = 'datasets/yubi_benchmark_dataset_v2_full/test.txt'
    label_file = 'datasets/yubi_benchmark_dataset_v2_full/test.label'
    
    test_data = read_txt_data(text_file)
    label_data = read_txt_data(label_file)
    
    ds = pd.DataFrame({"text":test_data, "language":label_data})
    ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
    ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    ds = ds[ds.text.str.split().apply(lambda row: len(row)) > 2]
    return ds

@dataset
def dakshina_dataset_v1():
    data_file_pattern = 'datasets/dakshina-dataset-v1/dakshina_dataset_v1.0/*/romanized/*.romanized.rejoined.tsv'
    dataset_files = glob(data_file_pattern)
    all_data = []
    for lang_file in dataset_files:
        lang_code = Path(lang_file).name.split(".")[0]
        lang_data = pd.read_csv(lang_file, delimiter="\t", error_bad_lines=False, header=None)
        
        org_data = lang_data[[0]]
        trans_data = lang_data[[1]]
        
        org_data['language'] = [lang_code]*len(org_data)
        org_data.columns = ['text', 'language']
        org_data['text'].astype(str)
        org_data['language'].astype("category")
        
        trans_data['language'] = [f"tr_{lang_code}"]*len(org_data)
        trans_data.columns = ['text', 'language']
        trans_data['text'].astype(str)
        trans_data['language'].astype("category")
        
        all_data.append(org_data)
        all_data.append(trans_data)

    ds = pd.concat(objs=all_data,ignore_index=True).dropna()
    ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
    ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    return ds

@dataset
def dakshina_dataset_v1_gt2():
    data_file_pattern = 'datasets/dakshina-dataset-v1/dakshina_dataset_v1.0/*/romanized/*.romanized.rejoined.tsv'
    dataset_files = glob(data_file_pattern)
    all_data = []
    for lang_file in dataset_files:
        lang_code = Path(lang_file).name.split(".")[0]
        lang_data = pd.read_csv(lang_file, delimiter="\t", error_bad_lines=False, header=None)
        
        org_data = lang_data[[0]]
        trans_data = lang_data[[1]]
        
        org_data['language'] = [lang_code]*len(org_data)
        org_data.columns = ['text', 'language']
        org_data['text'].astype(str)
        org_data['language'].astype("category")
        
        trans_data['language'] = [f"tr_{lang_code}"]*len(org_data)
        trans_data.columns = ['text', 'language']
        trans_data['text'].astype(str)
        trans_data['language'].astype("category")
        
        all_data.append(org_data)
        all_data.append(trans_data)

    ds = pd.concat(objs=all_data,ignore_index=True).dropna()
    ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
    ds = ds[ds.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    ds = ds[ds.text.str.split().apply(lambda row: len(row)) > 2]
    return ds

@dataset
def english_words_dataset():
    data_file_pattern = 'datasets/english-words-dataset/words_dictionary.json'
    with open(data_file_pattern, 'r') as jsf:
        eng_words_data = json.loads(jsf.read())
    eng_words_data_list = list(eng_words_data.keys())
    df = pd.DataFrame({"text": eng_words_data_list, "language": ['en']*len(eng_words_data_list)})
    df['text'].astype(str)
    df['language'].astype("category")
    df['alpha3'] = df['language'].apply(get_alpha3).astype("category")
    df = df[df.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    return df

@dataset
def norvig_freq_eng_words_dataset():
    data_file_pattern = 'datasets/norvig-most-frequent-eng-words-dataset/count_1w.txt'
    df = pd.read_csv(data_file_pattern, delimiter="\t", header=None)
    df.columns = ["text", 'freq']
    df['language'] = ['en']*len(df)
    df['text'].astype(str)
    df['language'].astype("category")
    df['alpha3'] = df['language'].apply(get_alpha3).astype("category")
    df = df[df.apply(lambda row:check_data(row.text, row.alpha3), axis=1)]
    return df

remov_latn_extns = lambda x: x.split("_")[0] if x.endswith("_Latn") else x

def get_supported_dataset_subset(dataset, supported_languages, remove_latn_lang_ext=False):
  if remove_latn_lang_ext:
    supported_languages = [lang_code for lang_code in  supported_languages if not lang_code.endswith("_Latn")]
    dataset["alpha3"] = dataset["alpha3"].apply(remov_latn_extns)
    return dataset[dataset['alpha3'].isin(supported_languages)]
  return dataset[dataset['alpha3'].isin(supported_languages)]

import os
import time
import numpy as np
import psutil
import sys
from langcodes import Language

sys.path.append("/home/ubuntu/yubi_ds_capability/")

def normalize_lang(lang):
  if lang.startswith("tr_"):
    lang = f"{lang[-2:]}_Latn"
  return lang

SUPPORTED_LANGUAGES_INTERNAL = 'hi bn gu pa ml kn ta te or mr as ne ur en tr_hi tr_bn tr_gu tr_pa tr_ml tr_kn tr_te tr_ta tr_mr tr_or tr_ne tr_ur tr_as'.split(" ")
SUPPORTED_LANGUAGES = [normalize_lang(lang) for lang in SUPPORTED_LANGUAGES_INTERNAL]

def measure_memory(model_path):
  p = psutil.Process(os.getpid())
  mem_before = p.memory_info().rss
  from cernunnos.nlp.language_detection.yubiLanguageDetection import LanguageDetection
  model = model = LanguageDetection()
  text = "CredAvenue is building India’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution."
  model.detect_language(input_text=text, top_k=5)
  return p.memory_info().rss - mem_before

def run(dataset, elapsed):
  from cernunnos.nlp.language_detection.yubiLanguageDetection import LanguageDetection

  lang = np.chararray(len(dataset), itemsize=15)
  prob = np.zeros((len(dataset),), dtype=np.float)
  model = LanguageDetection(task_name="e4_v1_language_detection", use_gpu=True)

  for i, text in enumerate(dataset):
    # For some reason fasttext likes one line at a time.
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = model.detect_language(input_text=text, top_k=2)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    assert len(result) == 5
    lang[i] = normalize_lang(result['lang_code'])
    prob[i] = result['confidence']

  return dict(lang=lang, prob=prob)
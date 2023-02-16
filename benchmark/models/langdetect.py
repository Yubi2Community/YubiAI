import time
import numpy as np
import psutil
import os


SUPPORTED_LANGUAGES = ("af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, " + \
  "hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, " + \
  "pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw").split(", ")


def measure_memory():
  p = psutil.Process(os.getpid())
  mem_before = p.memory_info().rss
  import langdetect
  langdetect.detect_langs("hello darkness my ol' fren")
  return p.memory_info().rss - mem_before


def run(dataset, elapsed):
  import langdetect
  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)

  for i, text in enumerate(dataset):
    try:
      iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
      result = langdetect.detect_langs(text)
      elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    except:
      result = None

    if result:
      lang[i] = result[0].lang
      prob[i] = result[0].prob
    else:
      lang[i] = 'n/a'
      prob[i] = float('nan')

  return dict(lang=lang, prob=prob)

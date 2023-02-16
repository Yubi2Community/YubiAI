import time
import numpy as np
import psutil
import os


SUPPORTED_LANGUAGES = "af, am, an, ar, as, az, be, bg, bn, br, bs, ca, cs, cy, da, de, dz, el, en, eo, es, et, eu, fa, fi, fo, fr, ga, gl, gu, he, hi, hr, ht, hu, hy, id, is, it, ja, jv, ka, kk, km, kn, ko, ku, ky, la, lb, lo, lt, lv, mg, mk, ml, mn, mr, ms, mt, nb, ne, nl, nn, no, oc, or, pa, pl, ps, pt, qu, ro, ru, rw, se, si, sk, sl, sq, sr, sv, sw, ta, te, th, tl, tr, ug, uk, ur, vi, vo, wa, xh, zh, zu".split(", ")


def measure_memory():
  p = psutil.Process(os.getpid())
  mem_before = p.memory_info().rss
  import langid
  langid.classify("hello darkness my ol' fren")
  return p.memory_info().rss - mem_before


def run(dataset, elapsed):
  import langid
  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = langid.classify(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    lang[i] = result[0]
    prob[i] = result[1]

  return dict(lang=lang, prob=prob)

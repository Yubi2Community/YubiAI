import numpy as np
import os
import psutil
import time

# https://github.com/google/cld3

SUPPORTED_LANGUAGES = "af am ar bg bg-Latn bn bs ca ceb co cs cy da de el el-Latn en eo es et eu fa fi fil fr fy ga gd gl gu ha haw hi hi-Latn hmn hr ht hu hy id ig is it iw ja ja-Latn jv ka kk km kn ko ku ky la lb lo lt lv mg mi mk ml mn mr ms mt my ne nl no ny pa pl ps pt ro ru ru-Latn sd si sk sl sm sn so sq sr st su sv sw ta te tg th tr uk ur uz vi xh yi yo zh zh-Latn zu".split(" ")


def measure_memory():
  p = psutil.Process(os.getpid())
  mem_before = p.memory_info().rss
  import gcld3
  model = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=3000)
  model.FindLanguage(text="hello darkness my ol' fren")
  return p.memory_info().rss - mem_before


def run(dataset, elapsed):
  import gcld3
  detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=3000)

  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)
  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = detector.FindLanguage(text=text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    lang[i] = result.language
    prob[i] = result.probability

  return dict(lang=lang, prob=prob)

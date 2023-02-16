import os
import time
import numpy as np
import psutil


MODEL_BIN = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
MODEL_COMPRESSED = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz'


SUPPORTED_LANGUAGES = "af als am an ar arz as ast av az azb ba bar bcl be bg bh bn bo bpy br bs bxr ca cbk ce ceb ckb co cs cv cy da de diq dsb dty dv el eml en eo es et eu fa fi fr frr fy ga gd gl gn gom gu gv he hi hif hr hsb ht hu hy ia id ie ilo io is it ja jbo jv ka kk km kn ko krc ku kv kw ky la lb lez li lmo lo lrc lt lv mai mg mhr min mk ml mn mr mrj ms mt mwl my myv mzn nah nap nds ne new nl nn no oc or os pa pam pfl pl pms pnb ps pt qu rm ro ru rue sa sah sc scn sco sd sh si sk sl so sq sr su sv sw ta te tg th tk tl tr tt tyv ug uk ur uz vec vep vi vls vo wa war wuu xal xmf yi yo yue zh".split(" ")


def measure_memory(model_path):
  p = psutil.Process(os.getpid())
  mem_before = p.memory_info().rss
  import fasttext
  download_model(model_path)
  model = fasttext.load_model('/tmp/fasttext.model')
  model.predict("hello darkness my ol' fren")
  return p.memory_info().rss - mem_before



def run(dataset, elapsed, model_path):
  import fasttext

  lang = np.chararray(len(dataset), itemsize=15)
  prob = np.zeros((len(dataset),), dtype=np.float)

  download_model(model_path)
  model = fasttext.load_model('/tmp/fasttext.model')

  for i, text in enumerate(dataset):
    # For some reason fasttext likes one line at a time.
    text = str(text).replace('\n', ' ')

    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = model.predict(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    assert len(result[0]) == 1
    lang[i] = result[0][0]
    prob[i] = result[1][0]

  return dict(lang=lang, prob=prob)


def download_model(path):
  os.system(f"wget -O /tmp/fasttext.model {path}")

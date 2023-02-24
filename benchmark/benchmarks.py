from functools import partial
from langcodes import Language

from langcodes import Language
from models import gcld3, langid, langdetect, pycld2, fasttext, yubidetect_v1, yubidetect_v2, yubidetect_e8_v1

def get_alpha3(lang):
  l = Language.get(lang)
  try:
    if l.script:
      return l.to_alpha3() + "_" + l.script
    return l.to_alpha3()
  except:
    return None

INTERESTED_LANGUAGES = yubidetect_v1.SUPPORTED_LANGUAGES


BENCHMARKS = {
  'fasttext': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_BIN),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_BIN),
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'fasttext-compressed': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_COMPRESSED),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_COMPRESSED),
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'gcld3': {
    'run': gcld3.run,
    'measure_memory': gcld3.measure_memory,
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in gcld3.SUPPORTED_LANGUAGES],
  },
  'langdetect': {
    'run': langdetect.run,
    'measure_memory': langdetect.measure_memory,
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in langdetect.SUPPORTED_LANGUAGES],
  },
  'langid': {
    'run': langid.run,
    'measure_memory': langid.measure_memory,
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in langid.SUPPORTED_LANGUAGES],
  },
  'pycld2': {
    'run': pycld2.run,
    'measure_memory': pycld2.measure_memory,
    'supported_languages_alpha3': [Language.get(lang).to_alpha3() for lang in pycld2.SUPPORTED_LANGUAGES],
  },
  'yulan-e4-v1': {
    'run': yubidetect_v1.run,
    'measure_memory': yubidetect_v1.measure_memory,
    'supported_languages_alpha3': [get_alpha3(lang) for lang in yubidetect_v1.SUPPORTED_LANGUAGES],
  },
  'yulan-e4-v2': {
    'run': yubidetect_v2.run,
    'measure_memory': yubidetect_v2.measure_memory,
    'supported_languages_alpha3': [get_alpha3(lang) for lang in yubidetect_v2.SUPPORTED_LANGUAGES],
  },
  'yulan-e8-v2': {
    'run': yubidetect_e8_v1.run,
    'measure_memory': yubidetect_e8_v1.measure_memory,
    'supported_languages_alpha3': [get_alpha3(lang) for lang in yubidetect_e8_v1.SUPPORTED_LANGUAGES],
  }
}


def common_languages():
  supported_languages = set(BENCHMARKS['fasttext']['supported_languages_alpha3'])
  for b in BENCHMARKS:
    supported_languages = supported_languages.intersection(BENCHMARKS[b]['supported_languages_alpha3'])
  return supported_languages

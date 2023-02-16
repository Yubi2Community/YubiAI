import argparse
from benchmarks import BENCHMARKS


MB = 1024*1024


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Calculates memory usage for loading the model and running one inference request.')
  parser.add_argument('benchmarks', nargs='+')

  args = parser.parse_args()

  mem_usage = {}
  for benchmark_name in args.benchmarks:
    mem_usage[benchmark_name] = BENCHMARKS[benchmark_name]['measure_memory']() / MB
  print(mem_usage)

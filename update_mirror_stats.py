#!/usr/bin/env python
import json
import os
import subprocess
import tempfile

try:
  with open("/home/mirror/web/stats.json") as fp:
    stats = json.load(fp)
except IOError:
  print("Couldn't open stats.json! Resetting database!")
  stats = {}

modules = []  # eh.
def explore(path_array):
  path = os.path.join('/pool/mirrors', *path_array)
  size_path = os.path.join(path, "mirror.umd.edu.size.txt")

  if path_array and os.path.exists(size_path):
    modules.append((path_array[-1], path))
  elif len(path_array) <= 2:
    for entry in os.listdir(path):
      if os.path.isdir(os.path.join(path, entry)):
        explore(path_array + [entry])

explore([])

for module_name, module_path in modules:
  if not module_name in stats:
    stats[module_name] = {}

  try:
    size_line = open(os.path.join(module_path, "mirror.umd.edu.size.txt"), "r").read().strip()
    size = int(size_line.split(' ')[0])
    stats[module_name]['size'] = size
  except IOError:
    pass

stats_file = open("/home/mirror/web/stats.json.tmp", "w")
json.dump(stats, stats_file)
stats_file.close()

os.rename("/home/mirror/web/stats.json.tmp", "/home/mirror/web/stats.json")


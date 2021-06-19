#!/usr/bin/env python3

import re, sys, operator

error_dict = {}
info_dict = {}
info_pattern = r"ticky: INFO: ([\w ]*) "
error_pattern = r"ticky: ERROR: ([\w' ]*) "

with open(sys.argv[1], 'r') as f:
  for line in f.readlines():
    line = line.strip()
    if re.search(error_pattern, line):
      result = re.search(error_pattern, line)
      error_dict[result[1]] = error_dict.get(result[1],0) + 1

print(sorted(error_dict.items(), key=operator.itemgetter(1),reverse=True))

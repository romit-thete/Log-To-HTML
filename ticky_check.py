#!/usr/bin/env python3

import re, sys, operator

per_error_dict = {}
error_dict = {}
info_dict = {}
per_user = {}
info_pattern = r"ticky: INFO: ([\w ]*) "
error_pattern = r"ticky: ERROR: ([\w' ]*) "
user_pattern = r"ticky: (INFO|ERROR):.*\(([\w]+)\)"

with open(sys.argv[1], 'r') as f:
  for line in f.readlines():
    line = line.strip()
    if re.search(error_pattern, line):
      result = re.search(error_pattern, line)
      per_error_dict[result[1]] = per_error_dict.get(result[1],0) + 1
#    if re.search(user_pattern, line):
#      result1 = re.search(user_pattern, line)
#      if result1[1].lower() == 'error':
#        error_dict[result1[2]] = error_dict.get(result1[2],0) + 1
#      elif result1[1].lower() == 'info':
#        info_dict[result1[2]] = info_dict.get(result1[2],0) +1
    if re.search(user_pattern,line):
      result = re.search(user_pattern,line)
      if result[1].lower() == 'info':
        per_user[result[2]] = per_user.get(result[2],0) + 1
#      elif result[1].lower() == 'info':
#        per_user[result[2]] = per_user.get(result[2],0) +1
print(per_user)
final_list = sorted(per_error_dict.items(), key=operator.itemgetter(1), reverse = True)
final_list.insert(0,("Error","Count"))
print(final_list)

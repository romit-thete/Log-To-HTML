"""
This program is one of the coolest examples of a day to day task.
It basically checks for logs within a file and creates two reports:
    1. Report of info, errors generated per user.
    2. Report of count of unique errors within the log.

Program Arguments:
    1. The log file.

Functions:
    1. error_count(line):
        This function expects a line from a particular log file as an argument.
        It then checks if the line corresponds to some error.
        If it does, it creates a list of (error,count) pairs.
    2. details_per_user(line):
        This function expects a line from a particular log file as an argument.
        It then checks if it corresponds to an info or an error.
        It further creates a list of (Username, info_count, error_count) triplets accordingly.
    3. write_to_csv():
        This function reads a log file and further creates 2 CSV files:
            a. error_message.csv        -->     Error to count representation
            b. user_statistics.csv      -->     User to info count and error count representation

Errors/Exceptions:
    1. FileNotFoundError: If a particular log file path given by the user is not found on the system.
    2. IndexError: If the user does not provide the log file path.

Usage:
    Windows:    python ticky.py <logfile_name>
    Unix:       ./ticky.py <log_file_path>
"""
#!/usr/bin/env python3

import re, sys, operator, csv

error_details_dict = {}
error_dict = {}
info_dict = {}
user_pattern = r"ticky: (INFO|ERROR): ([\w' ]*|[\w' ]*\[#\d+\].*).\(([\w]+)\)"
# result[0] --> The complete matched string
# result[1] --> INFO|ERROR
# result[2] --> Message (could be different for error and info)
# result[3] --> UserId

# Counts the number of errors and sort them in a descending order of count.
def error_count(line):
    result = re.search(user_pattern, line)
    if result[1].lower() == 'error':
        error_details_dict[result[2]] = error_details_dict.get(result[2],0) + 1
    error_count_list = sorted(error_details_dict.items(), key=operator.itemgetter(1), reverse = True)
    error_count_list.insert(0,("Error","Count"))
    return error_count_list

# Counts the number of info and error messages per user and sort by username.
def details_per_user(line):
    result = re.search(user_pattern,line)
    if result[1].lower() == 'info':
        info_dict[result[3]] = info_dict.get(result[3],0) + 1
    elif result[1].lower() == 'error':
        error_dict[result[3]] = error_dict.get(result[3],0) + 1
    new_list = sorted(info_dict.items(), key=operator.itemgetter(0))

    # The below code will add the error count per user in every tuple within the new_list.
    for tup in new_list:
        tup_list = list(tup)
        if tup[0] in error_dict.keys():
            # If we find the username in error_dict.keys(), add the value (error count) of the user in the tup_list.
            extension_value = error_dict[tup[0]]
            tup_list.append(extension_value)
        else:
            # If the username isn't found in error_dict.keys(), add error count as 0 in the tup_list for that user.
            extension_value = 0
            tup_list.append(extension_value)
        # Create tuple from tup_list and add it back to the same index.
        new_list[new_list.index(tup)] = tuple(tup_list)
    new_list.insert(0,("Username","INFO", "ERROR"))
    return new_list

# Adding a validation to check if the log file is provided or not.
try:
    fh = open(sys.argv[1])
    fh.close()
except IndexError:
    print("\n\nPlease enter a log file path as well!\n\n")
    sys.exit(1)
except FileNotFoundError:
    print("\n\nPlease enter the correct log file path!\n\n")
    sys.exit(1)

# Create a csv file based on the user_list and error_list.
def write_to_csv():
    # Open given log file for reading and create error count list and per user usage list.
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            line = line.strip()
            error_list = error_count(line)
            user_list = details_per_user(line)

    # Create a error_message.csv file
    with open('error_message.csv','w') as error_csv:
        writer = csv.writer(error_csv)
        writer.writerows(error_list)

    # Create a user_statistics.csv file
    with open('user_statistics.csv','w') as user_csv:
        writer = csv.writer(user_csv)
        writer.writerows(user_list)


if __name__ == '__main__':
    write_to_csv()

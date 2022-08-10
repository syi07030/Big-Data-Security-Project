#!/usr/bin/env python3
#python 8csv_reader_counts_for_multiple_files.py "C:＼Users＼kshje＼Desktop＼EWHA＼21-2＼빅데이터보안＼data-variable-length＼data"

import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
max_length = 0
max_row = 0
max_col = 0
name = "x"

for input_file in glob.glob(os.path.join(input_path,'*.csv')):
	row_counter = 1

	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)

		for row in filereader:
			row_counter += 1
		
		if row_counter*len(header) > max_length:
			max_length = row_counter*len(header)
			max_row = row_counter
			max_col = len(header)
			name = os.path.basename(input_file)

	print('{0!s}: \trow: {1:d} \tcol: {2:d}'.format(os.path.basename(input_file), row_counter, len(header)))
      
	file_counter += 1

print('Number of files: {0:d}'.format(file_counter))
print('Max: {0} \tlen: {1:d} \trow: {2:d} \tcol: {3:d}'.format(name, max_length, max_row, max_col))

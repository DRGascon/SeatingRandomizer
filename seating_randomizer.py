import csv
from random import shuffle

LIST_FILE = "list.csv"
PER_TABLE = 10

print("hello world!\n")

row_dict = { }
print("-------------- ORIGINAL ORDER -------------------")
with open(LIST_FILE) as reader:
	csv_reader = csv.reader(reader)
	row_num = 0
	for row in csv_reader:
		if row_num != 0:
			print(row[0])
			row_dict[row_num] = row
		row_num = row_num + 1
	# -1 for the header
	print("Number of students: " + str(row_num- 1))

keys = list(row_dict.keys())
shuffle(keys)

print("-------------- SHUFFLED ORDER -------------------")
row_num = 0
with open('shuffled_list.csv', 'w') as output_file:
	writer = csv.writer(output_file)
	for key in keys:
		if row_num % PER_TABLE == 0:
			header_row = [ "Table " + str(int((row_num / PER_TABLE) + 1))]
			writer.writerow( header_row );
			print("\nTable " + str(int((row_num / PER_TABLE) + 1)))
		print(row_dict[key][0])
		writer.writerow(row_dict[key])
		row_num = row_num + 1
print("Number of students shuffled: " + str(len(keys)))

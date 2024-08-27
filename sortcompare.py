import sys
import csv

def parse(f):
    """Takes in an open CSV file of the format first, last, email and turns
    it into a list that we can work with.
    """
    return [line.split(', ') for line in f]

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('Please use: python sortcompare.py <file>')
		sys.exit(-1)
	file1 = sys.argv[1]

	with open(file1, 'r') as f1:
		list1 = parse(f1)[0][0].upper().strip('\n').split(',')
		if '' in list1:
			list1.remove('')
		for i in sorted(list1):
			print(i)
#!/usr/bin/env python

# Write a program that given a text file will create a new text file in which 
# all the lines from the original file are numbered from 1 to n (where n is the
# number of lines in the file). [use small.txt]


def add_number():
	
	file = open('newfile.txt' , 'w')
	with open('small.txt') as f:
		count = 1
		for line in f:
			text = line.strip()
			newline = str(count) + " " + text + "\n"
			count += 1
			print newline
			file.write (newline)
	
	file.close()





def main():

	add_number()

if __name__ == '__main__':
    main()

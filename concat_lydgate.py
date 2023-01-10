import os
import unidecode
import re
import string
import ftfy

import sys

print(sys.getdefaultencoding())



def strip_extra_whitespace(s):
    # Use a regular expression to replace one or more spaces with a single space
    return re.sub(r'\s+', ' ', s)

#Steps to concatenate files

eightLine = "C:\\Users\\Matt\\Documents\\John Lydgate Works Text Files\\Religious Poems\\Eight-line rhyme royal\\Raw Text"
ballad = "C:\\Users\\Matt\\Documents\\John Lydgate Works Text Files\\Religious Poems\\Seven-line Ballad Stanza\\Raw Text"
rhymingCouplet = "C:\\Users\\Matt\\Documents\\John Lydgate Works Text Files\\Religious Poems\\Rhyming Couplet\\Raw Text"

filenames1 = os.listdir(eightLine)
filenames2 = os.listdir(ballad)
filenames3 = os.listdir(rhymingCouplet)
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
with open('C:\\Users\\Matt\\Documents\\Test_concat_file.txt', 'w') as outfile:
	for file in filenames1:
		with open(eightLine + '\\' + file,'r') as infile:
			contents = infile.read()
			contents = contents.replace('\n',' ')
			contents = contents + " "
			for char in punctuation:
				contents = contents.replace(char, ' ')
			contents = re.sub(r" — ", " ", contents, flags=re.I)
			contents = re.sub(r'[A-Za-z]', lambda x: x.group(0).lower(), contents)
			contents = strip_extra_whitespace(contents)
			outfile.write(contents)
	for file in filenames2:
		with open(ballad + '\\' + file,'r') as infile:
			contents = infile.read()
			contents = contents.replace('\n',' ')
			contents = contents + " "
			for char in punctuation:
				contents = contents.replace(char, ' ')
			contents = re.sub(r" — ", " ", contents, flags=re.I)
			contents = re.sub(r'[A-Za-z]', lambda x: x.group(0).lower(), contents)
			contents = strip_extra_whitespace(contents)
			outfile.write(contents)
	for file in filenames3:
		with open(rhymingCouplet + '\\' + file,'r') as infile:
			contents = infile.read()
			contents = contents.replace('\n',' ') 
			for char in punctuation:
				contents = contents.replace(char, ' ')
			contents = re.sub(r" — ", " ", contents, flags=re.I)
			contents = re.sub(r'[A-Za-z]', lambda x: x.group(0).lower(), contents)
			contents = contents + " "
			contents = strip_extra_whitespace(contents)
			outfile.write(contents)


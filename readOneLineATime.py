# -*- coding: utf-8 -*-
"""
Script to read one line at a time from file without newline character
"""

fileHandler = open('C:/Users/ca33443/Downloads/test_domains.txt', 'r')

listofLines = fileHandler.readlines()

for line in listofLines:
    print (line.strip())

fileHandler.close()

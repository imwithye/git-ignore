#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

from config import USER_PATH
from file_operation import read_all_from_file
from file_operation import test_folder
from file_operation import test_file

# git ignore save
def git_ignore_save(filename):
	gitignore = read_all_from_file('.gitignore')
	if gitignore=="":
		print "no .gitignore file found"
		return
	if filename=="":
		filename = raw_input("save as: ")
	filename += ".gitignore"
	filename = filename.lower()
	test_folder(USER_PATH)
	filepath = USER_PATH + filename
	if test_file(filepath):
		print filename + " already exists in " + filepath
		return
	ignorefile = open(filepath, 'w+')
	ignorefile.write(gitignore)
	ignorefile.close()
	print "save to " + filepath
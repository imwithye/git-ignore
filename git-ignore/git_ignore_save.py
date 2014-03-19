#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

from config import USER_PATH
from file_operation import read_all_from_file
from file_operation import test_folder

def git_ignore_save(filename):
	gitignore = read_all_from_file('.gitignore')
	if gitignore=="":
		print "no .gitignore file found."
		return
	if filename=="":
		filename = raw_input("save as: ")
	filename += ".gitignore"
	test_folder(USER_PATH)
	filepath = USER_PATH + filename
	ignorefile = open(filepath, 'w+')
	print "save to " + filepath
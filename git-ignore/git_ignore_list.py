#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

from config import USER_PATH
from file_operation import test_folder
from file_operation import find_all_files

# git ignore list
def git_ignore_list():
	test_folder(USER_PATH)
	files = []
	find_all_files(USER_PATH, files)
	if len(files)==0:
		return

	lists = []
	duplicate = False
	for name, path in files:
		name_lower = name.lower()
		if name_lower[-10:]==".gitignore":
			if name_lower in lists:
				duplicate = True
				print name[:-10] + "(duplicate)\t",
			else:
				lists.append(name_lower)
				print name[:-10] + "\t",

	print
	if duplicate:
		print
		print "git ignore is case-insensitive"
		print "some files are found duplicates in " + USER_PATH
	return
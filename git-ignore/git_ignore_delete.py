#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

# git ignore delete

import os
from config import USER_PATH
from file_operation import test_folder
from file_operation import test_file
from file_operation import find_all_files
from file_operation import delete_file
from file_operation import search_file

def git_ignore_delete(filenames):
	files = []
	if len(filenames)==0:
		path = os.getcwd()+"/.gitignore"
		if test_file(path):
			delete_file(path)
		else:
			print "no .gitignore found in current directory"
		return

	test_folder(USER_PATH)
	find_all_files(USER_PATH, files)
	delete_files = []
	for filename in filenames:
		path = search_file(filename, files)
		if path!="":
			delete_files.append(path)

	for delete in delete_files:
		delete_file(delete)
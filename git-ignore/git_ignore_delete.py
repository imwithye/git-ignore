#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

# git ignore delete

from config import USER_PATH
from file_operation import test_folder
from file_operation import find_all_files
from file_operation import delete_file
from file_operation import search_file

def git_ignore_delete(filenames):
	if len(filenames)==0:
		return

	files = []
	test_folder(USER_PATH)
	find_all_files(USER_PATH, files)
	delete_files = []
	for filename in filenames:
		delete_files.append(search_file(filename, files))

	for delete in delete_files:
		delete_file(delete)
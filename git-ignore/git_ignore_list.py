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
	for name, path in files:
		print name + "	",
	print ""
	return
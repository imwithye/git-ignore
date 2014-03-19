#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

import os

# list all files
def find_all_files(root, files):
	try:
		for lists in os.listdir(root):
			name = lists
			path = os.path.join(root, lists)
			if os.path.isfile(path):
				files.append((name, path))
			if os.path.isdir(path):
				find_all_files(path, files)
	except OSError:
		files = []

# search file
def search_file(language, templates):
	language = language.lower() + ".gitignore"
	for template in templates:
		if language == template[0].lower():
			return template[1]
	return ""

# read all content form a file
def read_all_from_file(filepath):
	content = ""
	try:
		file_to_read = open(filepath, 'r')
		content = file_to_read.read()
		file_to_read.close()
	except:
		content = ""
	finally:
		return content

def test_folder(path):
	if not os.path.exists(path):
		os.mkdir(path)

def test_file(path):
	return os.path.isfile(path)
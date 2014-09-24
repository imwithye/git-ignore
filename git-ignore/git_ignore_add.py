#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

from config import USER_PATH, SYS_PATH, GITHUB_PATH
from file_operation import find_all_files
from file_operation import read_all_from_file
from file_operation import search_file

# git ignore add
def git_ignore_add(languages):
	ignores = git_ignore_add_ignorelist(languages)
	if len(ignores)==0:
		print "no available git ignore file"
		return
	try:
		gitignore = open('.gitignore', 'a')
		for ignore in ignores:
			print "add gitignore file from " + ignore
			gitignore.write("# created by git-ignore\n")
			gitignore.write(read_all_from_file(ignore))
			gitignore.write("\n")
		gitignore.close()
	except IOError:
		print "cannot wirte to .gitignore file"

# get file list in three search paths
def git_ignore_add_list_file():
	user = []
	system = []
	github = []
	find_all_files(USER_PATH, user)
	find_all_files(SYS_PATH, system)
	find_all_files(GITHUB_PATH, github)
	return (user, system, github)

# create ignore file path list
def git_ignore_add_ignorelist(languages):
	user, system, github = git_ignore_add_list_file()
	ignorelist = []
	for language in languages:
		ignorefile = search_file(language, user)
		if ignorefile!="":
			ignorelist.append(ignorefile)
			continue
		ignorefile = search_file(language, system)
		if ignorefile!="":
			ignorelist.append(ignorefile)
			continue
		ignorefile = search_file(language, github)
		if ignorefile!="":
			ignorelist.append(ignorefile)
			continue	
	return ignorelist

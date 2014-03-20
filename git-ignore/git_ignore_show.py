#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

from file_operation import read_all_from_file
from git_ignore_add import git_ignore_add_ignorelist

# git ignore show
def git_ignore_show(languages):
	if len(languages)==0:
		try:
			gitignore = open('.gitignore','r')
			print gitignore.read()
			gitignore.close()
		except IOError:
			return
		return

	ignores = git_ignore_add_ignorelist(languages)
	if len(ignores)==0:
		print "no available git ignore file"
		return

	for ignore in ignores:
		print read_all_from_file(ignore)
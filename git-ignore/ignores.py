#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

import os, sys

userpath = os.path.expanduser('~') + '/.git-ignores/'
syspath = sys.path[0] + "/system-templates/"
githubpath = sys.path[0] + "/github-templates/"

# get file list in three search paths
def filelist():
	try:
		usertemplates = os.listdir(userpath)
	except OSError:
		usertemplates = []
	try:
		systemplates = os.listdir(syspath)
	except OSError:
		os.mkdir(syspath)
		systemplates = os.listdir(syspath)
	try:
		githubtemplates = os.listdir(githubpath)
	except OSError:
		githubtemplates = []

	return (usertemplates, systemplates, githubtemplates)

# search file
def searchfile(language, templates):
	language = language.lower() + ".gitignore"
	for template in templates:
		if language == template.lower():
			return template
	return ""

# create ignore file path list
def ignorelist(languages):
	user, system, github = filelist()
	ignorelist = []
	for language in languages:
		ignorefile = ""

		ignorefile = searchfile(language, user)
		if ignorefile != "":
			ignorelist.append(userpath + ignorefile)
			continue

		ignorefile = searchfile(language, system)
		if ignorefile != "":
			ignorelist.append(syspath + ignorefile)
			continue

		ignorefile = searchfile(language, github)
		if ignorefile != "":
			ignorelist.append(githubpath + ignorefile)
			continue
	return ignorelist

def readfile(filepath):
	content = ""
	try:
		ignorefile = open(filepath, 'r')
		content = ignorefile.read()
	except:
		content = ""
	finally:
		ignorefile.close()
		return content

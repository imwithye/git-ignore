#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Ciel <imwithye@gmail.com>
#
# Distributed under terms of the MIT license.

import os

userpath = os.path.expanduser('~') + '/.git-ignore-templates/'
syspath = os.getcwd() + "/system-templates/"
githubpath = os.getcwd() + "/github-templates/"

def searchpath():
	try:
		usertemplates = os.listdir(userpath)
	except OSError:
		os.mkdir(userpath)
		usertemplates = os.listdir(userpath)
	try:
		systemplates = os.listdir(syspath)
	except OSError:
		os.mkdir(userpath)
		systemplates = os.listdir(syspath)
	try:
		githubtemplates = os.listdir(githubpath)
	except OSError:
		githubtemplates = []

	return (usertemplates, systemplates, githubtemplates)

def searchfile(language, templates):
	language = language.lower() + ".gitignore"
	for template in templates:
		if language == template.lower():
			return template
	return ""

def ignorelist(languages):
	user, system, github = searchpath()
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

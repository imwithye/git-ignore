#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

import sys
from git_ignore_add import git_ignore_add
from git_ignore_save import git_ignore_save
from git_ignore_list import git_ignore_list
from git_ignore_show import git_ignore_show
from git_ignore_which import git_ignore_which
from git_ignore_delete import git_ignore_delete

# cat ignores >> .gitignore
def add(languages):
	git_ignore_add(languages)

# save current .gitignore
def save(filenames):
	if len(filenames)<1:
		filename = ""
	else:
		filename = filenames[0]
	git_ignore_save(filename)

# list all user ignore files
def list():
	git_ignore_list()

# delete user ignore files
def delete(filenames):
	git_ignore_delete(filenames)

# cat .gitignore file
def show(languages):
	git_ignore_show(languages)

# print which ignore file will be imported
def which(languages):
	git_ignore_which(languages)
		
# print usage
def usage():
	print "usage: git ignore <subcommand>"
	print
	print "Available subcommands are:"
	print "    add    <project type>    Add gitignore files. Try use 'git ignore add Python C'"
	print "    save   [project type]    Save current .gitignore file as a template"
	print "    list                     List all saved ignore templates"
	print "    delete [ignore file]     Delete .gitignore or ignore templates"
	print "    show   [ignore type]     Cat .gitignore or ignore templates"
	print "    which  <ignore type>     Show which ignore file will be imported"
	print "    usage                    Show this help message and exit"
	print "    version                  Show version and exit"
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# print version
def version():
	print "git ignore, version 0.2"
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# subcommand router
def select(argv):
	if argv[1] == "add":
		add(argv[2:])
		exit()
	elif argv[1] == "save":
		save(argv[2:])
		exit()
	elif argv[1] == "list":
		list()
		exit()
	elif argv[1] == "delete" or argv[1] == "remove":
		delete(argv[2:])
		exit()
	elif argv[1] == "show":
		show(argv[2:])
		exit()
	elif argv[1] == "which":
		which(argv[2:])
		exit()
	elif argv[1] == "help" or argv[1] == "usage":
		usage()
		exit()
	elif argv[1] == "version":
		version()
		exit()
	else:
		print "unknown subcommand"
		usage()
		exit()

if __name__ == "__main__":
	if len(sys.argv)==1:
		sys.argv.append("usage")
	select(sys.argv)

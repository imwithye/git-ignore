#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

import sys
from git_ignore_add import git_ignore_add

# cat ignores >> .gitignore
def add(languages):
	git_ignore_add(languages)

# save current .gitignore
def save(filenames):
	try:
		gitignorefile = open('.gitignore','r')
		gitignore = gitignorefile.read()
		gitignorefile.close()
	except IOError:
		print ".gitignore file not exist or can not open"
		return

	if len(filenames)==0:
		name = raw_input("save as: ")
		filenames.append(name)
	filename = filenames[0]
	try:
		savedignore = open(filename + ".gitignore", "w+")
		savedignore.write(gitignore)
	finally:
		savedignore.close()

# cat .gitignore file
def show():
	try:
		gitignore = open('.gitignore','r')
		print gitignore.read()
		gitignore.close()
	except IOError:
		print ".gitignore file not exist or can not open"
		
# print usage
def usage():
	print "usage: git ignore <subcommand>"
	print
	print "Available subcommands are:"
	print "    add         Add gitignore files. Try use 'git ignore add Python C'"
	print "    save        Save current .gitignore file as a template"
	print "    show        Cat .gitignore file"
	print "    usage       Show this help message and exit"
	print "    version     Show version and exit"
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# print version
def version():
	print "git ignore, version 0.1."
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# subcommand router
def select( argv ):
	if argv[1] == "add":
		add(argv[2:])
		exit()
	elif argv[1] == "save":
		save(argv[2:])
		exit()
	elif argv[1] == "show":
		show()
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

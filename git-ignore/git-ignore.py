#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Ciel <imwithye@gmail.com>
#
# Distributed under terms of the MIT license.

import sys
from ignores import ignorelist
from ignores import readfile

# cat ignores >> .gitignore
def language(languages):
	ignores = ignorelist(languages)
	if len(ignores)==0:
		print "no available git ignore file"
		return
	try:
		gitignore = open('.gitignore', 'a')
		for ignore in ignores:
			gitignore.write(readfile(ignore))
			gitignore.write("\n\n")
	finally:
		gitignore.close()

# save current .gitignore
def save(filename):
	print filename

# print usage
def usage():
	print "usage: git ignore <subcommand>"
	print
	print "Available subcommands are:"
	print "    language    Add gitignore files. Try use 'git ignore language Python C'"
	print "    save        Save current .gitignore file as a template"
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
	if argv[1] == "language":
		language(argv[2:])
		exit()
	elif argv[1] == "save":
		save(argv[2:])
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

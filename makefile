#
# makefile
# git ignore
# Ciel<imwithye@gmail.com>
#
prefix=/usr/local

all:
	@echo "usage: make install"
	@echo "       make uninstall"

install:
	cp -R git-ignore $(prefix)/share/
	ln -nsf $(prefix)/share/git-ignore/git_ignore.py $(prefix)/bin/git-ignore

uninstall:
	rm -rf $(prefix)/share/git-ignore
	rm $(prefix)/bin/git-ignore

# vim:ft=make
#

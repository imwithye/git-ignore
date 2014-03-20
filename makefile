#
# makefile
# git ignore
# Ciel<imwithye@gmail.com>
#
prefix=/usr/local

EXEC_FILES=git-ignore/git_ignore.py

all:
	@echo "usage: make install"
	@echo "       make uninstall"

install:
	@test -f github-flag || (echo "Run 'git submodule init && git submodule update' first." ; exit 1 )
	cp -R git-ignore $(prefix)/
	ln -sf $(prefix)/git-ignore/git_ignore.py $(prefix)/bin/git-ignore

uninstall:
	rm -rf $(prefix)/git-ignore
	rm -f $(prefix)/bin/git-ignore

# vim:ft=make
#
#!/bin/bash
#
# installer.sh
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

REPO=/tmp/ciel-im-git-ignore
if [ -d "$REPO" ]; then
	rm -rf $REPO
fi
( git clone --recursive git://github.com/imwithye/git-ignore.git "$REPO" && cd "$REPO" && make install)

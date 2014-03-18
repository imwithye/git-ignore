#!/bin/bash
#
# installer.sh
# Copyright (C) 2014 Ciel <imwithye@gmail.com>
#
# Distributed under terms of the MIT license.
#

REPO=/tmp/ciel-im-git-ignore
if [ -d "$REPO" ]; then
	rm -rf /tmp/git-ignore
fi
( git clone --recursive git://github.com/imwithye/git-ignore.git "$REPO" && cd "$REPO" && make install)

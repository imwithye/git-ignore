Git-ignore
===
Are you tired of managing your git ignore files? You probably work in this way

```Bash
mkdir myproject && cd myproject
cat /path-to-ignore-template >> .gitignore
git init
```

Or even worse, you edit your git ignore file every time. You may use git init --template a lot. But here is a more pretty solution! Try `git ignore`!

Git-ignore is a git plugin which allows you manage your git ignore files. Add ignore file to current project by using

```Bash
git ignore add Python C Java
```

Ignore files relate to Python C and Java will be added into `.gitignore` file. Git-ignore use [GitHub gitignore template](http://github.com/github/gitignore) as submodule. There are lots of language ignore files in this repository. You don't  have to create your own template. Just start using it!

Sure, of course Git-ignore provides a way to manage your own templates:).

##Install

Currently, git-ignore using a script installer to install. Try use

```Bash
curl -sSl https://raw.github.com/imwithye/git-ignore/master/installer.sh | sudo bash
```

Git-ignore will install itself to `/usr/local/share/git-ignore/` and create a symbolic link to `/usr/local/bin/git-ignore`. If the file already exists, git-ignore will override it. This can be used to upgrade git-ignore as well. This operation may require `sudo`. You can fully remove git-ignore by deleting these two files.

For manually installation, you can clone this repository and use `make install`. To remove simply use `make uninstall` (may require `sudo`).

**Start this repository if you like it:)**. I will publish it to `Howebrew` in the future. That will be much easier for installation.

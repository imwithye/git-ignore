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

For manually installation, you can clone this repository and use `make install`. To remove simply use `make uninstall` (may require `sudo`). Or you can recursive clone this repository and copy it to anywhere you like, then create a symbolic link of `git-ignore.py` as `git-ignore` to your system search path.

**Start this repository if you like it:)**. I will publish it to `Howebrew` in the future. That will be much easier for installation.

##Usage

Try `git ignore usage`. It will out put some useful information. 

Git-ignore is a quite simple tool.

`git ignore add <ignore files>`, this command allows you add multi git gitignore files to `.gitignore`. Note that there is a search path for searching ignore files. Firstly git-ignore search `~/.git-ignores/`, then `$GIT-IGNORE/system-templates`, then `$GIT-IGNORE/github-templates`. github-templates is cloned from [GitHub gitignore template](http://github.com/github/gitignore). All git ignore templates have to be named as `name.gitignore`.

To create your own template, try `git ignore save [filename]`. This command will save current `.gitignore` as `filename.gitignore` to `~/.git-ignores/`. Also you can directly create a git ignore template under `~/.git-ignores/`.

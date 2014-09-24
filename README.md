Git-ignore
===
Are you tired of managing your git ignore files? You probably work in this way

```Bash
mkdir myproject && cd myproject
cat /path-to-ignore-template >> .gitignore
git init
```

Or even worse, you edit your git ignore file every time. You may use `git init --template` a lot. But here is a more pretty solution! Try `git ignore`!

Git-ignore is a git plugin which allows you manage your git ignore files. Add ignore file to current project by using

```Bash
git ignore add python c java c++ objective-c
```

Ignore files relate to Python C and Java will be added into `.gitignore` file. Git-ignore use [GitHub gitignore template](http://github.com/github/gitignore) as submodule. There are lots of language ignore files in this repository. You don't  have to create your own template. Just start using it!

Sure, of course Git-ignore provides a way to manage your own templates:).

##Requirement

Git-ignore is fully wirtten in python 2. Make sure you have python 2 installed. And `git-ignore` use `/usr/bin/python` as default script. Do not override the system python. Report an issue if you find git-ignore cannot work on your workplace.

##Install

###OS X

Git-ignore can be installed via Homebrew. Try

```Bash
brew tap imwithye/formula
brew install git-ignore
```

**Start this project and make it popular! I will publish it to official Homebrew repository soon.**

###Linux & Unix

Currently, git-ignore using a script installer to install. Try use

```Bash
curl -sSl https://raw.github.com/imwithye/git-ignore/master/installer.sh | sudo bash
```

Git-ignore can be installed without sudo, if you have write permission on `/usr/local`.

###Manual Install

For manually installation, you can **recursively clone** this repository and use `make install`. To remove simply use `make uninstall` (may require `sudo`). Or you can **recursively clone** this repository and copy it to anywhere you like, then create a symbolic link of `git_ignore.py` as `git-ignore` to your system search path.

##Uninstall

If you install git-ignore via Homebrew, just run `brew uninstall git-ignore`.

For script or make installation, git-ignore will install itself to `/usr/local/git-ignore/` and create a symbolic link to `/usr/local/bin/git-ignore`. If the file already exists, git-ignore will override it. This can be used to upgrade git-ignore as well. This operation may require `sudo`. You can fully remove git-ignore by deleting `git-ignore` directory and `git-ignore` symbolic link.

**Again, star this repository if you like it:)**.

##Usage

Try `git ignore usage`. It will out put some useful information. 

Git-ignore is a quite simple tool.

###Add ignore

```Bash
git ignore add python java c
```

`git ignore add <ignore files>`, this command allows you add multi git gitignore files to `.gitignore`. Note that there is a search path for searching ignore files. Firstly git-ignore search `~/.git-ignores/`, then `$GIT-IGNORE/system-templates`, then `$GIT-IGNORE/github-templates`. github-templates is cloned from [GitHub gitignore template](http://github.com/github/gitignore). All git ignore templates have to be named as `name.gitignore`.

**Important, git-ignore is case-insenstive**.

###See what will be added

```Bash
git ignore show python java c
```

This command will show what will be added to your `.gitignore` file. The command without arguments will print out current `.gitignore` file.


###See which file will be added

```Bash
git ignore which python java
```

If you have two python templates, this command will out put which python template will be added.

###Save a template

```Bash
git ignore save my-python
```

To create your own template, try `git ignore save [filename]`. This command will save current `.gitignore` as `filename.gitignore` to `~/.git-ignores/`. Also you can directly create a git ignore template under `~/.git-ignores/`.

###Delete a template

```Bash
git ignore delete my-python
```

To delete your own template, try `git ignore delete [ignore file]`. This command will only remove the template under `~/.git-ignores/`. The command without arguments will remove the `.gitignore` file under current directory.

##Contribute

Git-ignore use git-flow developing model. Fork this repository then checkout a new feature. Then send a pull request.

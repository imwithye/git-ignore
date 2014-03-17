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

# Delete.py: `rm` with safety checks added

**Demo Video:**

![Terminal recording of delete.py](./assets/Demo.gif)

**Try it out:**

```bash
curl https://raw.githubusercontent.com/Songtech-0912/Safe-Delete/master/installDeletePython.sh | bash
```

## Overview

It is ***so*** often the case that I misuse the `rm` command. Take this, for example:

```bash
> rm package*
# deleted package.json and package-lock.json
```

Ahem...I just deleted my precious `package.json` while trying to delete my `package-lock.json`. Or what about this:

```bash
> ls | grep hello.txt
hello.txt

> rm -rf helo.txt
# no warning

> rm -rf helllo.txt
# no warning

> rm -rf hello.tx
# still no warning!
```

Unfortunately, the file is still there, and I have no idea that I didn't delete it. Or if this happens:

```bash
> rm -rf node_modules
# rm: cannot remove 'node_modules': Is a directory
```

Arrgh...you get the idea

**And these little things add up.**

We programmers have to use the `rm` command dozens of times a day. Every time we do something silly, wrong or even dangerous, the `rm` command is unable to correct our mistakes. What's more, the `rm` command is a **silent command**. If you run `rm -rf`, there's nothing stopping you from deleting your entire codebase - which you forgot to push to GitHub for some lazy reason.

**That is why I created delete.py.**

## Functionality

In most ways `delete.py` resembles the `rm` command, just in a more opinionated way. After all, it is basically a wrapper around `rm`, with some improvements using python. These include:

* Colorful commands with red/green/bold colors to keep things clear
* Avoiding the `is a directory` nonsense of `rm`
* Showing how to solve a particular error if you face one
* Allowing you to move something to trash rather than to permanently remove it
* (Opinionated) making moving to trash default
* (Opinionated) asking for confirms, and always setting the less destructive version as default
* (Opinionated) having only one "true" command line argument

Notably, while `delete.py` technically "absorbs" any command other than `-ff`, so you could really pass any argument to it (such as `-4u` or `-m8`), it only has one real commandline flag: `-ff`. The two f's stand for "forced force" which is why I added it.

Usage is very simple:

```bash
delete [-ff] <your-file-or-folder>
# e.g. delete ~/Downloads/Bloated-useless-stuff.gif
```

This command can be made even more simple if you read about [using aliases](#aliases) down below:

## Install

### Basic Install

To install this application, run this one-liner command:

```bash
curl https://raw.githubusercontent.com/Songtech-0912/Safe-Delete/master/installDeletePython.sh | bash
```

What this basically does is to run my `installDeletePython.sh` script after downloading it from github. This ensures you'll always have the latest, most up-to-date version of `delete.py` available from your computer.

### Install errors

* You may need to open a new terminal after running the command for `delete.py` to start working
* You will need to make sure that there is a file called `~/.profile` in your home directory

### Manual Install

First, clone the source code from GitHub:

```bash
git clone https://github.com/Songtech-0912/Safe-Delete.git && cd Safe-Delete
```

Then, copy the python script to `/usr/local/bin`:

```bash
cp delete.py /usr/local/bin/delete
```

Setup aliases:

```bash
# if you don't have a ~/.profile, create one
echo "export PATH=/usr/local/bin:$PATH" > ~/.profile
echo "alias rm='delete'" > ~/.zshrc # if you are using zsh shell (most MacOS)
echo "alias rm='delete'" > ~/.bashrc # if you are using bash shell (most GNU/Linux)
```

### Development

To start developing this application, run this command:

```bash
git clone https://github.com/Songtech-0912/Safe-Delete.git && cd Safe-Delete
```

### Aliases

To fully make use of `delete.py` however, I would recommend you *alias it* as `rm`. For those that don't know, an alias is like a command substituter, so when you type in one command, like this one:

```bash
> rm -rf my_useless_bloated_1GB_node_modules_folder
```

The alias actually runs this command in the background:

```bash
> delete node_modules
```

(In this case, the aliases used were `alias rm='delete'` and `alias node_modules='my_useless_bloated_1GB_node_modules_folder'`)

This is something that the install script will do by default, but if you are manually installing it, you will need to do this yourself. Just open your `~/.bashrc` file (if you use bash), or `~/.zshrc` file (if you use zsh)\*, and add in this line (no space before or after the equal sign):

```bash
alias rm='delete'
```

\*: Fish shell aliases are something I don't know much about, please inform me if you are experienced with it!

If you do this, your old muscle memory of `rm` doesn't need to be forcibly retaught to use `delete` instead.

## Limitations

Deleting multiple files, or using certain expressions that `rm` provides isn't always going to work with `delete.py`. For instance, the wildcard symbol (\*) which is used to delete multiple files only deletes the first file of the sequence using `delete.py`.




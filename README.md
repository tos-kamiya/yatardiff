# yatardiff

Yet-Another tar-diff tool.

It expands two tar files in some temporary directory,
then compares the directories with `diff` command,
and finally remove the all files expanded in the temporary directory.

## Usage

yatardiff: diff between two .tar files.
Recognized tar file extensions are: .tar, .tgz, .tar.gz, .tar.bz2, .tbz, .tbz2, .tar.xz, .tar.lzma, .tlz, .tar.Z

Usage:
  yatardiff -r options... tar1 tar2

All options will be passed through to `diff` command.

## Tutorial

```sh
$ mkdir d
$ cd d
$ echo a > a.txt
$ echo b > b.txt
$ mkdir sub
$ echo "sub's c" > sub/c.txt
$ tar zcvf ../d-1.tar.gz *
a.txt
b.txt
sub/
sub/c.txt
$ echo B > b.txt
$ tar zcvf ../d-2.tar.gz *
a.txt
b.txt
sub/
sub/c.txt
$ cd ..
$ yatardiff -r d-1.tar.gz d-2.tar.gz
diff -r a/a.txt b/a.txt
1c1
< b
---
> B
```


## Installation

Run `sudo pip3 install git+https://github.com/tos-kamiya/yatardiff` .
A script `yatardiff` will be copied in a directory for executables, such as `/usr/local/bin/`.

## License

Public Domain.


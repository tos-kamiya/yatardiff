# yatardiff

Yet-another Tar-Diff tool.

It expands two tar files in some temporary directory,
then compares the directories with `diff` command,
and finally remove the all files expanded in the temporary directory.

## Usage

yatardiff: diff between two .tar files.
Recognized tar file extensions are: .tar, .tgz, .tar.gz, .tar.bz2, .tbz, .tbz2, .tar.xz, .tar.lzma, .tlz, .tar.Z

Usage:  
  yatardiff -r options... tar1 tar2  
  yatardiff --git options... tar1 tar2  

Options:  
  --git     Use `git diff` instead of `diff`.  

All the other options will be passed through to `diff` command.

## Mini tutorial

```sh
$ mkdir d
$ cd d
$ echo A > A.txt
$ echo B > B.txt
$ tar zcvf ../d-1.tar.gz *
A.txt
B.txt
$ echo BB > B.txt
$ tar zcvf ../d-2.tar.gz *
A.txt
B.txt
$ cd ..
$ yatardiff -r d-1.tar.gz d-2.tar.gz
diff -r a/B.txt b/B.txt
1c1
< B
---
> BB
```


## Installation

Run `sudo pip3 install git+https://github.com/tos-kamiya/yatardiff` .
A script `yatardiff` will be copied in a directory for executables, such as `/usr/local/bin/`.

## License

Public Domain.


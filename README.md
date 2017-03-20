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
$ rm -rf d
$ mkdir d
$ echo A > d/A.txt
$ echo B B > d/B.txt
$ tar zcvf d-1.tar.gz d/*
d/A.txt
d/B.txt
$ echo B C > d/B.txt
$ tar zcvf d-2.tar.gz d/*
d/A.txt
d/B.txt
$ yatardiff -r d-1.tar.gz d-2.tar.gz
diff -r a/d/B.txt b/d/B.txt
1c1
< B B
---
> B C
$ yatardiff --git --word-diff d-1.tar.gz d-2.tar.gz
diff --git a/a/d/B.txt b/b/d/B.txt
index 1090f0c..a12ea8a 100644
--- a/a/d/B.txt
+++ b/b/d/B.txt
@@ -1 +1 @@
B [-B-]{+C+}
```

## Installation

Run `sudo pip3 install git+https://github.com/tos-kamiya/yatardiff` .
A script `yatardiff` will be copied in a directory for executables, such as `/usr/local/bin/`.

## License

Public Domain.

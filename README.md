# ytdiff

Yet-another Tar-Diff tool.

It mounts (or expands) two tar files in a temporary directory,
then compares the directories with `diff` command,
and finally remove the temporary directory.

## Usage

```
ytdiff: diff between two .tar files.
Recognized tar file extensions are: .tar, .tgz, .tar.gz, .tar.bz2, .tbz, .tbz2, .tar.xz, .tar.lzma, .tlz, .tar.Z

Usage:  
  ytdiff -r options... tar1 tar2  
  ytdiff --git options... tar1 tar2  

Options:  
  --git     Use `git diff` instead of `diff`.  
  --tar     Use `tar` to expand files to temporary directory.

All the other options will be passed through to `diff` command.
```

## Mini tutorial

```sh
$ # prepare two directories
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
$
$ # compare the directories
$ ytdiff -r d-1.tar.gz d-2.tar.gz
diff -r a/d/B.txt b/d/B.txt
1c1
< B B
---
> B C
$
$ # compare the directories with git-diff
$ ytdiff --git --word-diff d-1.tar.gz d-2.tar.gz
diff --git a/a/d/B.txt b/b/d/B.txt
index 1090f0c..a12ea8a 100644
--- a/a/d/B.txt
+++ b/b/d/B.txt
@@ -1 +1 @@
B [-B-]{+C+}
```

## Installation

Prerequisites: diff (or git), fusermount, archivemount, and python3.

To install, run `sudo pip3 install git+https://github.com/tos-kamiya/ytdiff` .
A script `ytdiff` will be copied in a directory for executables, such as `/usr/local/bin/`.

To uninstall run `sudo pip3 uninstall ytdiff` .

## License

Public Domain.

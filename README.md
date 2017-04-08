# ytdiff

Yet-another Tar-Diff tool.

It mounts (or expands) two tar files in a temporary directory,
then compares the directories with `diff` command,
and finally remove the temporary directory.

## Usage

```
ytdiff: Diff between two .tar files.
Recognized tar file extensions are: {extensions}

Usage:
  {f} -r <options>... <tar1> <tar2>
  {f} --git <options>... <tar1> <tar2>
  {f} <options>... <gzip1> <gzip2>

Options:
  --git     Use `git diff` instead of `diff`.
  -r        Recursive option, passed through to diff command.

All the other options will be passed through to `diff` command.
```

## Mini tutorial

Let make two directories to be compared as follows:

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
```

Compare the two directories.

```sh
$ ytdiff -r d-1.tar.gz d-2.tar.gz
diff -r a/d/B.txt b/d/B.txt
1c1
< B B
---
> B C
```

Compare them with `git diff` command, instead of `diff` command.

````sh
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

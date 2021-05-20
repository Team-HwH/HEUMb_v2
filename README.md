# HwH (HEUM)b 2.0

## Commit message guideline

> `[ create (file) ]`\
: Use this commit message when you create any file.

> `[ update (file) ]`\
: Use this commit message when you update any file.

> `[ delete (file) ]`\
: Use this commit message when you delete any file.

> `[ rename (previous name) to (file) ]`\
: Use this commit message when you rename any file.

> `[ move (file) to (directory) ]`\
: Use this commit message when you move any file into somewhere.

### *Guideline for file name*
If there's any modification for a file which has the same name of the file in other directory, you should write your commit message like this:
```
[ (message) (file) of (parent directory) ]

e.g.
[ update source.py of AES ]
[ move source.py of CRYPTO to AES ]
```
But when you use commit message for renamed files, the commit message should be like this:
```
[ rename (previous name) to (file) in (parent directory) ]

e.g.
[ rename source.py to AES.py in AES ]
```
If the file is in the root directory of the repository, you don't have to write your commit message like this.

It's not necessary but you want to write description of your commit message; you can write the purpose of your committing.

# [LICENSE](LICENSE)
This software is protected by GNU GPL 3.0 license.

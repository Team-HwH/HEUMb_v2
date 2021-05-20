# CRYPTO
This directory is created for the codes of crypto algorithms and some small functionalities.

## Functions

```python
FILE_COMP(Files, Dest)
```

`Files` is a string list, and `Dest` is a string.

This function compresses the files which `Files` refers, and save to the file which `Dest` refers(`Dest` must be an absolute path).

___

```python
FILE_DECOMP(File, Dest)
```

`File` is a file object, and `Dest` is a string.

This function decompresses the files which `File` refers, and save to the path which `Dest` refers(`Dest` must be an absolute path).
___

```python
PUT_HEADER(Password, File)
```

`Password` is a string, and `File` is a file object.

This function creates the (HEUM)b file header to the file which `File` refers.

___

```python
REMOVE_HEADER(Password, File)
```

`Password` is a string, and `File` is a file object.

This function removes the (HEUM)b file header from the file which `File` refers.

## Subordinate functionalities

### [AES](./AES)

### [A5/1](./A5_1)

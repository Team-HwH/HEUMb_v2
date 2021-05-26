# CRYPTO
This directory is created for the codes of crypto algorithms and some small functionalities.

## Functions

```python
FILE_COMP(Files, Dest)
```

`Files` is a string list, and `Dest` is a string.

This function compresses the files which `Files` refers, and saves to the file which `Dest` refers(`Dest` must be an absolute path).

___

```python
FILE_DECOMP(File, Dest)
```

`File` is a file object, and `Dest` is a string.

This function decompresses the files which `File` refers, and saves to the path which `Dest` refers(`Dest` must be an absolute path).
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

___

```python
encrypt(Files, Password, Dest)
```

`Files` is a list, `Password` is a string, and `Dest` is a string.

This function encrypts the files which `Files` refer with `Password` to the path which `Dest` refers.

___

```python
decrypt(Filepath, Password, Dest)
```

`Filepath` is a string, `Password` is a string, and `Dest` is a string.

This function decrypts the (HEUM)b decrypted file which `Filepath` refers with `Password` to the path which `Dest` refers.

## Subordinate directories

### [AES](./AES)

### [A5/1](./A5_1)

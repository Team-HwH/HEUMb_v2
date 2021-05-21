import os
import hashlib
import tarfile
from CRYPTO.AES.aes import *


def FILE_COMP(Files, Dest):
    tmppath = 'C:\\Program Files\\HwH (HEUM)b\\tmp\\'
    os.system(f'> NUL mkdir "{tmppath}"')
    for File in Files:
        os.system(f'> NUL move "{File}" "{tmppath}"')

    with tarfile.open(Dest, 'w:xz') as tar:
        tar.add(tmppath, arcname='Secret')

    os.system(f'> NUL rd /s /q "{tmppath}"')

    f = open(Dest, 'rb+')

    return f


def FILE_DECOMP(File, Dest):
    try:
        filename = File.name
        File.close()

        with tarfile.open(filename) as tar:
            tar.extractall(path=Dest)
        
        os.system(f'> NUL del "{filename}"')
    except Exception as ex:
        print(str(ex))
        return -1

    return 0


def PUT_HEADER(Password, File):
    filename = File.name

    File.seek(0)

    f = open(filename + '.temp', 'wb+')
    f.write(b'HEUMB')
    f.write(hashlib.sha512(Password.encode('utf-8')).digest())
    f.write(b'\0' * 24)

    while True:
        chunk = File.read(64*1024)

        if len(chunk) == 0:
            break

        f.write(chunk)

    File.close()
    f.close()

    os.system(f'> NUL del "{filename}" && > NUL move "{filename + ".temp"}" "{filename}"')

    f = open(filename, 'rb+')

    return f


def REMOVE_HEADER(Password, File):
    File.seek(0)

    signature = File.read(5).decode()

    if signature != 'HEUMB':
        print('This is not (HEUM)b encrypted file!')
        exit(0)

    passhash = File.read(64)

    if passhash != hashlib.sha512(Password.encode('utf-8')).digest():
        print('Password incorrect!')
        exit(0)

    chunksize = 64*1024

    wpos = 0
    rpos = File.tell()

    while True:
        File.seek(rpos)

        chunk = File.read(chunksize)

        if len(chunk) == 0:
            break

        rpos = File.tell()

        File.seek(wpos)

        File.write(chunk)

        wpos = File.tell()

    File.truncate(os.path.getsize(File.name) - 69)

    return File
import os
import struct
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES


def ENC_AES(Password, File):
    headersize = 69
    filesize = os.path.getsize(File.name) - headersize - 24

    iv = Random.new().read(AES.block_size)

    File.seek(headersize)

    Password = hashlib.sha256(Password.encode('utf-8')).digest()
    chunksize = 64 * 1024
    File.write(iv)
    File.write(struct.pack('<Q', filesize))

    aes = AES.new(Password, AES.MODE_CBC, iv)

    pos = File.tell()

    while True:
        File.seek(pos)
        chunk = File.read(chunksize)

        if len(chunk) == 0:
            break

        if len(chunk) % 16 != 0:
            chunk += b' ' * (16 - len(chunk) % 16)

        chunk = aes.encrypt(chunk)

        File.seek(pos)
        File.write(chunk)
        pos = File.tell()

    return File


def DEC_AES(Password, File):
    filename = File.name

    File.seek(0)

    iv = File.read(16)
    originsize = struct.unpack('<Q', File.read(struct.calcsize('Q')))[0]
    Password = hashlib.sha256(Password.encode('utf-8')).digest()
    chunksize = 64*1024

    aes = AES.new(Password, AES.MODE_CBC, iv)

    rpos = File.tell()
    wpos = 0

    while True:
        File.seek(rpos)
        chunk = File.read(chunksize)
        rpos = File.tell()

        if len(chunk) == 0:
            break

        chunk = aes.decrypt(chunk)

        File.seek(wpos)
        File.write(chunk)
        wpos = File.tell()

    File.truncate(originsize)

    return File
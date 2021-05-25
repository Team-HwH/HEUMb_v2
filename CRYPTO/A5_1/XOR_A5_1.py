import hashlib


def Shift(x, cnt, X):
    for i in range(cnt-1):
        x[i] = x[i+1]
    x[i] = X



def MakeKey(x, y, z):
    c = 0
    check = x[10] + y[11] + z[12]
    
    if check > 1:
        c = 1
    
    if x[10] == c:
        X = x[5] ^ x[2] ^ x[1] ^ x[0]
        Shift(x, 19, X)
        
    if y[11] == c:
        Y = y[1] ^ y[0]
        Shift(y, 22, Y)
        
    if z[12] == c:
        Z = z[15] ^ z[2] ^ z[1] ^ z[0]
        Shift(z, 23, Z)

    return x[0] ^ y[0] ^ z[0]



def A5_1(Password):
    x = list(Password[:19])
    y = list(Password[19:41])
    z = list(Password[41:])

    x = list(map(int, x))
    y = list(map(int, y))
    z = list(map(int, z))
    
    
    KeyStream = []
    for i in range(32):
        KeyStream.append(MakeKey(x, y, z))

    KeyStream = ''.join(map(str, KeyStream))
    KeyStream = hex(int(KeyStream,2))
    
    return KeyStream



def CheckPassword(Password):
    enc = hashlib.md5()
    enc.update(Password.encode('utf-8'))

    encText = enc.hexdigest()
    
    enc1 = bin(int(encText[:16], 16))
    enc2 = bin(int(encText[16:], 16))

    enc1 = str(enc1)[2:].rjust(64,"0")
    enc2 = str(enc2)[2:].rjust(64,"0")

    Key1 = A5_1(enc1)
    Key2 = A5_1(enc2)

    return Key1, Key2



def XOR_A5_1(Password, File, Mode='enc'):
    Key1, Key2 = CheckPassword(Password)

    K = []

    m = 0x1000000
    n = 0x100

    for i in range(4):
        K1 = int(Key1, 16) // m % n
        K2 = int(Key2, 16) // m % n
        K.append(K1^K2)
        m = m // 0x100

    encData = []

    c = 0
    
    f = File.read(1)
    
    while len(f) != 0:
        if c < 69 and Mode =='enc':
            encData.append(ord(f))
        else:
            encData.append(ord(f) ^ K[c%4])
        c = c + 1
        f = File.read(1)

    File.seek(0)

    for i in range(len(encData)):
        File.write(encData[i].to_bytes(1, byteorder="little"))
    
    return File

from _struct import unpack
import binascii
import os, sys, inspect
import struct
from core.bytes import Bytes

def set_path():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)


def str_to_array(s):
    return [int(b) for b in s.split(',')]


def block_copy(src, srcPos, dest, destPos, length):
    for i in range(length):
        dest[i + destPos] = src[i + srcPos]

def int_to_bytes(n):
    return struct.unpack('BBBB', binascii.unhexlify(format(n, 'x').zfill(8)))

def to_bytes(n, size=32):
    bits = format(n, 'b').zfill(size)
    b = []
    for i in xrange(size, 0, -8):
        b.append(int(bits[i - 8:i], 2))
    return b

def to_int32(a, off):
    return int(format(a[off + 3], 'b').zfill(8) + format(a[off + 2], 'b').zfill(8) + format(a[off + 1], 'b').zfill(8) + format(a[off], 'b').zfill(8), 2)

def circular_shift(b, w):
    return ((w << b) & 0xFFFFFFFF) | (w >> (32 - b))

def shift_key(key, n, direction=True):
    size = len(key)
    result = Bytes([0] * size)
    for i in xrange(0, size):
        if direction:
            result[(i + n) % size] = key[i];
        else:
            result[i] = key[(i + n) % size];
    return result

def xor_key(key1, key2):
    menor = min(len(key1), len(key2))
    result = Bytes([0] * menor)
    for i in xrange(0, menor):
        result[i] = key1[i] ^ key2[i]
    return result

def to_int1(s):
    return unpack('!' + (len(s) * 'B'), s)

def to_int4(s):
    return unpack('!' + ((len(s) / 4) * 'I'), s)

def to_hex(s):
    return binascii.hexlify(s)



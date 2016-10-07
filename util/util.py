from _struct import unpack
import binascii
import os, sys, inspect
import struct

import wx

from core.bytes import Bytes


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

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
            result[(i + n) % size] = key[i]
        else:
            result[i] = key[(i + n) % size]
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

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def img_transform(img, scale=None, width=None, height=None, rotate=None, color=None, gray=False):
    if color:
        if type(color) == str: color = hex_to_rgb(color)
        while len(color) < 4: color += (255,)
        img = img.AdjustChannels(color[0] / 255., color[1] / 255., color[2] / 255., color[3] / 255.)
    if gray:
        img = img.ConvertToGreyscale()
    if rotate:
        w, h = img.GetSize()
        img = img.Rotate(rotate, (w / 2., h / 2.))
    if scale:
        w, h = img.GetSize()
        img = img.Rescale(w * scale, h * scale, quality=wx.IMAGE_QUALITY_HIGH)
    elif width and height:
        img = img.Rescale(width, height, quality=wx.IMAGE_QUALITY_HIGH)
    return wx.BitmapFromImage(img)


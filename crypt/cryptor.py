
from sha import Sha

from core.bytes import Bytes
from cryptor_key import CryptorKey
from util.util import to_bytes, to_int32


class Cryptor(object):

    def __init__(self, key):
        self._key = [CryptorKey(55, 31), CryptorKey(57, 50), CryptorKey(58, 39)]
        self._change_len = 0
        self._change_data = 0
        buf = self.fill_key(key)

        for i in xrange(0, 680, 20):
            sha = Sha().digest(buf)
            for j in xrange(0, 5):
                pos = i + (j * 4)
                b = to_bytes(sha[j])
                buf[pos:pos + len(b)] = b

        for i in xrange(0, 220, 4):
            self._key[0].buffer[i / 4] = to_int32(buf, i)

        for i in xrange(0, 228, 4):
            self._key[1].buffer[i / 4] = to_int32(buf, 220 + i)

        for i in xrange(0, 232, 4):
            self._key[2].buffer[i / 4] = to_int32(buf, 448 + i)


    def fill_key(self, key):
        result = Bytes([0] * 680)
        for i in xrange(0, 680):
            result[i] = key[i % 128]
        result[0] = 128
        return result

    def apply_cryptor(self, buf, size):
        pre = size if size < self._change_len else self._change_len
        if pre != 0:
            for i in xrange(0, pre):
                buf[i] ^= (self._change_data >> (8 * (4 - self._change_len + i))) & 0xFF
            self._change_len -= pre
            size -= pre
        for i in xrange(pre, buf.len() - 3, 4):
            result = self._key[0].key & self._key[1].key | self._key[2].key & (self._key[0].key | self._key[1].key)
            for j in xrange(0, 3):
                k = self._key[j]
                if result == k.key:
                    t1 = k.buffer[k.pos1] & 0xFFFFFFFF
                    t2 = k.buffer[k.pos2] & 0xFFFFFFFF
                    t3 = t1 if t1 <= t2 else t2
                    k.sum = (t1 + t2) & 0xFFFFFFFF
                    k.key = 1 if t3 > k.sum else 0
                    k.pos1 = (k.pos1 + 1) % k.size
                    k.pos2 = (k.pos2 + 1) % k.size
                buf[i] ^= k.sum & 0xFF
                buf[i + 1] ^= (k.sum >> 8) & 0xFF
                buf[i + 2] ^= (k.sum >> 16) & 0xFF
                buf[i + 3] ^= (k.sum >> 24) & 0xFF

        remain = size & 3
        if remain != 0:
            result = self._key[0].key & self._key[1].key | self._key[2].key & (self._key[0].key | self._key[1].key)
            self._change_data = 0
            for j in xrange(0, 3):
                k = self._key[j]
                if result == k.key:
                    t1 = k.buffer[k.pos1] & 0xFFFFFFFF
                    t2 = k.buffer[k.pos2] & 0xFFFFFFFF
                    t3 = t1 if t1 <= t2 else t2
                    k.sum = (t1 + t2) & 0xFFFFFFFF
                    k.key = 1 if t3 > k.sum else 0
                    k.pos1 = (k.pos1 + 1) % k.size
                    k.pos2 = (k.pos2 + 1) % k.size
                self._change_data ^= (k.sum & 0xFFFFFFFF)

            for j in xrange(0, remain):
                buf[size + pre - remain + j] ^= (self._change_data >> (j * 8)) & 0xFF
            self._change_len = 4 - remain;


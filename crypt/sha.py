from core.bytes import Bytes
from util.util import circular_shift


class Sha(object):
    def __init__(self):
        self.computed = 0
        self.corrupted = 0

        self.length_high = 0
        self.length_low = 0

        self.message_block = Bytes([0] * 64)
        self.message_block_index = 0

        self.message_digest = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    def result(self):
        if self.corrupted: return 0
        if not self.computed:
            self.pad_message()
            self.computed = 1
        return 1

    def input(self, key):
        size = len(key)
        if size == 0: return

        if self.computed or self.corrupted:
            self.corrupted = 1
            return

        counter = 0
        while counter < size and not self.corrupted:
            self.message_block[self.message_block_index] = key[counter]
            self.message_block_index += 1
            self.length_low += 8
            self.length_low = self.length_low & 0xFFFFFFFF

            if self.length_low == 0:
                self.length_high += 1
                self.length_high &= 0xFFFFFFFF
                if self.length_high == 0:
                    self.corrupted = 1

            if self.message_block_index == 64:
                self.process_message_block()
            counter += 1

    def process_message_block(self):
        k = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
        w = [0] * 80
        temp = 0

        for i in xrange(0, 16):
            w[i] = (self.message_block[i * 4] & 0xFFFFFFFF) << 24
            w[i] |= (self.message_block[i * 4 + 1] & 0xFFFFFFFF) << 16
            w[i] |= (self.message_block[i * 4 + 2] & 0xFFFFFFFF) << 8
            w[i] |= self.message_block[i * 4 + 3]

        for i in xrange(16, 80):
            w[i] = w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]

        a = self.message_digest[0]
        b = self.message_digest[1]
        c = self.message_digest[2]
        d = self.message_digest[3]
        e = self.message_digest[4]

        for i in xrange(0, 20):
            temp = circular_shift(5, a) + ((b & c) | (~b & d)) + e + w[i] + k[0]
            temp &= 0xFFFFFFFF
            e = d
            d = c
            c = circular_shift(30, b)
            b = a
            a = temp

        for i in xrange(20, 40):
            temp = circular_shift(5, a) + (b ^ c ^ d) + e + w[i] + k[1]
            temp &= 0xFFFFFFFF
            e = d
            d = c
            c = circular_shift(30, b)
            b = a
            a = temp

        for i in xrange(40, 60):
            temp = circular_shift(5, a) + ((b & c) | (b & d) | (c & d)) + e + w[i] + k[2]
            temp &= 0xFFFFFFFF
            e = d
            d = c
            c = circular_shift(30, b)
            b = a
            a = temp

        for i in xrange(60, 80):
            temp = circular_shift(5, a) + (b ^ c ^ d) + e + w[i] + k[3]
            temp &= 0xFFFFFFFF
            e = d
            d = c
            c = circular_shift(30, b)
            b = a
            a = temp

        self.message_digest[0] = (self.message_digest[0] + a) & 0xFFFFFFFF
        self.message_digest[1] = (self.message_digest[1] + b) & 0xFFFFFFFF
        self.message_digest[2] = (self.message_digest[2] + c) & 0xFFFFFFFF
        self.message_digest[3] = (self.message_digest[3] + d) & 0xFFFFFFFF
        self.message_digest[4] = (self.message_digest[4] + e) & 0xFFFFFFFF

        self.message_block_index = 0

    def pad_message(self):
        self.message_block[self.message_block_index] = 0x80
        self.message_block_index += 1

        if self.message_block_index > 55:
            while self.message_block_index < 64:
                self.message_block[self.message_block_index] = 0
                self.message_block_index += 1
            self.process_message_block()

        while self.message_block_index < 56:
            self.message_block[self.message_block_index] = 0
            self.message_block_index += 1


        self.message_block[56] = (self.length_high >> 24) & 0xFF
        self.message_block[57] = (self.length_high >> 16) & 0xFF
        self.message_block[58] = (self.length_high >> 8) & 0xFF
        self.message_block[59] = (self.length_high) & 0xFF
        self.message_block[60] = (self.length_low >> 24) & 0xFF
        self.message_block[61] = (self.length_low >> 16) & 0xFF
        self.message_block[62] = (self.length_low >> 8) & 0xFF
        self.message_block[63] = (self.length_low) & 0xFF

        self.process_message_block()

    def digest(self, key):
        self.input(key)
        self.result()
        return self.message_digest

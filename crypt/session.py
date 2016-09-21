from core.bytes import Bytes
from crypt.cryptor import Cryptor
from util.util import shift_key, xor_key


class Session(object):

    def __init__(self, server_keys, client_keys):
        self.client_key1 = client_keys[0]
        self.client_key2 = client_keys[1]
        self.server_key1 = server_keys[0]
        self.server_key2 = server_keys[1]
        self.tmp_key_1 = shift_key(self.server_key1, 67)
        self.tmp_key_2 = xor_key(self.tmp_key_1, self.client_key1)
        self.tmp_key_1 = shift_key(self.client_key2, 29, False)
        self.decrypt_key = xor_key(self.tmp_key_1, self.tmp_key_2)
        self.decryptor = Cryptor(self.decrypt_key)
        self.tmp_key_1 = shift_key(self.server_key2, 41)
        self.decryptor.apply_cryptor(self.tmp_key_1, 128)
        self.encrypt_key = Bytes([0] * 128)
        self.encrypt_key[0:128] = self.tmp_key_1[0:128]
        self.encryptor = Cryptor(self.encrypt_key)

    def encrypt(self, data):
        self.encryptor.apply_cryptor(data, data.len())


    def decrypt(self, data):
        self.decryptor.apply_cryptor(data, data.len())

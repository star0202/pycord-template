from base64 import b64decode, b64encode
from hashlib import sha256

from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key: str):
        self.bs = AES.block_size
        self.key = sha256(key.encode()).digest()

    async def encrypt(self, raw: str):
        raw = await self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw.encode())).decode()

    async def decrypt(self, enc: str | bytes):
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        unpaded = await self._unpad(cipher.decrypt(enc[AES.block_size:]))
        return unpaded.decode('utf-8')

    async def _pad(self, s: str):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    async def _unpad(s: str | bytes):
        return s[:-ord(s[len(s) - 1:])]

from lib.crypto.crypto_interface import CryptoInterface

# DQ500 FRF data is unencrypted (encrypt-compress-method = "00")
# This is a passthrough implementation.


class DQ500(CryptoInterface):
    def decrypt(self, data: bytes):
        return data

    def encrypt(self, data: bytes):
        return data

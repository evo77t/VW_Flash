from lib.crypto.crypto_interface import CryptoInterface
import pathlib
from lib.constants import internal_path

# Same progressive substitution cipher as DQ250 (DSG), with a different 256-byte key table.
# The algorithm and key table were found in the DQ400 CBOOT at 0x80015998 (decrypt function)
# and 0x8001698c (key table) via Ghidra reverse engineering of a bench dump.
# Rolling increment is 0x167 (same as DQ250).


class DQ400(CryptoInterface):
    def decrypt(self, data: bytes):
        dq400_key = internal_path("data", "dq400_key.bin")
        dq400_key_bytes = pathlib.Path(dq400_key).read_bytes()
        counter = 0
        offset = 0
        rolling_stream_offset = 0
        last_data = 0
        output_data = []
        while counter < len(data):
            cipher_data = dq400_key_bytes[data[counter] + offset & 0xFF]
            offset += cipher_data
            offset += last_data
            rolling_stream_offset += 0x167
            offset += dq400_key_bytes[(rolling_stream_offset >> 8) & 0xFF]
            last_data = cipher_data
            output_data.append(cipher_data)
            counter += 1
        return bytes(output_data)

    def encrypt(self, data: bytes):
        dq400_key = internal_path("data", "dq400_key.bin")
        dq400_key_bytes = pathlib.Path(dq400_key).read_bytes()
        counter = 0
        offset = 0
        rolling_stream_offset = 0
        last_data = 0
        output_data = []
        while counter < len(data):
            data_byte = data[counter]
            match_index = dq400_key_bytes.index(data_byte)
            cipher_data = match_index - offset & 0xFF
            offset += data_byte
            offset += last_data
            rolling_stream_offset += 0x167
            offset += dq400_key_bytes[(rolling_stream_offset >> 8) & 0xFF]
            last_data = data_byte
            output_data.append(cipher_data)
            counter += 1
        return bytes(output_data)

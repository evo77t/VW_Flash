from lib.constants import ControlModuleIdentifier, FlashInfo
from lib.crypto import dq500

dsg_control_module_identifier = ControlModuleIdentifier(0x7E9, 0x7E1)

block_transfer_sizes_dsg = {2: 0x800, 3: 0x800}

software_version_location_dsg = {
    2: [0x0, 0x0],
    3: [0x218, 0x22B],
}

box_code_location_dsg = {2: [0x0, 0x0], 3: [0x0, 0x0]}

block_identifiers_dsg = {2: 2, 3: 3}

block_checksums_dsg = {
    2: bytes.fromhex("FFFFFFFF"),
    3: bytes.fromhex("FFFFFFFF"),
}

block_lengths_dsg = {
    2: 0xF8000,  # ASW (1015808 bytes)
    3: 0x20000,  # CAL (131072 bytes)
}

dsg_sa2_script = bytes.fromhex(
    "6805824A10680284100819734A05872506200382499318111973824A058712082001824A0181494C"
)
block_names_frf_dsg = {2: "FD_2", 3: "FD_3"}

dsg_binfile_offsets = {
    2: 0x80000,  # ASW
    3: 0x20000,  # CAL
}

dsg_binfile_size = 1540096  # 0x178000

dsg_project_name = "ST3A"

dsg_crypto = dq500.DQ500()

# Conversion dict for block name to number
block_name_to_int = {"ASW": 2, "CAL": 3}

dsg_flash_info = FlashInfo(
    None,
    block_lengths_dsg,
    dsg_sa2_script,
    block_names_frf_dsg,
    block_identifiers_dsg,
    block_checksums_dsg,
    dsg_control_module_identifier,
    software_version_location_dsg,
    box_code_location_dsg,
    block_transfer_sizes_dsg,
    dsg_binfile_offsets,
    dsg_binfile_size,
    dsg_project_name,
    dsg_crypto,
    block_name_to_int,
    None,
    None,
)

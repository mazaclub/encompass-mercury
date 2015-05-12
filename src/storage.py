import plyvel
import ast
import hashlib
import os
import sys

from storage_leveldb import LevelDBStorage
from processor import print_log, logger
from utils import bc_address_to_hash_160, hash_160_to_pubkey_address, hex_to_int, int_to_hex, Hash

def get_new_storage(config, shared, test_reorgs, db_type='leveldb'):
    """Get a storage object.

    Currently only supports leveldb
    """

    # if db_type == 'leveldb'...
    return LevelDBStorage(config, shared, test_reorgs)

"""Hashing algorithms"""

import hashlib

def sha256(x):
    return hashlib.sha256(hashlib.sha256(x).digest()).digest()

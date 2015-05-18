'''Hashing algorithms'''
import hashlib

# modules containing hash algos
import ltc_scrypt

# Most common hash algo, sha256d
#sha_256 = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
def sha_256(cls, x):
    return hashlib.sha256( hashlib.sha256(x).digest() ).digest()

# Scrypt - Litecoin implementation
#scrypt_1024 = lambda x: ltc_scrypt.getPoWHash(x)
def scrypt_1024(cls, x):
    return ltc_scrypt.getPoWHash(x)


# Dictionary of name: function
hash_algos = {
    'sha256': sha_256,
    'scrypt': scrypt_1024,
}


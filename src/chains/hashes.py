'''Hashing algorithms'''

sha_256 = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()

# Dictionary of name: function
hash_algos = {
    'sha256': sha_256,
}

handler = None

def get_handler():
    global handler
    return handler

def set_handler(h):
    global handler
    handler = h

class HashHandler(object):

    base_hash = sha_256
    pow_hash = sha_256
    header_hash = sha_256
    base58_hash = sha_256

    def __init__(self):
        # singleton
        set_handler(self)

    def set_base_hash(self, algo):
        try:
            self.base_hash = hash_algos[algo]
        except KeyError:
            self.base_hash = sha_256

    def set_pow_hash(self, algo):
        try:
            self.pow_hash = hash_algos[algo]
        except KeyError:
            self.pow_hash = sha_256

    def set_header_hash(self, algo):
        try:
            self.header_hash = hash_algos[algo]
        except KeyError:
            self.header_hash = sha_256

    def set_base58_hash(self, algo):
        try:
            self.base58_hash = hash_algos[algo]
        except KeyError:
            self.base58_hash = sha_256

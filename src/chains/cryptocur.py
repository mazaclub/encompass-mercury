import hashes

class CryptoCur(object):

    p2pkh_version = 0
    p2sh_version = 0
    genesis_hash = 0

    coin_name = 'CryptoCur'
    code = 'COIN'

    def header_hash(self, x):
        return hashes.sha256(x)

    def tx_hash(self, x):
        return hashes.sha256(x)

    def base58_hash(self, x):
        return hashes.sha256(x)

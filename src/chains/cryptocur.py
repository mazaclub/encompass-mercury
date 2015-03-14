'''Abstract class for a cryptocurrency

The CryptoCur class is intended to contain everything that a cryptocurrency
may customize. This allows fields to be overridden in the coin's subclass if needed.
'''
import hashlib

class CryptoCur(object):

    #########################
    # Chainparams constants #
    #########################

    # Pay-To-Public-Key-Hash version
    pubkey_address = 0

    # Pay-To-Script-Hash version
    script_address = 5

    # Genesis block hash
    genesis_hash = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'


    ###################
    # Hash algorithms #
    ###################

    # Algorithm used to hash block headers, txs, etc.
    Hash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()

    # Proof-of-Work hashing algorithm (same as Hash by default)
    PoWHash = Hash

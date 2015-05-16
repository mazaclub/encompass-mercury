import cryptocur
from cryptocur import CryptoCur
import hashes
from hashes import hash_algos

class Currency(CryptoCur):
    code = 'BTC'
    p2pkh_version = 0
    p2sh_version = 5

    genesis_hash = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'

    # Not necessary to define hashes here, but done so as an example
    hash_algo = hash_algos['sha256']
    pow_algo = hash_algos['sha256']
    header_hash = hash_algos['sha256']
    base58_hash = hash_algos['sha256']

    irc_channel = '#electrum'
    irc_nick_prefix = 'E_'

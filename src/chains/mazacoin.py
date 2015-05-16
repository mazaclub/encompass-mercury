import cryptocur
from cryptocur import CryptoCur
import hashes
from hashes import hash_algos

class Currency(CryptoCur):
    code = 'MZC'
    p2pkh_version = 50
    p2sh_version = 9

    genesis_hash = '00000c7c73d8ce604178dae13f0fc6ec0be3275614366d44b1b4b5c6e238c60c'

    # Not necessary to define hashes here, but done so as an example
    hash_algo = hash_algos['sha256']
    pow_algo = hash_algos['sha256']
    header_hash = hash_algos['sha256']
    base58_hash = hash_algos['sha256']

    irc_channel = '#tate'
    irc_nick_prefix = 'E_'

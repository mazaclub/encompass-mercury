"""The basis of the multi-chain system in Encompass Mercury"""
import hashes
from hashes import hash_algos

class CryptoCur(object):
    """Base class for a cryptocurrency"""

    # Abbreviation of the coin (e.g. BTC)
    code = ''

    ### Chain params ###

    # Address base58 prefix
    p2pkh_version = 0
    # Script hash base58 prefix
    p2sh_version = 0
    # Hash of block #0
    genesis_hash = '0000000000000000000000000000000000000000000000000000000000000000'

    ### Hash algorithms ###
    hash_algo = hash_algos['sha256']
    pow_hash = hash_algos['sha256']
    header_hash = hash_algos['sha256']
    base58_hash = hash_algos['sha256']

    ### IRC ###
    # IRC channel on freenode where servers meet
    irc_channel = ''

    # Nick prefix that all servers have
    irc_nick_prefix = ''

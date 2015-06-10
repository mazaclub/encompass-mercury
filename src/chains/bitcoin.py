import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 0
    p2sh_version = 5
    genesis_hash = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'

    coin_name = 'Bitcoin'
    code = 'BTC'

    irc_nick_prefix = 'E_'
    irc_channel = '#electrum'

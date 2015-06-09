import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 48
    p2sh_version = 5
    genesis_hash = '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2'
    
    coin_name = 'Litecoin'
    code = 'LTC'

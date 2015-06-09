import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 71
    p2sh_version = 33
    genesis_hash = '4e9b54001f9976049830128ec0331515eaabe35a70970d79971da1539a400ba1'

    coin_name = 'Viacoin'
    code = 'VIA'

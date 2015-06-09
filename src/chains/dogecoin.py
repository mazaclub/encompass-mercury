import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 30
    p2sh_version = 22
    genesis_hash = '1a91e3dace36e2be3bf030a65679fe821aa1d6ef92e7c9902eb318182c355691'

    coin_name = 'Dogecoin'
    code = 'DOGE'

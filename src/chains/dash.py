import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 76
    p2sh_version = 16
    genesis_hash = '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6'

    coin_name = 'Dash'
    code = 'DASH'

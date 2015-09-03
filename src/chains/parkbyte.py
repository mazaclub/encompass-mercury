import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 55
    p2sh_version = 28
    genesis_hash = '000000a49664091ce50794d84fb243cde97738534b554b2022fa00a029d0ab7c'

    coin_name = 'ParkByte'
    code = 'PKB'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)

import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 55
    p2sh_version = 117
    genesis_hash = '0000000032fe677166d54963b62a4677d8957e87c508eaa4fd7eb1c880cd27e3'

    coin_name = 'Peercoin'
    code = 'PPC'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)

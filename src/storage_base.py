"""Abstract storage class"""

class Storage(object):

    height = 0
    last_hash = None

    def get_root_hash(self):
        pass

    def get_history(self, addr):
        pass

    def get_address(self, txi):
        pass

    def get_balance(self, addr):
        pass

    def get_proof(self, addr):
        pass

    def get_utxo_value(self, addr, txi):
        pass

    def import_transaction(self, txid, tx, block_height, touched_addr):
        pass

    def revert_transaction(self, txid, tx, block_height, touched_addr, undo):
        pass

    def get_undo_info(self, height):
        pass

    def write_undo_info(self, height, bitcoind_height, undo_info):
        pass

    # necessary??
    def update_hashes(self):
        pass

    def listunspent(self, addr):
        pass

    def close(self):
        pass


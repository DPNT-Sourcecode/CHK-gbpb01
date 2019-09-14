
class SupermarketResource():

    def __init__(self, store_units):
        self.store_units = store_units
        self.store_prices = {'A': 50, 'B': 30, 'C' : 20, 'D': 15}

    
    def get_offer_price(self):
        
        for item in self.store_units:


    def _string_formatter(self, store_units):
        return ''.join([unit for unit in store_units if not unit.isdigit()])






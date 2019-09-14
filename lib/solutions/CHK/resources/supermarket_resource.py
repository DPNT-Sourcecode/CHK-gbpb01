from solutions.CHK.util.formatter_char import char_formatter


class SupermarketResource():

    STORE_ITEMS = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    STORE_OFFERS = {'A' : {'offer': 3, 'price': 130}, 'B': {'offer': 2, 'price': 45}, 'E': {'offer': 2, 'price': 30}}

    def __init__(self, store_units):
        self.store_units = list(store_units)
    
    def get_offer_price(self):
        """
        Special offer price that that is done by a supermarket based on the
        number of items bought
        """
        if self._input_validation(self.store_units) == False:
            return -1
        price = 0

        for item in self.store_units:
            price = price + self.STORE_ITEMS[item]
        
        price = self._get_offers(self.store_units, price)
        return price

    def _get_offers(self, items, price):
        """
        """
        store_items = list(set(self.store_units))
        for item in store_items:
            if item in self.STORE_OFFERS:
                print(item)
                self._get_offers(item)
                offer = self.STORE_OFFERS[item]['offer']
                total_price = int(items.count(item) / offer)
                if total_price > 0:
                    for i in range(total_price):
                        cost = self.STORE_ITEMS[item] * offer
                        offer_cost = self.STORE_OFFERS[item]['price'] 
                        price -= cost % offer_cost
        return price


    def _input_validation(self, line):
        """
        Checks if the input is valid
        """
        for item in line:
            if item not in self.STORE_ITEMS:
                return False

    def _group_offers(self, items):
        price = 0
        if 'E' == items:
            items['E'] = items['E'] - int(items['B'] / 2)
            price = ((items['E'] % 2) * 30 + int((items['E']) / 2) * 45)
        print(price)

    






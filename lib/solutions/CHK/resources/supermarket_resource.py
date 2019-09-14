from solutions.CHK.util.formatter_char import char_formatter


class SupermarketResource():

    STORE_ITEMS = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    STORE_OFFERS = {'A' : {'offer': 3, 'price': 130}, 'B': {'offer': 2, 'price': 45} }

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
        
        price = self._get_offers(list(set(self.store_units)), price)
        return price

    def _get_offers(self, items, price):
        """
        """
        for item in items:
            if item in self.STORE_OFFERS:
                offer = self.STORE_OFFERS[item]['offer']
                print('offer', offer)
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





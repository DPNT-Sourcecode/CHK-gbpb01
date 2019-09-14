from solutions.CHK.util.formatter_char import char_formatter


class SupermarketResource():

    STORE_ITEMS = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    STORE_DISCOUNT = {'A' : {'offer': 3, 'rate': 130}, 'B': {'offer': 2, 'rate': 45} }

    def __init__(self, store_units):
        self.store_units = list(store_units)
    
    def get_offer_price(self):
        """
        Special offer price that that is done by a supermarket based on the
        number of items bought
        """
        total_checkout = 0
            
        for item in self.store_units:
            total_checkout = total_checkout + 
            
        for item in self.store_units:
            if type(item) is not str or char_formatter(item) not in self.STORE_ITEMS.keys():
                total_checkout = -1
                break
            elif item[0].isdigit():
                items = char_formatter(item)
                num_items = int(item[:len(items)])
                total_checkout = ((num_items // self.STORE_DISCOUNT[items]['offer']) + self.STORE_ITEMS[items] * self.STORE_DISCOUNT[items]['rate']) + \
                                ((num_items % self.STORE_DISCOUNT[items]['offer']) * self.STORE_ITEMS[items])
                print('total_item', total_checkout)
            else:
                total_checkout = total_checkout + self.STORE_ITEMS[item]
        return total_checkout

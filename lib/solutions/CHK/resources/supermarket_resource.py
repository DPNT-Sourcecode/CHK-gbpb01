from solutions.CHK.util.formatter_char import char_formatter


class SupermarketResource():

    STORE_ITEMS = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    STORE_DISCOUNT = {'A' : {'offer': 3, 'rate': 150 / 130}, 'B': {'offer': 2, 'rate': 45 / 60}}

    def __init__(self, store_units):
        self.store_units = store_units
    
    def get_offer_price(self):
        """
        Special offer price that that is done by a supermarket based on the
        number of items bought
        """
        total_checkout = 0
        for item in self.store_units:
            if type(item) is not str or char_formatter(item) not in STORE_ITEMS.keys():
                return -1
            elif item[0].isdigit():
                items = char_formatter(item)
                num_items = int(item[:len(items)])
                total_checkout = self._total_price_offer(num_items, items)
            else:
                total_checkout += STORE_ITEMS[item]
        return total_checkout

    def _total_price_offer(self, num_item, items):
        """
        Total price of the offer based of the number of item
            Args:
                num_item (int) : number of items needed to buy to get the offer
        """
        total_price = total_price + ((num_item // STORE_DISCOUNT[items]['offer']) * STORE_ITEMS[items] * STORE_DISCOUNT[items]['rate']) + \
                                    ((num % STORE_DISCOUNT[items]['offer']) * STORE_ITEMS[items])
        return total_price




from lib.solutions.CHK.util.check_items import char_formatter


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
            if type(item) if not str or char_formatter(item) not in STORE_ITEMS:
                return -1
            elif item[0].isdigit():
                items = char_formatter(item)
                num_items = int(item[:len(items)])
                total_checkout = total_sum + ((num_item // STORE_DISCOUNT[items]['offer']) * STORE_ITEMS[items] * STORE_DISCOUNT[items]['rate']) + \
                                    ((num % STORE_DISCOUNT[items]['offer']) * STORE_ITEMS[items])
            else:
                total_checkout += STORE_ITEMS[item]
        return total_checkout

    def _total_checkout(self, )


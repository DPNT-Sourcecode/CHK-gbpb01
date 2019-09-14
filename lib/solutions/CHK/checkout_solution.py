from solutions.CHK.resources.supermarket_resource import SupermarketResource

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Checkout price of the special offer
        Args:
            skus (str): number of items
    """
    def get_char_from_str(string):
        return "".join([i for i in string if not i.isdigit()])
    skus = skus.split()
    total_sum = 0
    store_skus = {"A": 50, "B": 30, "C": 20, "D": 15}
    skus_discount = {"A": {
        "min_prod": 3,
        "rate": 130 / 150},
        "B": {
            "min_prod": 2,
            "rate": 45 / 60}
    }
    for sku in skus:
        if type(sku) is not str or get_char_from_str(sku) not in store_skus.keys():
            total_sum = -1
            break
        elif sku[0].isdigit():
            sku_str = get_char_from_str(sku)
            num = int(sku[:len(sku_str)])
            total_sum = total_sum + \
                        ((num // skus_discount[sku_str]["min_prod"]) * store_skus[sku_str] * skus_discount[sku_str]["rate"]) + \
                        ((num % skus_discount[sku_str]["min_prod"]) * store_skus[sku_str])
        else:
            total_sum = total_sum + store_skus[sku]

    return total_sum

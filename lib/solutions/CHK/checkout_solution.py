from solutions.CHK.resources.supermarket_resource import SupermarketResource

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Checkout price of the special offer
        Args:
            skus (str): number of items
    """
    supermarket = SupermarketResource(skus)
    return supermarket.get_offer_price()



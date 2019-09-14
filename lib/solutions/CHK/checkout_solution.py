from lib.solutions.CHK.resources.supermarket_resource import SupermarketResource

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """

    """
    supermarket = SupermarketResource(skus)
    return supermarket.get_offer_price()


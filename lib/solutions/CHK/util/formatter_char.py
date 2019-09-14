
def char_formatter(line):
    """
    Returns the char for the special offers
    """
    return ''.join([ch for ch in line if not ch.isdigit()])

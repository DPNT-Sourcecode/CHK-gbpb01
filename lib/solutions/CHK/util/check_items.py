"""
Helper function
"""
def char_formatter(line):
    return ''.join([ch for ch in line if not ch.isdigit()])
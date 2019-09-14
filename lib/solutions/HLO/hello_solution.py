

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """
    Hello Mihail!
        Args:
            friend_name (str) : name of your friend
    Returns:
        A string containing a message
    """
    return 'Hello, {}!'.format(friend_name.strip())
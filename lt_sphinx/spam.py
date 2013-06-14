"""
.. module:: lt_sphinx.spam


This is the spam module.  you define this by putting::

    \.. module\:: lt_sphinx.spam

into your module docsting

wich is just reStructured Text

"""


def eggs(with_spam=True):
    """
    this is the function eggs.  It gives you eggs.  with spam. even if you
    say you don't want any.

    :param with_spam: Do you want spam with that?
    :type with_spam: `Boolean`
    :returns: string, "Spam with Spam" (because we know thats what you really
            want
    """
    if not with_spam:
        # yeah right
        pass
    return "Spam with Spam"

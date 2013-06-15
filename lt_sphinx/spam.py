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

class Spam(object):
    """This is Spam, it is all Spam"""
    is_egg = None
    is_spam = None

    def __init__(self):
        """There is always spam, set up the Spam for use with other tasty
        foods, like :class:`lt_sphinx.eggs.Egg` (actually, it is `Spam`).
        """
        self.is_egg = False
        self.is_spam = True

    @classmethod
    def open_can(cls, number):
        """
        open `number` cans of spam

        :param number: Number of cans, must be postive
        :type number: positive int
        :returns: [:class:`lt_sphinx.spam.Spam`]
        :raises: :exc:`AssertionError`
        """

        assert number > 0
        return [cls() for x in xrange(number)]

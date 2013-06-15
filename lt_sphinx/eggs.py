"""
.. module:: lt_sphinx.eggs

We've added a new module.  This will have some classes and methods
"""


class Egg(object):
    """.. class::Egg
    This is an egg, which only exist to not be served with
    :class:`lt_sphinx.spam.Spam`

    @TODO: make this subclass :class:`lt_sphinx.spam.Spam`

    :members:
    """
    #TODO make lt_sphinx.spam eggs
    is_egg = None
    is_spam = None

    def __init__(self):
        """
        Create an Egg.  Really is spam
        """

        self.is_egg = False
        self.is_spam = True

    def __unicode__(self):
        return u"Spam"

    @classmethod
    def break_egg(cls, number):
        """
        break the egg to make a meal

        :param number: Number of eggs, must be postive
        :type number: positive int
        :returns: [:class:`lt_sphinx.spam.Spam`]
        :raises: :exc:`AssertionError`
        """
        assert number >0
        from lt_spinx.spam import Spam
        return [Spam() for x in xrange(number)]

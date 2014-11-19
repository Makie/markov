""" Markov Model and useful tools. """

from random import choice


class MarkovModel(object):

    """ A simple 0 order markov model with generator. """

    def __init__(self, corpus=None, text=None, order=0):
        """ Create the model from a corpus or a text stream. """
        super(MarkovModel, self).__init__()
        self.order = order
        self.db = None
        if text:
            create_from_text(text)
        if corpus:
            create_from_corpus(corpus)

    def create_from_text(self, text):
        """ Docstring for create_from_text. """
        pass

    def create_from_corpus(self, corpus):
        """ Docstring for create_from_corpus. """
        pass
        
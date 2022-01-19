import sys


class OGUtil:
    def __init__(self, logger):
        self.l = logger
    def ex(self, inp):
        raise Exception(str(inp))


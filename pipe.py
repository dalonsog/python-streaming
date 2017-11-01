#!/usr/bin/env python


class Streameable(object):
    def __init__(self, obj):
        self.obj = obj

    def pipe(self, *args):
        self.obj = self.__concatenate_functions(*args)(self.obj)
        return self

    def __concatenate_functions(self, *args):
        if len(args) > 1:
            return lambda x: args[-1]((
                self.__concatenate_functions(*args[:-1]))(x))
        else:
            return lambda x: args[0](x)

    def collect(self):
        return self.obj


class ListStream(Streameable):
    def __init__(self, obj):
        if isinstance(obj, list):
            super(ListStream, self).__init__(obj)
        else:
            raise TypeError("No list object given")

    def map(self, function):
        self.obj = [function(e) for e in self.obj]
        return self

    def filter(self, predicate):
        self.obj = [e for e in self.obj if predicate(e)]
        return self

    def for_each(self, function):
        for e in self.obj:
            function(e)
        return self

    def limit(self, l):
        self.obj = self.obj[:l]
        return self

    def sort(self, reverse=False, keygetter=None):
        self.obj = sorted(self.obj, reverse=reverse, key=keygetter)
        return self

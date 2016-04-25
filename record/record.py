# Copyright (c) GearDragon Software 2016
class Record(object):
    Unused = 0
    FORMAT = lambda n: "%08d" % (n,)
    Serialized = dict()
    
    def __init__(self, name="null")
        self.name = name
        self.serial = Record.FORMAT(Record.Unused)
        Record.Unused += 1
        Record.Serialized.update({self.serial: self})
    
    def __repr__(self):
        return repr([self.name])
    
    def __setattr__(self, name, value):
        if name == "serial":
            raise AttributeError("cannot manually set serial attribute of a record")
        else:
            super(object).__setattr__(self, name, value)
            Record.Serialized.update({self.serial: self})

    def make_callable(self, action=lambda: none): # TODO: lint
        CallableRecord.__init__(self, action, **vars(self))


class CallableRecord(Record):
    def __init__(self, name="null", action=lambda: None, **kwargs):
        Record.__init__(self, name)
        self.__action__ = action
        for kw, arg in kwargs:
            setattr(self, kw, arg)
    
    def __repr__(self):
        return repr([(self.name, self.__action__)])
    
    def __call__(self, *args, **kwargs):
        return self.__action__(*args, **kwargs)
    
    def make_uncallable(self): # TODO: lint
        del self.__action__
        del self.__call__

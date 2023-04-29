class MyDict():
    def __init__(self, dct: dict = None):
        if dct is None:
            self._dct = dict()
        else:
            self._dct = dct

    def __getitem__(self, key):
        return self._dct[key]

    def __setitem__(self, key, value):
        self._dct[key] = value

    def __delitem__(self, key):
        del self._dct[key]

    def keys_of(self, value):
        for k, v in self._dct.items():
            if v == value:
                yield k


md = MyDict()
md['lumberjack'] = 1
md['lumber'] = 2
md['lum'] = 2
print(md._dct)
print(list(md.keys_of(2)))
del md["lum"]
print(list(md.keys_of(2)))

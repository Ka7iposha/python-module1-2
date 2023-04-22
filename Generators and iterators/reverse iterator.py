class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(self.data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


lst = [1, 2, 3, 4, 5]
rev_iter = ReverseIterator(lst)
for i in rev_iter:
    print(i)


from collections import Iterator
class Test():
    def __init__(self, a, b):
        self.a = b
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        self.a += 1
        if self.a > self.b:
            raise StopIteration()
        return self.a

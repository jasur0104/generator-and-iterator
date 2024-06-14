class FibonacciIterator:
    def __init__(self, stop: int):
        self._index = 0
        self._start = 0
        self._stop = stop
        self._next = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self._index > self._stop:
            raise StopIteration('Collections out of range')
        else:
            fibonacci = self._start
            self._index += 1
            self._start, self._next = self._next, self._start + self._next
            return fibonacci
obj1=FibonacciIterator(10)
for i in obj1:
    print(i)
#fibonacci sonlarini iterator orqali qildim  bizga nechta fibonacci soni kerak bulsa kirgizamiz chiqarib beradi



"""class FibonacciIterator:
    def __init__(self):
        self._start = 0

        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibonacci = self._start
        self._start, self._next = self._next, self._start + self._next
        return fibonacci

fibo = FibonacciIterator()

for i in fibo:
    print(i)"""
#bu esa cheksiz bibonacci sonlari


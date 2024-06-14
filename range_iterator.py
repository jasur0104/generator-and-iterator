from typing import Optional
class MyRange:
    def __init__(self, start, stop, step: Optional[float] = None):
        self.start = start
        self.step = step or 1.0
        self.stop = stop
    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item
        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item
start=float(input("start="))
stop=float(input("stop="))
step=float(input("step="))

obj = MyRange(start=start, stop=stop, step=step)
for i in obj:
    print(i)
#stepimiz manfiy bolgan holat uchun ham range funksiyasini qolda yaratdm
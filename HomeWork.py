class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.current
        self.current, self.next = self.next, self.current + self.next
        self.count += 1
        return result


fibonacci = FibonacciIterator(10)
while True:
    try:
        num = next(fibonacci)
        print(num)
    except StopIteration:
        break

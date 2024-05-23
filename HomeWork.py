class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.prev, self.curr = self.curr, self.prev + self.curr
        return value


fib = Fibonacci()
# for i in range(10):
#     print(next(fib))

# try:
#     while True:
#         print(next(fib))
# except StopIteration:
#     pass


def fibonacci_gen():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


fib2 = fibonacci_gen()


def programming_languages_gen():
    try:
        while True:
            language = yield
            print("Programming language: " + language)
    except GeneratorExit:
        print("generator closed")


gen = programming_languages_gen()
next(gen)

languages = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "PHP", "Swift", "Go", "Rust"]

for i in languages:
    gen.send(i)

gen.close()

# generator gives one value at a time

def numbers():
    print("Generator started")

    yield 1

    print("After first yield")

    yield 2

    print("After second yield")

    yield 3

    print("Generator finished")


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
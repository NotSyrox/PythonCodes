def test():
    print("step 1")
    yield 1          # freezes here
    print("step 2")
    yield 2          # freezes here
    print("step 3")
    yield 3          # freezes here

for val in test():
    print(val)


def countdown(n):
    while n > 0:
        yield n
        input()  # waits until you press Enter
        n -= 1

for num in countdown(5):
    print(num)


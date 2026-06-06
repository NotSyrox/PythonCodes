# Kinda used ai for the for loop part.
askUser = int(input("Enter a number: "))


def powerOfTwo(n):
    output = []
    for i in range(n+1):
        output.append(str(2**i))
    print(" ".join(output))
powerOfTwo(askUser)
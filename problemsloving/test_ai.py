def generateRandomName():
    import string
    import random
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

def generateRandomEmail():
    import string
    import random
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

def generateRandomCountry():
    import string
    import random
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

def generateRandomCity():
    import string
    import random
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))


print(generateRandomName())
print(generateRandomEmail())
print(generateRandomCountry())
print(generateRandomCity())
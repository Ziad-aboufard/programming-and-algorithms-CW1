import time

seed = 1
length = 16
m = 2 ** 32  # modulus
c = 1103515245  # increment
a = 12345  # multiplier
number_range = int(input("please enter the max range of numbers to generate (multiples of 10)"))


def generate_seed():
    global seed
    seed = time.time()  # dynamically generate a seed based on the time passed
    # seed = 398475340 # manually set seed value
    print(f"New seed: {seed}")


def lcg(length, m, a, c):
    global seed
    if m <= 0:
        return "m must be greater than 0"
    if a <= 0:
        return "a must be greater than 0"
    if a >= m:
        return "a must be less than m"
    if c < 0:
        return "c must be greater than or equal to 0"
    if c >= m:
        return "c must be less than m"
    if seed == 1:
        generate_seed()
    while seed < 0 or seed >= m:
        generate_seed()

    for i in range(length):
        # loops on the formula Xn+1 = (aXn + c) mod m to generate the random number
        seed = (a * seed + c) % m
    return int((seed / m) * number_range)


print(lcg(length, m, c, a))
print(lcg(length, m, c, a))
print(lcg(length, m, c, a))
print(lcg(length, m, c, a))

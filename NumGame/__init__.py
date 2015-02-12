


def split_bit(string, bit, start=0):
    return [string[i:i + bit] for i in range(start, len(string), bit)]


def hex2int(string):
    return int(string, 16)


def int2hex(num):
    return hex(num).replace('0x', '')


def bin2hex():
    pass


print(hex())

print int2hex(123)
print int('123', 4)
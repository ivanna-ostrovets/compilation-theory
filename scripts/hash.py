def hash_1(value, mod=1):
    return (ord(value[0]) + ord(value[1])) % mod


def hash_2(value, mod=1):
    return (ord(value[-1]) + ord(value[-2])) % mod


def hash_3(value, mod=1):
    return (ord(value[0]) + ord(value[-1])) % mod


def hash_4(value, mod=1):
    return (ord(value[0]) + ord(value[int(len(value) / 2)]) + ord(value[-1])) % mod


def rehesh(hash_value, array_length):
    perturb_shift = hash_value
    perturb = hash_value >> perturb_shift
    j = 5 * hash_value + 1 + perturb

    return j % array_length

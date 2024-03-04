import random

BASIS = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
]


def weight(word):
    return sum(word)


def sum_words(word1, word2):
    if len(word1) != len(word2):
        return [], False
    result = [word1[i] ^ word2[i] for i in range(len(word1))]
    return result, True


def product(word1, word2):
    if len(word1) != len(word2):
        return [], False
    result = [word1[i] & word2[i] for i in range(len(word1))]
    return result, True


def distance(word1, word2):
    if len(word1) != len(word2):
        return -1, False
    result = sum(1 for i in range(len(word1)) if word1[i] != word2[i])
    return result, True


def encode_bitset(bs):
    result = [0] * 24
    for i in bs:
        res, ok = sum_words(result, BASIS[i])
        if not ok:
            return result, False
        result = res
    return result, True


def encode_string(word):
    if len(word) == 0:
        return [], False
    bin_str = ''.join(format(ord(c), '08b') for c in word)
    bit_sets = []
    for i in range(0, len(bin_str), 8):
        bs = {j for j, bit in enumerate(bin_str[i:i+8]) if bit == '1'}
        bit_sets.append(bs)
    result = []
    for i, bs in enumerate(bit_sets):
        res, ok = encode_bitset(bs)
        if ok:
            result.extend(res)
        else:
            print("ENCODING ERROR:", res, ok, bs)
    return result, True


def decode(code):
    if len(code) == 0 or len(code) % 24 != 0:
        return "", False
    res = ""
    uniques = [[0] * 24 for _ in range(4096)]
    for i in range(4096):
        bs = {j for j in range(12) if (i & (1 << j)) >> j == 1}
        v, ok = encode_bitset(bs)
        if ok:
            uniques[i] = v
        else:
            return "", False
    for i in range(0, len(code), 24):
        bin_str = code[i:i+24]
        min_dist, min_idx, repeats = 999999, 999999, 1
        for j in range(4096):
            d, ok = distance(bin_str, uniques[j])
            if d < min_dist:
                min_dist, min_idx, repeats = d, j, 1
            elif min_dist == d:
                repeats += 1
        if min_dist > 0:
            print("TRANSMISSION ERROR:\n", " GOT:     ", bin_str)
        if repeats == 1:
            bin_str = uniques[min_idx]
            if min_dist > 0:
                print("  EXPECTED:", bin_str)
        else:
            print("UNRECOVERABLE TRANSMISSION ERROR")
        res += ''.join(str(bit) for bit in bin_str[:8])
    return ''.join(chr(int(res[i:i+8], 2)) for i in range(0, len(res), 8)), True


def print_code(code):
    for i in range(len(code)):
        if i % 24 == 0 and i > 0:
            print()
        if i % 12 == 0 and i % 24 != 0:
            print(" ", end="")
        print(format(code[i], 'b'), end="")
    print()


def main():
    word = "lorem ipsum"
    print(f"Encode: \"{word}\"\n\nCode:")
    res1, ok1 = encode_string(word)
    print_code(res1)
    print("\nTransmitted Code:")
    swap = list(range(24))
    random.shuffle(swap)
    num_errors = 3
    for i in range(num_errors):
        idx = swap[i]
        res1[idx] = 1 - res1[idx]
        print(
            f"  ADD TRANSMISSION ERROR: INDEX={idx}, BIT={idx % 24} LINE={idx // 24}")
    print()
    print_code(res1)
    print()
    res2, ok2 = decode(res1)
    print(f"\nDecode: \"{res2}\"")


if __name__ == "__main__":
    main()

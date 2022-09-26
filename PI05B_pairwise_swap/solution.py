def swap_odd_even_bits(x: int) -> int:
    even_mask = 0b101010101010101010101010101010101010
    odd_mask =  0b010101010101010101010101010101010101
    even_shift = (x&even_mask) >> 1
    odd_shift  = (x&odd_mask) << 1
    return even_shift + odd_shift

if __name__ == "__main__":
    even_mask = 0b101010101010101010101010101010101010
    odd_mask =  0b010101010101010101010101010101010101
    print(swap_odd_even_bits(120))
    print((120&even_mask) >> 1)
    print((120&odd_mask) << 1)

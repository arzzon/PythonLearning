'''
    Conversion to and from binary
    Counting of 0 and 1 in the binary
'''
if __name__ == "__main__":
    n = 5
    b = bin(5) # Returns the binary in string format with 0b as its prefix
    print(b)  # 0b101
    # Extra 0b is present in front on the binary representation
    # Get the proper binary
    B = b[2:]
    print(B)  # 101
    # Count the 1s
    print(B.count('1'))
    # Count the 0s
    print(B.count('0'))

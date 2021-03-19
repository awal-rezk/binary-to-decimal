def calc_decimal(binary):
    binary_string = str(binary) #convert binary number to string
    number_of_bits = len(binary_string)
    decimal_equivalent = 0 #holds decimal equivalent of binary number
    index = number_of_bits-1 #bit position in binary number
    for i in binary_string:
        if i != "0":#first convert individual character to integer to compare it to 0. Then, 0 x 2^any power = 0
            temp = pow(2,index)
            decimal_equivalent += temp
        index -=1 #decrement the bit position --> moving to the right in the binary number
    decimal_equivalent_string = str(decimal_equivalent)
    print("This is the corresponding decimal value: " + decimal_equivalent_string)
print("Please enter a binary number, with no leading zeroes (most significant bit).")
calc_decimal(110)



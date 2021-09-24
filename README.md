# binary-to-decimal converter
This program displays a prompt for a user to enter a binary number.  Then, the program takes that binary number and first converts it to a string to facilitate iterating through the bits of the binary number.  Then, the program determines the number of bits in the binary number as this will later be used to figure out the bit positions as one iterates through the bits.  Next, the program initializes the variable that will hold the final decimal equivalent of the binary number.  Then, the program iterates through the bits of the binary number, and for each bit, the program checks for any bits that are logical 1.  If that is the case, the program raises 2 to a power and said power is the current bit position.  The bits that are logical 0 are ignored because 0 x (2^bit_position) = 0 and moreover, 0 being added to the decimal equivalent will not change the decimal equivalent.  Next, the result of the computation for any logical 1 bit gets added to the decimal equivalent variable.  At the end of the loop, the program converts the decimal equivalent variable, which initially served as a number so it could be added to, to a string to facilitate concatenation for printing.  Finally, the program prints a message explaining the significance of the number displayed at the end, which is the decimal equivalent.     

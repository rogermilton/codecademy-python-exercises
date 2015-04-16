# advanced topics
# comprehending comprehensions

# list of numbers divisable by 3 or 5

threes_and_fives = [var for var in range(1,16) if (var % 5 == 0) or (var % 3 == 0) ]
print( threes_and_fives )

# reverse and extract alternate characters, list[start,end,stride]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print( message )

# lambda function

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
#message2 = filter(lambda x: x != "X", garbled)
#print( message2 )

# bitwise operators

print( 5 >> 4 )  # Right Shift
print( 5 << 1 )  # Left Shift
print( 8 & 5 )   # Bitwise AND
print( 9 | 4)    # Bitwise OR
print( 12 ^ 42 ) # Bitwise XOR
print( ~88 )     # Bitwise NOT

# binary number representation

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

# print binary representations for numbers 2..5

for i in range(2,6):
    print( i, " ",bin(i))
    
# int's 2nd parameter specifies the base of the number in the string

print("int's 2nd parameter specifies the base of the number in the string...")
print( int("1",2))
print( int("10",2))
print( int("111",2))
print( int("0b100",2))
print( int(bin(5),2))
# print decimal equivalent of the binary 11001001.
print( int("11001001",2))

# bit shifting

print("\nbit shifting...\n")
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print( bin(shift_right))
print( bin(shift_left))

print("\nbitwise AND...\n")
print( bin( 0b1110 & 0b101))

       

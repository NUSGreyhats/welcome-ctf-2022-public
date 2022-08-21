import sys

# Read two files as byte arrays
file0_b = bytearray(open(".\\original.pptx", 'rb').read())
file1_b = bytearray(open(".\\3", 'rb').read())
file2_b = bytearray(open(".\\2", 'rb').read())
file3_b = bytearray(open(".\\1", 'rb').read())


# First XOR
# Set the length to be the smaller one
size = len(file1_b) if len(file0_b) < len(file1_b) else len(file1_b)
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
        xord_byte_array[i] = file0_b[i] ^ file1_b[i]
	
result1 = xord_byte_array
    
    
# Second XOR   
# Set the length to be the smaller one
size = len(file2_b) if len(result1) < len(file2_b) else len(file2_b)
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = result1[i] ^ file2_b[i]
    
result2 = xord_byte_array


# Third XOR
# Set the length to be the smaller one
size = len(file3_b) if len(result2) < len(file3_b) else len(file3_b)
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = result2[i] ^ file3_b[i]
    
   

# Write the XORd bytes to the output file	
open(".\\flag.pptx", 'wb+').write(xord_byte_array)

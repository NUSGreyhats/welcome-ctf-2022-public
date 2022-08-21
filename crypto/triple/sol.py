import sys

# Read two files as byte arrays
file0_b = bytearray(open(".\\flag.pptx", 'rb').read())
file1_b = bytearray(open(".\\1", 'rb').read())
file2_b = bytearray(open(".\\2", 'rb').read())
file3_b = bytearray(open(".\\3", 'rb').read())

size = len(file0_b)



# First XOR
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = file0_b[i] ^ file1_b[i]
    
result1 = xord_byte_array
    
    
# Second XOR   
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = result1[i] ^ file2_b[i]
    
result2 = xord_byte_array


# Third XOR
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
	xord_byte_array[i] = result2[i] ^ file3_b[i]
    
   

# Write the XORd bytes to the output file	
open(".\\plaintext.pptx", 'wb+').write(xord_byte_array)

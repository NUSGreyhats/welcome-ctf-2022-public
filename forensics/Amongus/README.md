# Amongus

### Challenge Details
A hidden png is buried underneath the first amoonguss PNG file

### Key Concepts
- To know about the strucutre of a PNG image
- Basic steganography 

### Solution
- Run `binwalk --dd='png image:png:' amoonguss.png --rm` to extract the hidden png file
- Use MS paint to fill over the hidden png to reveal the flag

### Learning Objectives
A png-recgonised file is only read till its footer. Data after the footer will not be read.

### Flag
greyhats{su5$y_baKA_E5A7F5}
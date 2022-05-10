# NTW-04 Counting in Binary and Hex
Today I learned what how to convert DEC to BIN, BIN to DEC, DEC to HEX and HEX to DEC by hand. In the future you just can use a website which will automatically calculate it for you. It is however good to know how to do it by hand. 

## Key terminology
- Binary: Binary describes a numbering scheme in which there are only two possible values for each digit: 0 and 1. One physical unit can contain electricity or not => 1 or 0.  
- Bit: A bit (short for binary digit) is the smallest unit of data on a computer; each bit has a single value of either 1 or 0.  
- Byte: A byte is a unit of digital information used in computer processing and storage. A standard byte is made of eight binary digits, which are called bits. Originally, bytes could consist of any number of bits, such as six-bit bytes, but eventually, the standard byte was set at 8 bits. A single byte can be used to represent 2 to the 8th or 256 different values.  
- Decimal: Decimal means there’s 10 options or symbols to represent a number (0-9).   
- Hexadecimal: Hexadecimal is the name of the numbering system that is base 16. This system, therefore, has numerals 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, and 15. That means that two-digit decimal numbers 10, 11, 12, 13, 14, and 15 must be represented by a single numeral to exist in this numbering system. To address the two-digit decimal values, the alphabetic characters A, B, C, D, E, and F are used to represent these values in hexadecimal and are treated as valid numerals. 
- Base 2: Base 2 uses powers of 2. The possible digits are 0 and 1. Most computers are coded in binary at the most basic level!
- Base 16: Base 16 uses powers of 16. The possible digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. Some computers use hexadecimal for certain things, like color codes!

## Exercise
### Sources
- https://www.techtarget.com/whatis/definition/binary 
- https://www.webopedia.com/definitions/byte/
- https://www.sciencedirect.com/topics/engineering/hexadecimal 
- https://www.expii.com/t/base-binary-numbers-9192 
- https://www.expii.com/t/base-hexadecimal-numbers-9193
- https://www.youtube.com/watch?v=rsxT4FfRBaM 
- https://www.youtube.com/watch?v=QJW6qnfhC70    
- https://www.youtube.com/watch?v=pg-HEGBpCQk 

### Overcome challenges
- At first I had to find what excactly all the key terminology mean.
- After that I had to find out how counting in base 2 works and how to convert Decimal to Binary.
- After that I had to find out how counting in base 16 works and how to convert Decimal to Hexadecimal and reversed. 

### Results

- DEC => BIN

  VB: 
  
      128 64 32 16 8 4 2 1 

       0  0  0  1  0 0 0 0

  16 = 10000 

  128 = 1000 0000

  228 = 11100100

  112 = 1110000

  73 = 1001001

- BIN => DEC

  1010 1010 = 170
  
  1111 0000 = 240
 
  1101 1011 = 219
  
  1010 0000 = 160
 
  0011 1010 = 58

- DEC => HEX

  VB: 
      
      246/16 = 15,375 = 15 R 6
    
      15/16 = 0,9375 = 0 R 15 

      F6

  15 = F

  37 = 25

  246 = F6

  125 = 7D

  209 = D1


- HEX => DEC

VB:

    EO = 14 x 16^1 + 0 x 16^0 = 224

  88 = 136

  E0 = 224

  CB = 203

  2F = 47

  D8 = 216



 
# Part I - Programming Fundamentals

## Entering Expressions into the Interactive shell

### Integer, FLoating-point, String Data Types

Most Common data types

- Integer (Int) = 0, 1, 2
- FLoating-point number (float) = float
- String (str) = "a", "aa"

**Subtle detail** any math performed using an int and a float results in a float.

Can have blank strings (" ")

### String concatetation and replication 

Concatetation occurs only on same data type. 
"alice" + 42  = error

*However* ('alice'*5) returns 'alicealicealciealcielaicealice' - needs to be float 

Not used as much as string concatetation. 

### abs()

Returns the absolute value of the number argumment. 

In mathematics, defined as distance from zero. 

## How computers store data with binary numbers 

Example of sound->bits->Output: Grapth sound waves intensity and frequency over time. Numbers on graph can be converted to binary which go to speakers

## bin()
Convert integer number to Binary (prefixed with 0b)

## hex()
Convert a integer to a lowercase hexadecimal string (prefixed wiht 0x)

# If-else and Flow Control

## Difference between = and == operators

== two values are the same as each other 
=  puts value on the right into the variable on the left. 

## Mixing boolean and Comparism operator 

Evlauate the left expression first, then evaluete the right expression. 

(| 4 < 5 | 5 > 6 |
| -------------- | --------------- |
| True.1 | 5 > 6.1 |
| True.2 | True.2 |
        True)



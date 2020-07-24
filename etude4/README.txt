Etude 4: Counting it up
Brodie Bosecke, 5471718
Meggie Morrison, 7777435

This program prompts the user for two integer values, n and k. The program calculates NCK and for this specific program we were not allowed to use BigInteger. Our program works by simplifying the numerator and denominator by the Greatest Common Divisor until x/1. Then x is the remaining answer.

To deal with overflow (due to restrictions on BigInteger) we noticed that pascal's triangle is 'mirrored'. By making this observation, we decided that we only had to access the first half of the Pascal's triangle therefore allowing our array to never be greater than 2^32 (overflow). Lines 31-34 is only ran if(n/2 < k). (See "RESUB 4" below)


Download the attached files into the same folder.

To compile thr program, open a terminal window and cd into the directory where you downloaded the attachments. In the terminal, type 'javac Counting.java' to compile the program. To run the program, in the terminal type 'java Counting.java'

You will be prompted to input the values for N and K (i.e. 52, 5)

The program then computes the number of possibilities of unique combinations. 

RESUB 1: Changed int to long
RESUB 2: Used a non-recursive method in which the numerator array continues to simplify by the denominator array until it reaches the final answer
RESUB 3: Fixed an issue within the GCD part of finalAns. Also solved any issues when k = n-1 when the numbers are of type long. 
RESUB 4: Mathmatically, if 0.5n < k then we can set k = n - k because 50 and 1 gives us 50 possibilites, and 50 and 49 gives us 50 possibilites too. Pascals Triangle

We used the following values to test our program and got the following outputs:

N: 4
K: 2
OUTPUT: 6

N: 10
K: 3
OUTPUT: 120

N: 10
K: 4
OUTPUT:
210

N: 52
K: 5
OUTPUT: 2598960

N: 9223372036854775807
K: 1
OUTPUT: 9223372036854775807

N: 66
K: 33
OUTPUT: 7219428434016265740


N: 4294966000
K: 2
OUTPUT: 92220522363267000

N: 3810779
K: 3
OUTPUT: 9223371416043870029


We also manually calculated some of these test cases and got the same answers.

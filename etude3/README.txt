Etude 3: Arithmetic
Brodie Bosecke, 5471718

Arithmetic is a program where it takes two lines of input, the first being a series of numbers from 1 -> 10, the second line has two values, an answer and either N or L to determine which method to run the program in. The program will then try every possibility of addition and multiplication to reach the answer. This program uses recursion to find if the answer is possible to reach.

Download the attached files into the same folder

Compile both the Arith.java and ArithApp.java by running the command, "javac Arith.java" and "javac ArithApp.java". To run the program, into the command line, type "java ArithApp < test.txt", test.txt being the file you wish to run.

Some test cases I ran against my program to ensure the output was correct

1 3 5
16 N
OUTPUT: N 16 1 + 3 * 5

1 2 3 4 5 6 7
28 N
OUTPUT: N 28 1 + 2 + 3 + 4 + 5 + 6 + 7

1 200 12
10440 L
OUTPUT: L 10440 impossible

1 9 9 5
86 L
OUTPUT: L 86 1 * 9 * 9 + 5

1 8 2 6
60 L
OUTPUT: L 60 1 * 8 + 2 * 6

1 2 3
7 N
OUTPUT: N 7 1 + 2 * 3

1 2 3
9 L
OUTPUT: L 9 1 + 2 * 3

1 2 3
100 N
OUTPUT: N 100 impossible

2 2 2 2
16 N
OUTPUT: N 16 2 * 2 * 2 * 2

5 5 5 5 5
630 N
OUTPUT: N 630 5 + 5 * 5 * 5 * 5

6
6 N
OUTPUT: N 6 6

6
6 L
OUTPUT: L 6 6

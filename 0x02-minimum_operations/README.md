# 0x02. Minimum Operations

Dynamic Programming is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems.

## How Dynamic Programming (DP) works:
Identify Subproblems: Divide the main problem into smaller, independent subproblems.
Store Solutions: Solve each subproblem and store the solution in a table or array.
Build Up Solutions: Use the stored solutions to build up the solution to the main problem.
Avoid Redundancy: By storing solutions, DP ensures that each subproblem is solved only once, reducing computation time.

## 0.Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6


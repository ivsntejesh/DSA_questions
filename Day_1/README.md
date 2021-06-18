This repo contains the solutions for the DSA questions asked in Day - 1

Questions
1. Fibonacci series:
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the
second number is 1 and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a
function that takes in an integer n and returns the nth Fibonacci number.
input: 6
o/p: 5

2. Permutations:
    Write a function that takes in an array of unique integers and returns an
 array of all permutations of those integers in no particular order.
If the input array is empty, the function should return an empty array
i/p: [1,2,3]
o/p: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

3. Product sum:
     A "special" array is a non-empty array that contains either integers or other
 "special" arrays. The product sum of a "special" array is the sum of its
 elements, where "special" arrays inside it are summed themselves and then
 multiplied by their level of depth.
 i/p: [5,2, [7, -1], 3, [6, [-13, 8], 4]]
 o/p: 12
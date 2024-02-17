# cyberchallenge-3
# NOT WORKS CORRECTLY 

Alan: Alright, guys, today we'll delve into the fascinating world of public-key cryptography!

Bob: Public key?! So, we just throw our passwords out there for everyone to see?

Alan: ...not exactly, Bob. But you're on the right track. In public-key cryptography, we share some information publicly while keeping the rest private...

Charlie: Oh, I get it! It's that thing where we multiply numbers together, and then it's really hard to figure out the original numbers!

Alan: You've grasped the essence, Charlie. In public-key cryptography, we use one-way functions: easy to calculate but hard to reverse mathematical problems. It's like creating a maze: simple to design if you know the path, difficult to navigate backward.

Charlie: That's what I said, right?

Alan: Of course, factorization is just one example of a challenging problem, but there are many others: discrete logarithms, knapsack problems, learning with errors, solving multivariate systems...

Bob abruptly interrupts.

Bob: If there are so many, can't I create my own?

Alan: No, Bob, it doesn't work that way...

Bob: Wait, hear me out! I give you a large set S of distinct positive integers and a number D. Then I choose two subsets A and B of S with no common elements. But here's the twist: if you choose two numbers in the same subset (both A and B), their difference (absolute value) won't be greater than D! I bet that, given S and D, you can't calculate the maximum sum of the number of elements in A and B!

Alan: This makes no sense, Bob... Bob, can you calculate this number or not? Alan is left speechless...

**Problem Details**

**Input:**
The input consists of 2T + 1 lines:

- Line 1: the number of test cases T
- Lines 2, ..., 2T + 1: each group of 2 lines is formatted as follows:
  - Line 1: two integers separated by space, N (the size of set S), and the number D
  - Line 2: N integers separated by space, representing set S

**Output:**
The output consists of T lines, each representing the answer to the respective test case.

1
CyberChallenge.IT 2024 - Programming Test

**Score:**
Your program will be tested on various test cases grouped into subsets. To obtain the score associated with a subset, you must correctly solve all its test cases.

- Subset 1 [30 points]: 1≤T ≤20,1≤N ≤500,1≤D≤250
- Subset 2 [30 points]: 1≤T ≤20,1≤N ≤10000,1≤D≤5000
- Subset 3 [40 points]: 1≤T ≤20,1≤N ≤100000,1≤D≤50000

For each test case, each element in array S is a positive integer not exceeding 260.

**Examples**

**INPUT**
3
11 500
1598 2672 660 1864 1672 2942 1075 4744 3685 2893 2777
15 100
278 3176 4710 1836 777 3152 584 4548 1126 2195 3482
3945 4201 1556 3140
10 10
431 4202 2861 4287 2514 3694 4068 3125 2083 3434

**OUTPUT**
7
4
2

**EXPLANATION**
In the first test case, we can construct subsets as follows: A = {2672, 2942, 2893, 2777}, B = {1598, 1864, 1672}, for a total of 4 + 3 = 7 elements.
In the second case, one possibility for the subsets is: A = {3176, 3152, 3140}, B = {278}, for a total of 4 elements.
In the third test case, there are no elements with a difference less than or equal to 10, so we can choose any pair of numbers and create two single-element sets, resulting in 2 total elements.

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) complexity. Because the while loop iterations grows as the size of n growns, this means that the code will have to run additional times as n increases. The number of iterations will grow linearly


b) O(n^2) complexity. This code has nested loops that are both related to the size of n. As n increases, the number of iterations will grow exponentially


c) O(n) complexity. This code will have to run one additional time for every incremental increase in bunnies. As bunnies increases, the amount of times the code will have to run increases linearly

## Exercise II
I would treat this problem like a binary search problem. I would first try to drop an egg at f = n/2. If the egg broke that means that f = n/2 is too high so then I would try f = (0+n/2)/2. If the egg didn't break I would set f higher at f = (n/2+n)/2. I would then repeat this process recursively until I narrowed the floors that I was considering to one floor. The runtime complexity of this algorithm is O(log n). 


# 0x02. Minimum Operations

Find lowest number of operations necessary to get n characters of H

Solution:
if n <= 1 return 0
if n == 2 or n is prime return n
else
find highest prime factor of n
get result of n / highest prime factor
return sum of highest prime fact and result of division

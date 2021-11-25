# 0x00 Pascal's Triangle

Implementation of pascal's triangle in python

Algorithm:

```
input: n (number of rows required)
output: list of lists of pascal's triangle of n


if n <= 0 return []

output = [[1]] # this takes care of first row

loop from i until n - 1 # because we took care of first row
    store last array in output in temp var and append 0 to end and beginning
    create empty row array
    loop from j until (length of last array in output + 1)
        append value of (temp[j] + temp[j + 1]) to row array
    append row array to output

return output
```

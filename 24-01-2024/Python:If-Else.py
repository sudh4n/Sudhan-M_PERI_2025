"""Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example


Print the following:

8
-2
15
Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Constraints



Output Format

Print the three lines as explained above.

Sample Input 0

3
2
Sample Output 0

5
1
6
Explanation 0"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and n>2 and n<=5:
        print("Not Weird")
    elif n%2 ==0 and n > 6 and n <=20:
        print("Weird")
    else:
        print("Not Weird")



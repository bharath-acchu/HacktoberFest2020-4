'''
Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6] . Anna declines to eat item  k = bill[2] which costs 6 . If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3  . If he includes the cost of bill[2] , he will calculate (2+4+6)/2 =  6. In the second case,
 he should refund 3 to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill

Input Format

The first line contains two space-separated integers  n and k, the number of items ordered and the -based index of the item that Anna did not eat.
The second line contains 0 space-separated integers  where .
The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
Explanation 0
Anna didn't eat item bill[1] = 10,
 but she shared the rest of the items with Brian. 
 The total cost of the shared items is 3+2+9 = 14 and, split in 
 half, the cost per person is b actual = 7. Brian charged her b charged = 12 for her portion of the bill. 
 We print the amount Anna was overcharged,bcharged - bactual = 12 - 7 = 5 , on a new line.



'''

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    
    sum_ = 0
    for i in range(len(bill)):
        if i!=k:
            sum_+=bill[i]
            avg = sum_ //2

    if (b-avg) != 0:
        print((b-avg))
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

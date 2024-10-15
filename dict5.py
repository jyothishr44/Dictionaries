'''
 The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
'''
n = int(input())
sum = 0
dct = dict()
for i in range(n):
    val = int(input())
    dct.update({i:val})
for i in dct.values():
    sum+=i
print(sum)
    

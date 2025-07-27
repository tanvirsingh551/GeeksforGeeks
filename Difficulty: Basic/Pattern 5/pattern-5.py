#User function Template for python3

class Solution:
    def printTriangle(self, n):
        for i in range(n):
            for j in range(i,n):
                print('*',end=' ')
            print()
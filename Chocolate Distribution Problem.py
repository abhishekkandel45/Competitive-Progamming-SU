class Solution:
     def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        min_diff = float('inf')
        for i in range(N-M+1):
            min_diff = min(min_diff, A[i+M-1] - A[i])
        return min_diff
# Driver Code
if __name__ == "__main__":

    t=int(input())
    for _ in range(0,t):
        N=int(input())
        A=list(map(int,input().split()))
        M=int(input())
        ob=Solution()
        print(ob.findMinDiff(A,N,M))
# } Driver Code Ends
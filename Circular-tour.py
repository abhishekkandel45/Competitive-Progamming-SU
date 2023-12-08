class Solution:
    def tour(self, lis,n):
        #Code here
        start = 0
        end = 1
        curr_petrol = lis[start][0] - lis[start][1]
        while end != start or curr_petrol < 0:
            while curr_petrol < 0 and start != end:
                curr_petrol -= lis[start][0] - lis[start][1]
                start = (start + 1) % n
                if start == 0:
                    return -1
            curr_petrol += lis[end][0] - lis[end][1]
            end = (end + 1) % n
        return start

# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
# } Driver Code Ends

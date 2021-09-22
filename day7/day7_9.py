#9Check if the number is balanced
#solution taken from internet
#was confused how to take length of an integer

class Solution:

	def balancedNumber (self, N):
		LHS_sum = 0
		RHS_sum = 0

		middle = N[len (N) // 2]

		if middle >= '0' and middle <= '9':
			for i in range (len (N) // 2):
				LHS_sum += (int)(N[i])

			for i in range (len (N) // 2 + 1, len (N)):
				RHS_sum += (int)(N[i])

			if LHS_sum == RHS_sum:
				return True

			return False

		return False
t = int(input())
for tc in range(t):
    N = input()
    ob = Solution()
    if ob.balancedNumber(N):
        print(1)
    else:
        print(0)


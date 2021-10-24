# Given a list of numbers and a number k,
#return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7]
#and k of 17, return true since 10 + 7 is 17.


def solution(num, k):
	## Naive solution:
	## check all combinations:
	val = False
	for i in range(len(num)-1):
		for j in range(1, len(num)):
			if num[i]+num[j] == k:
				val = True
				break
		if val == True:
			break

	## Improvement version 1:
	## sort the numbers, have two pointers running in
			## from both sides based on the difference

	return val

print (solution([10,15,3,7], 13))
			

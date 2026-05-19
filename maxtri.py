
t = int(input())
def solve(arr):
	max_one = max_two = max_three = -9999999999999999999999
	for i in arr:
		if(i > max_one):
			max_three = max_two
			max_two = max_one
			max_one = i
		elif(i > max_two):
			max_three = max_two
			max_two = i
		elif(i > max_three):
			max_three = i
	return(max_one+max_two+max_three)

while(t > 0):
	n = int(input())
	arr= list(map(int,input().split()))
	if(n == 1): print(arr[0])
	elif(n == 2): print(arr[0]+arr[1])
	else:
		print(solve(arr))
	t -= 1

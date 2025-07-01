a=[1,2,6,9,3,7,4]
first=second=a[0]
for i in range(len(a)):
	if (a[i] > first):
		second=first
		first=a[i]
	elif(second<a[i]<first):
		second=a[i]
print(max)

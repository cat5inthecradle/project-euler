print("Problem 1\n")

i=1
s=0

while i < 1000:
	if i%3==0:
		s+=i
	elif i%5==0:
		s+=i
	i+=1

print("Finished\n--------\nSUM:",s)



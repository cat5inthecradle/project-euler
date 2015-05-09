f1=1
f2=2
f3=3
s=2

while f3<4000000:
	if f3%2==0:
		s+=f3
	f1=f2
	f2=f3
	f3=f2+f1

print(s)

#python program to check the validity of a password
#Developer Hamo@ hamprecious30@gmail.com

l, u, p, d = 0, 0, 0, 0
print("Enter your password")
x =input()

specialchar="$@_!#%*&."
smallalphabets="abcdefghijklmnopqrstuvwxyz"
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
if (len(x) >= 8):
	for i in x:

		#lowercase alphabets counts
		if (i in smallalphabets):
			l+=1		

		#uppercase alphabets counts
		if (i in capitalalphabets):
			u+=1		

		#digits counts
		
		if (i in digits):
			d+=1		

		#special characters 
		if(i in specialchar):
			p+=1	
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(x)):
	print("Strong Password")
else:
	print("Weak Password")

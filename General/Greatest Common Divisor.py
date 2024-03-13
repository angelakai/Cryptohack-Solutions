def gcd(a,b):
  #Euclidean Algorithm
	while a % b > 0:
		R = a % b
		a = b
		b = R
	return b

result=gcd(66528,52920)
print(result)

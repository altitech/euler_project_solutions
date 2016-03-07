def getPrimeFactors(num):
	pFactors = []
	n = num

	while n > 1:
		for i in range(2,num):
			if n%i == 0:
				pFactors.append(i)
				n = n/i
				break

		if len(pFactors) == 0:
			pFactors.append(num)
			break


	return pFactors

def main():
	num = 600851475143
	pFactors = getPrimeFactors(num)
	
	print(max(pFactors))

if __name__=="__main__":
	main()

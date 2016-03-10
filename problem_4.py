def isPalindrom(num):
	string = str(num)
	
	if string == string[::-1]:
		return True
	else:
		return False

def main():
	result = 0
	for n in range(999,0,-1):
		for m in range(999,0,-1):
			if(isPalindrom(n*m)):
				if result < n*m:
					result = n*m

	print result

if __name__=="__main__":
	main()
def main():
	fiblist = [1,2] #starting term
	sum = 2 #current sum
	
	i = 2
	curr = 0
	while(curr <= 4000000):
		curr = fiblist[i-2]+fiblist[i-1]
		fiblist.append(curr)	
		if curr%2==0: #add to sum, if even number
			sum += curr
		i += 1

	print sum

if __name__=="__main__":
	main()

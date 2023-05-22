
def findAndUpdate(x, arr, second_chance, frames):
	
	for i in range(frames):
		
		if arr[i] == x:
			second_chance[i] = True
			
			return True
	
	return False

def replaceAndUpdate(x, arr, second_chance, frames, pointer):
	while(True):
	
		if not second_chance[pointer]:
		
			arr[pointer] = x
			return (pointer+1)%frames
		
		second_chance[pointer] = False
		
		pointer = (pointer + 1) % frames

def printHitsAndFaults(reference_string, frames):
	
	pointer = 0
	
	pf = 0
	
	arr = [0]*frames
	
	for s in range(frames):
		arr[s] = -1
		
	second_chance = [False]*frames
	
	Str = reference_string.split(' ')
	
	l = len(Str)
	
	for i in range(l):
		x = Str[i]
		
		if not findAndUpdate(x,arr,second_chance,frames):
		
			pointer = replaceAndUpdate(x,arr,second_chance,frames,pointer)
			
			pf += 1
	
	print("Total page faults were", pf)


# Test 2:
reference_string = "2 5 10 1 2 2 6 9 1 2 10 2 6 1 2 1 6 9 5 1"
frames = 4

# Output is 11
printHitsAndFaults(reference_string,frames)

# This code is contributed by mukesh07.

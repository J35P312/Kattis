import time
#inp="aiemckgobjfndlhp"
#inp="abcdefghijklmnoprstuvxy"
inp=input()



#recursive function that "walks" through each possible solution
def recursive(past_positions,position):
	if not sequence_map[position]:
		return(past_positions)	
	else:
		highest=0
		for n in sequence_map[position]:
			#skip if the maximum points are lower than the current highest value
			if past_positions+l[n][5] < highest:
				continue
			r=recursive(past_positions+1,n)
			if r > highest:
				highest=r				
	return(highest)

sequence_map={}
l=[]
positions=[]

#itterate through every letter in the input
for i in range(0,len(inp)):
	positions.append(i)
	n=0
	letter_before=[]
	letter_before_pos=[]

	possible=0	
	letter_after=[]
	letter_after_pos=[]

	#itterate through every letter following the letter on position i
	for j in range(i,len(inp)):
		if i == j:
			continue
		#check if letter j and i is in correct order
		#not correct
		if inp[j] <= inp[i]:
			letter_before.append(inp[j])
			letter_before_pos.append(j)
			n+=1
		#correct
		else:
			possible+=1
			letter_after.append(inp[j])
			letter_after_pos.append(j)
	
	#seuence map contains all letters that follow letter[i], in the alphabet and in the input seuence
	sequence_map[i]=set(letter_after_pos)	

	#store all indormation
	l.append([i,inp[i],n,letter_before,letter_before_pos,possible,letter_after,letter_after_pos])

highest=0

evaluated=set([])
#itterate through all letters in the input
for i in range(0,len(positions)):

	#skip if letter i has alread been visited in a previous chain
	if positions[i] in evaluated:
		continue

	#check all possible "chains" starting from letter i
	t=recursive(1,positions[i])
	evaluated=evaluated.union(sequence_map[positions[i]])

	#save if longest chain is found
	if t > highest:
		highest=t

#print the answer
print(26-highest)

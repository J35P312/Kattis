import itertools
alfa=26
inp="aiemckgobjfndlhp"
inp_list=list(inp)
n=1
lists=[]



for i in range(1,len(inp) ):
	
	lists+=list(itertools.combinations(inp_list, 10))
quit()

longest=0
longest_list=[]
for l in lists:
	wrong_order=False
	for i in range(0,len(l)-1):
		if l[i] > l[i+1]:
			wrong_order=True

	if not wrong_order and len(l) > longest:
		longest=len(l)
		longest_list=l
		


print(longest_list,longest)
print(alfa-longest)
#print(lists)

	


"""The following implementation assumes that the activities 
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 

def printMaxActivities(s , f ): 
	n = len(f) 
	print ("The following activities are selected")

	# The first activity is always selected 
	i = 0
	print (i) 

	# Consider rest of the activities 
	for j in range(n): 

		# If this activity has start time greater than 
		# or equal to the finish time of previously 
		# selected activity, then select it 
		if s[j] >= f[i]: 
			print (j) 
			i = j 

# Driver program to test above function 
l =[(17,23), (2,12), (15,22), (7,15), (4,13), (6,12), (1,7), (2,20), (14,19), (3,5), (7,21)]
l= sorted(l,key = lambda x:x[1])
s =[]
f = []
for i in l:
    s.append(i[0])
    f.append(i[1])

print (l)
print (s)
print (f)
# s = [1 , 3 , 0 , 5 , 8 , 5] 
# f = [2 , 4 , 6 , 7 , 9 , 9] 
printMaxActivities(s , f) 
print (l[0],l[3],l[6])

# This code is contributed by Nikhil Kumar Singh 

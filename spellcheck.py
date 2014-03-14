

import numpy as np

def editdistance(s1,s2):
	table = np.empty((len(s1)+1,len(s2)+1,))
	table[:] = None
	table[0,:] = np.arange(len(s2)+1)
	table[:,0] = np.arange(len(s1)+1)
	for i in np.arange(len(s1))+1:
		for j in np.arange(len(s2))+1:
			replace_cost = table[i-1,j-1] + (0 if s1[i-1] == s2[j-1] else 1)
			operation_costs = [replace_cost, table[i,j-1]+1, table[i-1,j]+1]
			table[i,j] = min(operation_costs)

	return int(table[-1,-1])





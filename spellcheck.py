

#==========================================
#	Spelling Correction Library
#==========================================



import numpy as np
from bisect import bisect

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



class Speller(object):
	""" This simple speller suggests the term with the smallest Levenshtein-distance"""

	def __init__(self):
		self.vocabulary = file("words.txt").read().split("\n")

	def suggest(self,s):
		if s == "":
			raise ValueError("String s cannot be empty")

		# only calculate edit-distance for terms in vocabulary
		# which start with the same letter
		first_letter = s[0]
		start_index = bisect(self.vocabulary,first_letter)
		end_index = bisect(self.vocabulary,chr(ord(first_letter)+1))-1
		
		# find the term with the minimum edit distance
		min_ed = float("inf")
		suggested_term = None
		# we only iterate over terms with same start letter
		for term in self.vocabulary[start_index:end_index]:
			term_dist = editdistance(s,term)
			if term_dist < min_ed:
				suggested_term = term
				min_ed = term_dist

		return suggested_term




				







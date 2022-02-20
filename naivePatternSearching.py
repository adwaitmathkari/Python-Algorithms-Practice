# Python3 program for Naive Pattern 
# Searching algorithm 
def search(pat, txt): 
	M = len(pat) 
	N = len(txt) 

	# A loop to slide pat[] one by one */ 
	for i in range(N - M + 1): 
		j = 0
		
		# For current index i, check 
		# for pattern match */ 
		for j in range(0, M): 
			if (txt[i + j] != pat[j]): 
				break

		if (j == M - 1): 
			print("Pattern found at index ", i) 

# Driver Code 
if __name__ == '__main__': 
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	search(pat, txt) 

# This code is contributed 
# by PrinciRaj1992 

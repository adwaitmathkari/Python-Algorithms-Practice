"""

KMP search
Knuth Morris Pratt algorithm

Better searching patterns in strings

preprocess the pattern string
make an array lps[] which hs the length of the longest proper prefix which is also a suffix

thus if pattern is aabxbaabx

then lps=[0,1,0,0,0,1,2,3,4]
corresponding to 
[a a b x b a a b x] 
[0,1,0,0,0,1,2,3,4]

so now when matching the string, 
if we get a match upto say the k th char in pat, and the k+1 th is a mismatch, then
for checking the next one, 

since the maximum matching prefix which is also a suffix is of lps[k] length, 
you gotta check the unmatching char to the lps[k]+1 th char of pat directly


if the pattern is ababadfghabc
and the string is ababapoabdhglkjpopababadfghabcip

then ababa will match, p will not match and now, for the next matching, we know that in the string, ababap is there while in the pattern, ababad is there

the prefix taht is same as the suffix will already be matching the pattern, and thus all we need to match next is the lps[i]+1 th char in the pattern

also since the longest such prefix or suffix is chosen, it will make sure that no other case is left to check

The time complexity of this kmp is as follows
O(m^2) where m is the pattern length which is often negligible as compared to the string,
further, we always move forward and compare each and every char only once, just depends which char in the pattern we compare.




"""

# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
	M = len(pat) 
	N = len(txt) 

	# create lps[] that will hold the longest prefix suffix 
	# values for pattern 
	lps = [0]*M 
	j = 0 # index for pat[] 

	# Preprocess the pattern (calculate lps[] array) 
	computeLPSArray(pat, M, lps) 

	i = 0 # index for txt[] 
	while i < N: 
		if pat[j] == txt[i]: 
			i += 1  
			j += 1

		if j == M: 
			print("Found pattern at index " + str(i-j) )
			j = lps[j-1] 

		# mismatch after j matches 
		elif i < N and pat[j] != txt[i]: 
			# Do not match lps[0..lps[j-1]] characters, 
			# they will match anyway 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1

def computeLPSArray(pat, M, lps): 
	len = 0 # length of the previous longest prefix suffix 

	lps[0] # lps[0] is always 0 
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			# This is tricky. Consider the example. 
			# AAACAAAA and i = 7. The idea is similar 
			# to search step. 
			if len != 0: 
				len = lps[len-1] 

				# Also, note that we do not increment i here 
			else: 
				lps[i] = 0
				i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt) 

# This code is contributed by Bhavya Jain 

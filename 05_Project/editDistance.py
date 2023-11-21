import sys
import json
import ast

def editDistance(word1, word2):
	if(isinstance(word2,str)):
		len1, len2 = len(word1), len(str(word2))
		dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

		for i in range(len1 + 1):
			for j in range(len2 + 1):
				if i == 0:
					dp[i][j] = j
				elif j == 0:
					dp[i][j] = i
				elif word1[i - 1] == word2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1]
				else:
					dp[i][j] = 1 + min(dp[i - 1][j],      # deletion
						dp[i][j - 1],      # insertion
						dp[i - 1][j - 1])  # substitution
	else:
		return float('inf')

	return dp[len1][len2]

if __name__ == '__main__':
	filename1 = "tokenize_clean.txt"
	word = sys.argv[1]
#	sentence=sys.stdin.readline()
#	word=sys.stdin.readline()
	suggestions=[]
	with open(filename1, 'r', encoding="utf8") as ref:
		lookup = ref.read()
		lookup=set(ast.literal_eval(lookup))
	for key in lookup:
		value=editDistance(word,key)
		if(value <= 1):
			suggestions.append(key)
	print(suggestions)

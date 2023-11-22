import sys
import json
import ast
import re

hindi_punctuation = ['।', ',', '!', '?', ';', ':']
def tokenize_hindi(text):
        tokens=[]
        word=''
        for char in text:
                if char not in hindi_punctuation and char!=' ':
                        word+=char
                else:
                        if word:
                                hindi_script_pattern = re.compile(r'[\u0900-\u097F]+')
                                cleaned_word = ''.join(hindi_script_pattern.findall(word))
                                tokens.append(cleaned_word)
                        word=''
                        if char != ' ':
                                hindi_script_pattern = re.compile(r'[\u0900-\u097F]+')
                                cleaned_char = ''.join(hindi_script_pattern.findall(char))
                                tokens.append(cleaned_char)
        if word:
                hindi_script_pattern = re.compile(r'[\u0900-\u097F]+')
                cleaned_word = ''.join(hindi_script_pattern.findall(word))
                tokens.append(cleaned_word)
        return tokens

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
	sentence = sys.argv[1]
#	sentence=sys.stdin.readline()
#	word=sys.stdin.readline()
	
	words=tokenize_hindi(sentence)
	suggestions=[]
	with open(filename1, 'r', encoding="utf8") as ref:
		lookup = ref.read()
		lookup=set(ast.literal_eval(lookup))
	count=0
	correct=False
	for word in words:
		for key in lookup:
			value=editDistance(word,key)
			if(value == 0):
				print("This word is correct", key)
				count+=1
				correct=True
				break
			elif(value == 1 or value==2):
				suggestions.append(key)
		if(correct==False):
			print("incorrect word suggestion",word,"\n",suggestions)
		correct=False
		suggestions=[]
	if(count==len(words)):
		print("this full sentence is correct")


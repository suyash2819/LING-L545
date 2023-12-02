import sys
import json
import ast
import re

incorrect_sentences=[
    "मैंने खाना खाइया।",
    "वह बच्चा बहुत शरारति है।",
    "उसका नाम अनीता है।",
    "मैंने अपना काम पूरा किय।",
    "वह बहुत अच्छा गायकक है।",
    "तुम्हारी कहानी सुनने मे मजा आया।",
    "मैंने उसे फोन किया।",
    "वह बहुत स्मार्ट्त दिखती है।",
    "तुम्हारा नया फोन कैसा है?",
    "उसने खाना बनाय।",
    "बच्च्या ने बहुत दिनों बाद किताब पढ़ी।",
    "मैंने तुम्हें फोन किया था",
        " तुम्हारा बहन कितनी प्यारी है",
        "वह बहुत ज्यादा हँसती है",
        "तुम्हें किसने बताया था"
        "मैंने अपनी खोई हुई किताब ढूंढ ली",
        "तुमने वहाँ जाकर क्या किया था",
        "मैंने तुम्हें कहाथा जाना है"
]

incorrect_words={"खाइया","शरारति", "किय", "गायकक", "मे", "फोन", "स्मार्ट्त","बनाय","कहाथा","बच्च्या"}

correct_words={'', 'अपना', 'कितनी', 'वह', 'प्यारी', '।', 'उसे', 'पढ़ी', 'तुम्हारा', 'स्मार्ट्त', 'ज्यादा', 'उसने', 'मजा', 'बताया', 'पूरा', 'अच्छा', 'गायकक', 'अनीता', 'बाद', 'किया', 'ढूंढ', 'आया', 'है', 'कहाथा', 'नाम', 'ने', 'सुनने', 'हुई', 'नया', 'कैसा', 'हँसती', 'खाना', 'बच्चा', 'दिखती', 'जाना', 'उसका', 'फोन', 'ली', 'शरारति', 'क्या', 'मैंने', 'काम', 'तुम्हारी', 'बहन', 'कहानी', 'बहुत', 'बच्च्या', 'जाकर', 'था', 'किसने', 'तुमने', 'थामैंने', 'अपनी', 'खोई', 'दिनों', 'खाइया', 'मे', 'किय', 'किताब', 'बनाय', 'तुम्हें', 'वहाँ'}

correct_suggestions={"खाया", "शरारती", "किया", "गायक", "में", "फ़ोन", "स्मार्ट", "बनाया","कहा", "बच्चा"}

total_incorrect_words=len(incorrect_words)
total_correct_words=len(correct_words)
total_words=total_incorrect_words+total_correct_words


hindi_punctuation = ['।', ',', '!', '?', ';', ':']
def tokenize_hindi(text):
        tokens=[]
        word=''
        for char in text:
                if char not in hindi_punctuation and char!=' ':
                        word+=char
                else:
                        if word:
				#use of regex to only get hindi data and remove unnecessary data.
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
	suggestions=[]
	with open(filename1, 'r', encoding="utf8") as ref:
		lookup = ref.read()
		lookup=set(ast.literal_eval(lookup))
	count=0
	correct=False

	correct_words_predicted=set()
	incorrect_words_predicted=set()
	correct_word_suggestion=set()
	final_suggestions=[]

	for i in range(len(incorrect_sentences)):
		words=tokenize_hindi(incorrect_sentences[i])
		for word in words:
			for key in lookup:
				value=editDistance(word,key)
				if(value == 0):
					correct_words_predicted.add(key)
					correct=True
					break
				elif(value == 1 or value==2):
					suggestions.append(key)
			if(correct==False):
				incorrect_words_predicted.add(word)
				final_suggestions.extend(suggestions)
			correct=False
			suggestions=[]

	incorrect_words_predicted_count=0
	correct_words_predicted_count=0
	for w in incorrect_words_predicted:
		#if the word is in the reference incorrect words list
		if(w in incorrect_words):
			incorrect_words_predicted_count+=1

	for w in correct_words_predicted:
		#if the word is in the reference correct words list
		if(w in correct_words):
			correct_words_predicted_count+=1


	print("model accuracy", (incorrect_words_predicted_count+correct_words_predicted_count)/total_words)
	for suggestion in final_suggestions:
		#if suggestion is in the correct_suggestions list
		if(suggestion in correct_suggestions):
			correct_word_suggestion.add(suggestion)
	print("correct word suggestion accuracy: ", len(correct_word_suggestion)/len(correct_suggestions))


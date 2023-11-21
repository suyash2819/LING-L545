#hindi_text = "हिन्दी भाषा में टोकनाइज़ेशन कैसे करें, यह आपके काम आ सकता है।"
import pickle
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

inputFile='wiki.txt'
outputFile='tokenize_clean.txt'

chunk_size = 10000


#hindi_script_pattern = re.compile(r'[\u0900-\u097F]+')
#cleaned_chunk = ''.join(hindi_script_pattern.findall(hindi_text))
#print(cleaned_chunk) 

with open(inputFile, 'r', encoding='utf-8') as Infile:
	tokenized_text=[]
	i=8000
	while i>0:
		chunk = Infile.read(chunk_size)
		#hindi_script_pattern = re.compile(r'[\u0900-\u097F]+')
		#cleaned_chunk = ''.join(hindi_script_pattern.findall(chunk))
		if not chunk:
			break
		tokens=tokenize_hindi(chunk)
		tokenized_text.extend(tokens)
		i-=1

tokenizeSet=set()

for i in range(len(tokenized_text)):
        tokenizeSet.add(tokenized_text[i])


tokenized_text=str(tokenizeSet)

with open(outputFile, 'w', encoding='utf-8') as output_file:
	output_file.write(tokenized_text)

print("written")

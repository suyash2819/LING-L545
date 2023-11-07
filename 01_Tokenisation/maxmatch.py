import sys
import json

def maxmatch(sentence,lookup, word):
	if(sentence==""):
		return word
	for i in range(len(sentence),-1,-1):
		firstword=sentence[0:i]
		remainder=sentence[i:len(sentence)]
		if(firstword in lookup):
			word.append(firstword)
			return maxmatch(remainder, lookup, word)
	#no word is found
	firstword=sentence[0]
	remainder=sentence[1:len(sentence)]
	return maxmatch(remainder,lookup,word)


if __name__ == '__main__':
	filename1 = sys.argv[1]
	sentence=sys.stdin.readline()
	with open(filename1, 'r', encoding="utf8") as ref:
		lookup = ref.read()
		lookup = json.loads(lookup)
	while(sentence):
		words=maxmatch(sentence.strip(), lookup, [])
		result=""
		for word in words:
			result+=word+" "
		print(result)
		f = open("hypothesis.txt", "w")
		f.write(result)
		f.close()
		sentence=sys.stdin.readline()

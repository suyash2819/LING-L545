import sys
import json
import ast
import re
from collections import defaultdict
import itertools


sentences=['दक ु ान उस और है','कलम पानी में उगता है','मैं अपने घर पर बैठा हूँ', 'लेकिन मेरी चाई स्वादिष्ट नहीं लग रही है','यह एक उदाहरण है', 'कहानी में बहुत सारे अजीब घटनाएं होती हैं', 'यह एक दुर्लभ कार्य है', 'आप बहुत अच्छा काम करते हैं', 'मेरा घर नदी की और है', 'उसने मुझे कलम का फूल दिया']



real_word_errors={('उस','और'),('कलम','पानी'),('मेरी', 'चाई'),('चाई','स्वादिष्ट'),('सारे','अजीब'),('की', 'और'),('कलम','का')}

correct_bigram_words={('काम', 'करते'), ('घर', 'पर'), ('बहुत', 'सारे'), ('यह', 'एक'), ('करते', 'हैं'), ('मुझे', 'कलम'), ('मेरा', 'घर'), ('उसने', 'मुझे'), ('दक', 'ु'), ('ु', 'ान'), ('घर', 'नदी'), ('आप', 'बहुत'), ('लेकिन', 'मेरी'), ('और', 'है'), ('कहानी', 'में'), ('नहीं', 'लग'), ('अजीब', 'घटनाएं'), ('अपने', 'घर'), ('रही', 'है'), ('का', 'फूल'), ('उदाहरण', 'है'), ('पर', 'बैठा'), ('पानी', 'में'), ('में', 'उगता'), ('बैठा', 'हूँ'), ('कार्य', 'है'), ('उगता', 'है'), ('एक', 'दुर्लभ'), ('होती', 'हैं'), ('ान', 'उस'), ('बहुत', 'अच्छा'), ('मैं', 'अपने'), ('स्वादिष्ट', 'नहीं'), ('नदी', 'की'), ('लग', 'रही'), ('में', 'बहुत'), ('घटनाएं', 'होती'), ('फूल', 'दिया'), ('दुर्लभ', 'कार्य'), ('अच्छा', 'काम'), ('एक', 'उदाहरण')}


correct_suggestions={('की','ओर'),('कमल','का'),('उस', 'ओर'),('कमल','पानी'),('मेरी','चाय'),('चाय','स्वादिष्ट'),('सारी','अजीब')}


total_incorrect_real_word_errors=len(real_word_errors)
total_correct_bi_grams=len(correct_bigram_words)
total_bigrams=total_incorrect_real_word_errors+total_correct_bi_grams
total_correct_suggestions=len(correct_suggestions)

def edits(word):
    letters = 'अ आ इ ई उ ऊ ए ऐ ओ औ क ख ग घ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह ा ि ी ु ू ृ े ै ो ौ ् ॐ । ॥ १ २ ३ ४ ५ ६ ७ ८ ९ ०'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    deletes = [left + right[1:] for left, right in splits if right]
    inserts = [left + c + right for left, right in splits for c in letters]
    replaces = [left + c + right[1:] for left, right in splits if right for c in letters]
    transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right) > 1]

    return set(deletes + inserts + replaces + transposes)

def generate_candidate_grams(erroneous_gram,lookup_bi_gram):
	candidate_grams = defaultdict(list)

	for i, word in enumerate(erroneous_gram):
		possible_edits = edits(word)
		for edit in possible_edits:
			candidate = list(ast.literal_eval(str(erroneous_gram)))
			candidate[i] = edit
			# only take those which are present in the lookup_bi_gram
			if(tuple(ast.literal_eval(str(candidate))) in lookup_bi_gram):
				candidate_grams[word].append(tuple(ast.literal_eval(str(candidate))))

	return candidate_grams


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


def check_for_real_word_errors(sentence, corpus_ngrams_freq):
	errors=[]
	words = tokenize_hindi(sentence)
	correct_bi_grams=0
	for i in range(len(words) - 2 + 1):
		ngram = tuple(words[i:i + 2])
		if ngram in corpus_ngrams_freq:
                # Set a threshold frequency to determine low-frequency bi-grams
			frequency = corpus_ngrams_freq[ngram]
			threshold_frequency = 2
			if frequency < threshold_frequency:
				errors.append((ngram, frequency))
			else:
				correct_bi_grams+=1
		else:
			errors.append((ngram,0))

	return (errors,correct_bi_grams)

if __name__ == '__main__':
	filename1 = "bi-grams.txt"
	with open(filename1, 'r', encoding="utf8") as ref:
		lookup_bi_gram = ref.read()
		lookup_bi_gram_dict = ast.literal_eval(lookup_bi_gram)

	total_real_word_error_predicted=0
	total_correct_bi_grams_predicted=0
	total_correct_suggested=0

	for j in range(len(sentences)):
		errors,correct_bigrams=check_for_real_word_errors(sentences[j],lookup_bi_gram_dict)
		# add the correct bigrams for a particular error
		total_correct_bi_grams_predicted+=correct_bigrams
		for error in errors:
			#if the bigram is in the reference real word errors list
			if(error[0] in real_word_errors):
				total_real_word_error_predicted+=1

		for i in range(len(errors)):
			candidate_grams = generate_candidate_grams(errors[i][0],lookup_bi_gram_dict)
			for word, candidates in candidate_grams.items():
				for candidate in candidates:
					#if the bigram is in the correct suggestion reference list
					if(candidate in correct_suggestions):
						total_correct_suggested+=1

	print("model_accuracy: ",(total_real_word_error_predicted+total_correct_bi_grams_predicted)/total_bigrams)
	print("correct bi-gram suggestion accuracy", total_correct_suggested/total_correct_suggestions)

# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

SUYASH MANDHANA

Exercises with sed:
```
1. sed 's/[^a-zA-Z]\+/\n/g' wiki.txt | sed 's/[aeiouAEIOU].*//g' | sort | uniq -c | sort -nr > initial-consonants.hist

2. sed 's/[^a-zA-Z]\+/\n/g' wiki.txt| sed 's/.*[aeiouAEIOU]//g' | sort  | uniq -c | sort -nr > final-consonants.hist
```

SEGMENTER REPORT:

brief description:

This is the segmenter which I have written myself and it is written in python language. It does not use any regular expression, instead it is based on detecting the end of a line using 
if else statements. It reads the file and traverse it line by line. It is not using any libraries or machine learning as well.

quantitative evalutaion:

It was able to detect 25 lines out of 26 correctly that is around 86.5% of the lines.

qualitative evaluation:

The segmenter which I wrote was according to the language english and so it was breaking for language slots because it has different abbreviations like it counted or 
segmented "cf." as well because it was able to see a full stop. 
There were more empty number of lines between the segmented lines.

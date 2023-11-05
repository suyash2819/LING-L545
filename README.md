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

TOKENIZATION REPORT:

  execution of maxmath.py - 

  We need to pass the dictionary file as an argument and take input of the sentence from stdin, the 1st line is the stdin and the 2nd line is the result that we received from the 
  maxmatch algorithm.
  
  ![image](https://github.com/suyash2819/LING-L545/assets/28905722/98fd5b76-e298-4ef6-be38-a81267b8e9c7)

   To check the performance, word error rate is calculated by passing the hypothesis and reference files, hypothesis file is generated from the maxmatch.py code and reference file has 
   the original sentence with space as token separator. The WER comes out to be 30.30% for the 1st sentence.

  WER from reference and hypthesis:
 
  ![image](https://github.com/suyash2819/LING-L545/assets/28905722/0414756f-6354-4b65-9c73-49adf88da701)

DEPENDENCY GRAMMAR AND PARSING

Finish:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/50e4d933-48da-4362-aa97-c9606cee4654)

Galician:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/62ed27f0-132f-444f-afbe-97d48fdc8451)

Hungarian:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/7dc34f7c-74aa-45b9-b9ca-81282c562018)

Irish:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/aaf03bf8-3866-40aa-99cf-3221e4b5e716)

Kazakh:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/70c85900-a5bf-4fec-9efd-e2b0779bb481)

Serbian:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/591d5ae4-cf75-4a1e-a399-091e6b8de44c)

Maltese:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/671c7bdf-c202-4bf2-92b1-805449f16fc4)

Buryat:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/837f10e5-8297-4094-873f-c825741329e3)

Afrikaans:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/8e041f41-8f52-4d70-b56f-0dc40fece0ec)


Ancient Hebrew:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/ce44a25a-fd09-4cb9-9e0e-8e3ffc2bce45)


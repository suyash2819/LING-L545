English Language evaluation:

![image](https://github.com/suyash2819/LING-L545/assets/28905722/1335a26b-7145-4d75-bbda-793769a710a4)


Inspecting 10 trees for errors:

1. text = what are the coach flights between dallas and baltimore leaving august tenth and returning august twelve

   Error in this is, although August is Noun which is masked the same but its actually a proper noun which is not marked in this.

   11	august	August	NOUN	_	Number=Sing	10	obl	_	_

2. i want a flight from nashville to seattle that arrives no later than 3 pm

   Everything seems fine in this sentence.

3. show me ground transportation in philadelphia on monday morning

   Everything seems fine in this sentence.

4.  what does the meal code s stand for

      Here S is tagged as proper noun but it os not a proper noun, it is just a noun.

      6	s	S	PROPN	_	Number=Sing	5	nmod	_	_

5. what meals are available on dl 468 which al arrives in san francisco at 950 am

   Everything seems fine in this sentence.

6. list flights between boston and san francisco that serve breakfast

   here San Francisco is one word although its broken down into two but the tags are correct as proper noun.

     6	san	San	PROPN	_	Number=Sing	4	conj	_	_
     7	francisco	Francisco	PROPN	_	Number=Sing	6	flat	_	_

7.  what is the fare going from baltimore to atlanta one way on november seventh

      Everything seems fine in this sentence.

8. flight from milwaukee to denver

      Everything seems fine in this sentence.

9. please find a flight from kansas city to newark

     Here Please is tagged as interjection but it seems to be Adverb.

     1	please	please	INTJ	_	_	2	discourse	_	_

10. only show continental flights

     Everything Seems fine in this sentence.

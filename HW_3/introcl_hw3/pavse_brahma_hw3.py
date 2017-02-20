import re;
import nltk;
from nltk.corpus import brown;

########
# Your name and EID: Brahma S. Pavse, bsp686

#########
# Problem 1:

def problem_1():
	mystring = "-.12";

	# (characers \. or \d etc)? - makes things inside optional
	res = re.match("(\-)?\d+((\.\d+)|$)", mystring);
	print (res);
# problem_1();

#########
# Problem 2:

def problem_2():
	mystring = "oeia";
	res = re.findall("[aeiouAEIOU]", mystring);
	# print (len(res));
# problem_2();


#########
# Problem 3:

def problem_3():

	patterns = [
		# My new additions
		(r'.*ish$', 'JJ'),					# 1. Childish - adjective
		(r'.*er$', 'NN'),					# 2. Seller - noun
		(r'.*able$', 'JJ'),					# 3. personable - adjective
		(r'.*ize$', 'VERB'),				# 4. digitalize - verb
		(r'.*less$', 'JJ'),					# 5. useless - adjective
		(r'.*ful$', 'JJ'),					# 6. forgetful - noun
		(r'.*ly$', 'RB'),					# 7. slowly - adverb
		(r'.*ness$', 'NN'),					# 8. completeness - noun
		(r'.*ment$', 'NN'),					# 9. placement - noun
		(r'.*ion$', 'NN'),					# 10. mission - noun

		(r'.*ing$', 'VBG'),               	# gerunds
		(r'.*ed$', 'VBD'),                	# simple past
		(r'.*es$', 'VBZ'),                	# 3rd singular present
		(r'.*ould$', 'MD'),               	# modals
		(r'.*\'s$', 'NN$'),               	# possessive nouns
		(r'.*s$', 'NNS'),                 	# plural nouns
		(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  	# cardinal numbers
		(r'.*', 'NN'),    				  	# nouns (default)
	];

	regexp_tagger = nltk.RegexpTagger(patterns)
	brown_sents = brown.sents(categories='news');
	regexp_tagger.tag(brown_sents[3])
	brown_tagged_sents = brown.tagged_sents(categories='news')
	res = regexp_tagger.evaluate(brown_tagged_sents)
	# print(res);
# problem_3();


#########
# Problem 4:

# a:
'''
1. A case where it may be useful is when another part of speech tagging 
algorithm incorrectly identifies a word because it may be more tailored towards
specific type of words . For the most part based on emperical
data, it might be helpful to tag a word as the most frequent result. Such
as labeling it as a Noun.

2. Another case in relation to the functioning of the algorithm is if 
an advanced algorithm has never seen the word. Mainly because Nouns
are always getting created. It is better to assume that the new word
encountered is a noun.

3. It is a great way to begin some form of an algorithm. Rather than
having no clue about POS, it is better to give a guess of what it may be
and adjust your hypothesis accordingly.

Here, just based on frequency and most common observations we can assign a
word as a noun because that seems to be the most frequent result.

Our hope is that with this simple algorithm, we cover a reasonable percentage
of correctness.

Depending on the data this might work out to be perfect. But on average
it will do poorly.

'''

# b:
'''
I think the lookup tagger algorithm of looking at the most common/frequent
words and labelling input data works because most of the frequent words
are words that are necessary to form coherent english sentences.

In other words, in our most 100 words would not get necessarily get words
like anticlimactic, kernel etc. In part these words dont help in forming
structure to english so they dont necessarily appear again. But the 100 
common words would include things like "the", "a", "of" and "and" which
are definitely used in forming sentences to have meaningful english. On most
corpus data it will do at about 50% for the same reason that these words
are inherent in coherent text

- - - 

The tagger is not using a machine learning model to predict tagging 
based on given data. So if we do not include certain words they will
not be tagged. For this reason we can go from 100 most common to 1000, but
we are still leaving out some words that will not come under this new threshold.
Hence, you will not get a success rate of 100% unless you include every single
word in your model.

- - -

The reason we an asymtope structure in the log function is because in the 
beginning there are many common words. They fall under most 100 common words
and they are indeed common hence there is a high success rate initially.
Similar this works as we increase the size of common words we are looking at, but
we reach a dimishing return eventually. For example, while we might be
looking at the top 10000 words, it does not mean that words ranked from
5000-10000 will even show up even though fall under top 10000 words. They
may fall under the category of most frequent but in practice they do not 
appear. Hence there is high rate of change in the beginning and over time
the growth slows down.

'''
# c: 

'''
Which number you should trust depends completely on the purpose of the
tagging. If you are building a tagger to analyze news data segments then
you should go with the 93% because the tagger is working successfully
in the domain of words that you are targeting.

If youre aiming at fiction stories and analyzing those words, it is 
important to consider the deficiency of the tagger and work on improving
it. In this case it is irrelevant if the tagger works for news data
because that is not what your project is based on.

To summarize, it completely depends on the situation. There is only one
right answer depending on the problem you are solving.

'''

#########
# Problem 5:
'''
Total words tagged = 10
Total words correctly tagged = 6
(They, refuse, us, obtain, the, permit)

Accuracy = 6 / 10 = 60%

'''
#########
# Problem 6:

'''
I chose (C) because while the probablity of green cars is high, the witness
has a high success rate of identify cars. So the probablities were
not favoring any particular circumstance. More or less, they would
be around the same given that the evidence was favoring blue.

Need to find

P(B/WB) and P(G/WB)

Given in the question, P(G) = 0.85
P(B) = 0.15
Based on the information, the witness guesses correctly 80%.

So P(Witness pointing out Blue given it was correctly Blue) = 0.8
P(WB / B) = 0.8

By Bayes' rule

P(B/WB) = (P(WB/B) P(B)) / (P(WB/B) * P(B) + P(WB/G) * P(G))

= (0.8 * 0.15) / (0.8 * 0.15 + 0.2 * 0.85)
= 0.41379
'''



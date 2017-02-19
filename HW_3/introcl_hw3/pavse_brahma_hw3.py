import re;
import nltk;
from nltk.corpus import brown;

########
# Your name and EID: Brahma S. Pavse, bsp686

#########
# Problem 1:

def problem_1():
	mystring = "-5.";

	# (characers \. or \d etc)? - makes things inside optional
	res = re.match("(\-)?\d+((\.\d+)|$)", mystring);
problem_1();

#########
# Problem 2:

def problem_2():
	mystring = "onomatopoeia";

	res = re.findall("[aeiouAEIOU]", mystring);
problem_2();


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
	print(res);
problem_3();


#########
# Problem 4:

# a:

# b:

# c: 

#########
# Problem 5:

#########
# Problem 6:

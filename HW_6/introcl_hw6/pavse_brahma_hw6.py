import nltk
import random
import math
import operator
import string

#### Homework 5
# Name: Brahma S. Pavse
# EID: bsp686

#########
# Problem 1:

'''
Trigram model of 
P(<s> My iguana is on fire </s>)
	= P(My|<s>) * P(iguana|<s>, My) * P(is|My, iguana) * P(on|iguana, is) *
		P(fire|is, on) * P(</s>|on, fire) 

'''

#########
# Problem 2:

'''
P(fire|is, on) = count (is, on, fire) / count (is, on)
'''

#########
# Problem 3:

'''
(1) matches with (A) because

We are talking about the first sentence heard. The situation does describe
or hint that "Do" is the first word heard, so the probablility cannot assume
that it is the first thing heard.

Similarly, the situation doesnt describe that think was the last thing heard,
hence the probability doesnt include a sentence ending.


(2) matches with B because 
The situation describes the first three words heard, so we know that "Do" was
the first word heard. Hence the probability should include the fact it was the
starting word.

Compared (3), (2) hints that the sentence ends. Hence need to include the 
end of sentence in the probability

(3) matches with C because
The situation describes the first sentence heard is "Do you think", hence 
we need to include the start of the sentence in the probability. But the 
situation specifies that it starts with these words and nothing about the 
end.

So we cannot assume that this is the end of the sentence and hence we do 
not include it in the proabability.

'''

#########
# Problem 4:
''' Taken from file specified in hw '''

def problem_4(corpus):

	count = {}
	my_probs = {};

	# corpus = """
	# <s> I am Sam </s>
	# <s> Sam I am </s>
	# <s> I do not like green eggs and ham </s>
	# """

	words = corpus.split()

	# nltk.bigrams(words) yields a list of pairs, [('<s>', 'I'), ('I', 'am'), ...]
	# I could iterate over them by saying 'for pair in nltk.bigrams(words):...'
	# Or I can use assignment to multiple variables at once, as I do below.
	# Remember: I can say
	# word1, word2 = ('I', 'am')
	# and that will assign 'I' to word1 and 'am' to word2.
	# I am just doing this in a for-loop.


	for word1, word2 in nltk.bigrams(words):
	    if word1 not in count:
	        count[word1] = { }

	    if word2 not in count[word1]:
	        count[word1][word2] = 1
	    else:
	        count[word1][word2] += 1

	# This printout just demonstrates
	# that the code does the right thing
	# for word1 in count:
	# 	for word2 in count[word1]:
	# 		print(word1, word2, count[word1][word2])

	# print(" ");
	'''

	P(I | <s>) = count(<s>, I) / count(<s>, --- )

	'''
	# Go through all word1 in count
	for word1 in count:

		total_count = 0;

		# keep track of all counts for denominator
		for word2 in count[word1]:
			total_count += count[word1][word2];

		if word1 not in my_probs:
			my_probs[word1] = {};

		# for each, numerator/denominator.
		# numerator is the count for a specific pair (word1, word2)
		for word2 in count[word1]:
			pair_count = count[word1][word2];
			my_probs[word1][word2] = pair_count * 1.0 / total_count;

	# print(" ");
	#prob = {'green': {'eggs': 1.0}, 'and': {'ham': 1.0}, 'am': {'Sam': 0.5, '</s>': 0.5}, 'like': {'green': 1.0}, 'eggs': {'and': 1.0}, 'Sam': {'I': 0.5, '</s>': 0.5}, 'not': {'like': 1.0}, 'ham': {'</s>': 1.0}, 'do': {'not': 1.0}, '<s>': {'Sam': 0.3333333333333333, 'I': 0.6666666666666666}, 'I': {'am': 0.6666666666666666, 'do': 0.3333333333333333}, '</s>': {'<s>': 1.0}}
	

	# If true, matches the map provided in the hw by instructor
	#print ("Found matches: " + str(my_probs == prob))

	return my_probs

	# for word1 in probs:
	# 	for word2 in probs[word1]:
	# 		print(word1, word2, probs[word1][word2])

# problem_4();


#########
# Problem 5a:

def problem_5a(prob):

	
	# prob = {'<s>': {'one': 0.4, 'mice': 0.2, 'something': 0.2, 'else': 0.2}};
	START_WORD = "<s>"

	word = START_WORD;
	print(word);
	for x in range (1, 51):
		p = random.random();

		# probs[word] gives dictionary with corresponding words and the
		# probability of the combinations

		# Want to pick word that has closest probability to the p

		# then print  word corresponding to that probability 
		# and repeat process 50 times	

		# Put probs[word] in ascending order of probabilities
		# searc through this until first value that p is greater than and
		# break


		word_counter_sorted = sorted(prob[word].items(), key = operator.itemgetter(1), reverse = True);
		temp_prob = dict(word_counter_sorted);
		max_word = word_counter_sorted[0][0];
		max_prob = word_counter_sorted[0][1];
		change = max_prob;

		# Forming box similar to that in handout
		# if probs are 0.4, 0.2, 0.2, 0.2
		# then arranged as
		# 0 to 0.4, to 0.6 to 0.8 to 1
		# then search in ascending order for somrthing just greater than p
		# that is the answer
		for other_words in word_counter_sorted:

			if other_words[0] != max_word:
				temp_prob[other_words[0]] += change;
				change = temp_prob[other_words[0]] ;

		word_counter_sorted = sorted(temp_prob.items(), key = operator.itemgetter(1), reverse = False);

		for possible_word in word_counter_sorted:
			#print (possible_word);
			#print (p);
			if p <= possible_word[1]:
				word = possible_word[0];
				break;
		print(word);

# problem_5a();


###########
# Problem 5b:

def problem_5b():

	file = open("alicecorpus.txt");

	alice_string = file.read();

	punc = set(string.punctuation)

	alice_tok_temp = alice_string.split();
	alice_tok = [];

	# option to remove punctuations
	for ele in alice_tok_temp:
		if ele not in punc:
			alice_tok.append(ele);

	# converting back to a string
	# comment out below line to allow stripping of punc
	#alice_string = ' '.join(alice_tok)

	# Passing in result from problem 4 to solve random word problem
	prob_dict = problem_4(alice_string)
	problem_5a(prob_dict);

# problem_5b();


def main():

	problem_4_corpus = """
	<s> I am Sam </s>
	<s> Sam I am </s>
	<s> I do not like green eggs and ham </s>
	"""

	#print("Solving problem 4 and 5a at once");
	problem_5a(problem_4(problem_4_corpus));

	#print("Solving problem 5b");
	problem_5b();

#main();








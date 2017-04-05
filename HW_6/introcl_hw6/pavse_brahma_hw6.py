import nltk
import random
import math
import operator
import string

#### Homework 6
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
A matches with (2)

Both match because the situation described refers to just hearing
certain sequence of words. Does not describe a situation that the
sequence is the starting or ending sentence. Hence no, <s> and </s>
Words could have existed before and after it.

B matches with (1)
The situation describes that the sequence of words heard is a complete
sentence. Given that this is true, it should have starting and
ending tags. Hence inclusion of <s> and </s>

C matches with (3)
The situation described says the sentence is the starting sentence.
Hence the use of <s>, but it also says it starts with that sentence
with no mention of the end. Hence the exclusion of </s>. The 
sentence may still be in the process of going on.

'''

#########
# Problem 4:
''' Taken from file specified in hw '''

def problem_4(corpus):

	count = {}
	my_probs = {};

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

	'''
	P(I | <s>) = count(<s>, I) / count(<s>, --- )
	'''
	# Go through all word1 in count
	for word1 in count:

		total_count = 0;

		# keep track of all counts for denominator
		# Calculating count(word1, --)
		for word2 in count[word1]:
			total_count += count[word1][word2];

		if word1 not in my_probs:
			my_probs[word1] = {};

		# for each, numerator/denominator.
		# numerator is the count for a specific pair (word1, word2)
		for word2 in count[word1]:
			pair_count = count[word1][word2];
			my_probs[word1][word2] = pair_count * 1.0 / total_count;

	# Returns prob map of count(word1, word2)/count(word1, -) corresponding to its chance
	# of occuring based on MLE and corpus provided
	return my_probs


#########
# Problem 5a:

def problem_5a(prob):
	
	START_WORD = "<s>"
	word = START_WORD;
	print(word);
	for x in range (1, 51):
		p = random.random();

		# Get sorted order of probabilities from word1 to ---
		word_counter_sorted = sorted(prob[word].items(), key = operator.itemgetter(1), reverse = True);
		temp_prob = dict(word_counter_sorted);

		# max_word corresponds to word2 such that [word1][word2] is max
		max_word = word_counter_sorted[0][0];
		# gets the max value prob - [word1][word2]
		max_prob = word_counter_sorted[0][1];
		change = max_prob;

		# Forming box similar to that in handout
		# if probs are 0.4, 0.2, 0.2, 0.2
		# then arranged as
		# 0 to 0.4, to 0.6 to 0.8 to 1
		# then search in ascending order for somrthing just greater than p
		# that is the answer
		for other_words in word_counter_sorted:

			# Skipping over first word, could have also made change = 0 if I did not want to skip it.
			if other_words[0] != max_word:
				
				# With respect to the example, 0.4 remains the same, 0.2 becomes 0.6, 0.2 because 0.8 and 0.8 becomes 1.0
				# Hence intervals of (0.4, 0.6, 0.8, 1.0) - similar to the box in the handout.
				temp_prob[other_words[0]] += change;
				change = temp_prob[other_words[0]];

		# sort this new dictionary just be safe.
		word_counter_sorted = sorted(temp_prob.items(), key = operator.itemgetter(1), reverse = False);

		# Placed in ascending order, hence will guarantee that word is 
		# chosen based on dart simulation
		# break immediately once lowest condition is satisfied 
		# otherwise all conditions hold true if allowed to proceed

		# If prob is 0.7,
		# Then 0.7 is not less than 0.4
		# 0.7 is not less than 0.6,
		# 0.7 is less than 0.8.
		# So 0.7 corresponds to the 3rd category as described in the handout.
		# Break immedaiately after finding the word match
		for possible_word in word_counter_sorted:
			if p <= possible_word[1]:
				word = possible_word[0]; # reassign the word, to base next iteration on
				break;
		print(word);

###########
# Problem 5b:

def problem_5b():

	file = open("alicecorpus.txt");

	alice_string = file.read();
	punc = set(string.punctuation);

	remove_punc = False;

	alice_tok_temp = alice_string.split();
	alice_tok = [];

	if remove_punc:
		# option to remove punctuations
		for ele in alice_tok_temp:
			if ele not in punc:
				alice_tok.append(ele);

		# converting back to a string
		# comment out below line to allow stripping of punc
		alice_string = ' '.join(alice_tok)

	# Passing in result from problem 4 to solve random word problem
	prob_dict = problem_4(alice_string)
	problem_5a(prob_dict);

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








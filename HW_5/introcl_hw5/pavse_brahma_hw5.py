
# Name and EID: Brahma S. Pavse, bsp686

import nltk;
import operator;

# Get data from brown_news
brown_news = nltk.corpus.brown.tagged_words(categories = "news");
#########
# Problem 1:
def problem_1():


	word_counter = {};
	pos_counter = {};

	for word_pos in brown_news:

		# Extract relevant word and its POS tagging
		word = word_pos[0].lower();
		pos = word_pos[1];

		# If found increment it else, set count = 1
		if word in word_counter:
			word_counter[word] += 1;
		else:
			word_counter[word] = 1;

		if pos in pos_counter:
			pos_counter[pos] += 1;
		else:
			pos_counter[pos] = 1;


	# Sort in reverse order
	word_counter_sorted = sorted(word_counter.items(), key = operator.itemgetter(1), reverse = True);

	pos_counter_sorted = sorted(pos_counter.items(), key = operator.itemgetter(1), reverse = True);

	print("Most frequent word: " + word_counter_sorted[0][0]);
	print("Most frequent pos: " + pos_counter_sorted[0][0]);

#problem_1();


def problem_2():

	word_to_pos = {};

	for word_pos in brown_news:

		word = word_pos[0].lower();
		pos = word_pos[1];

		# Adding POS to list
		if word in word_to_pos:
			word_to_pos[word].add(pos);
		else:
			# Set to get all unique POS
			word_to_pos[word] = set([pos]);

	problem_2a(word_to_pos);
	return problem_2b(word_to_pos);

#########
# Problem 2a:
def problem_2a(word_to_pos):

	counter = 0;
	for word in word_to_pos:
		if len(word_to_pos[word]) >= 2:
			counter += 1;

	print("Words with more than 2 distinct POS: " + str(counter));

#########
# Problem 2b:

def problem_2b(word_to_pos):

	max_pos = -1;
	max_word_to_pos = {};

	for word in word_to_pos:
		if len(word_to_pos[word]) >= max_pos:
			max_pos = len(word_to_pos[word]);

	for word in word_to_pos:
		if len(word_to_pos[word]) == max_pos:
			max_word_to_pos[word] = word_to_pos[word];

	print("Words with maximum distinct POS tagging " + str(max_word_to_pos));

	return max_word_to_pos;

#########
# Problem 3:

def problem_3(max_word_to_pos):

	brown_sents = nltk.corpus.brown.tagged_sents(categories = "news")

	sents = [];

	# Go through the words with max disinct POS tagging
	for word in max_word_to_pos:

		# To check if we have encountered a POS  before
		pos_list = max_word_to_pos[word]

		for pos in pos_list:
			word_pos_pair = (word, pos);
			pos_tracked = []; # List of pos that we have seen before

			# For each sentence find the the pairs with this mapping and break
			for sent in brown_sents:
				for pair in sent:
					word_in_sent = pair[0].lower();
					pos_in_sent = pair[1];

					# If the pairs match and we have not tried looking for this pos before
					if word_pos_pair[0] == word_in_sent and word_pos_pair[1] == pos_in_sent and word_pos_pair[1] not in pos_tracked: # If the pair is in a sentence.
						sents.append(sent);
						pos_tracked.append(word_pos_pair[1]);
						break; # Look at another sentence

	print("Sentences for words with distinct POS tagging: ");
	for s in sents:
		print(s);

	print ("Total sentences: (of all the words with max distinct POS taggings): " + str(len(sents)));


def main():
	problem_1();
	max_word_to_pos = problem_2();
	problem_3(max_word_to_pos);

#main();






# Name and EID: Brahma S. Pavse, bsp686

import nltk;
import operator;

brown_news = nltk.corpus.brown.tagged_words(categories = "news");
#########
# Problem 1:
def problem_1():


	word_counter = {};
	pos_counter = {};

	for word_pos in brown_news:

		word = word_pos[0].lower();
		pos = word_pos[1];

		if word in word_counter:
			word_counter[word] += 1;
		else:
			word_counter[word] = 1;

		if pos in pos_counter:
			pos_counter[pos] += 1;
		else:
			pos_counter[pos] = 1;


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

		# Adding to list
		if word in word_to_pos:
			word_to_pos[word].add(pos);
		else:
			word_to_pos[word] = set([pos]);

	problem_2a(word_to_pos);
	problem_2b(word_to_pos);

#########
# Problem 2a:
def problem_2a(word_to_pos):

	counter = 0;
	for word in word_to_pos:
		if len(word_to_pos[word]) >= 2:
			counter += 1;

	print(counter);

#########
# Problem 2b:

def problem_2b(word_to_pos):

	max_pos = -1;
	max_list = [];

	for word in word_to_pos:
		if len(word_to_pos[word]) >= max_pos:
			max_pos = len(word_to_pos[word]);

	for word in word_to_pos:
		if len(word_to_pos[word]) == max_pos:
			max_list.append(word);

	print(str(max_list));

problem_2();

#########
# Problem 3:







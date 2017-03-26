
# Name and EID: Brahma S. Pavse, bsp686

import nltk;
import operator;
#########
# Problem 1:

def problem_1():
	brown_news = nltk.corpus.brown.tagged_words(categories = "news");

	word_counter = {};
	pos_counter = {};

	for word_pos in brown_news:

		word = word_pos[0];
		pos = word_pos[1];

		if word in word_counter:
			word_counter[word] += 1;
		else:
			word_counter[word] = 0;

		if pos in pos_counter:
			pos_counter[pos] += 1;
		else:
			pos_counter[pos] = 0;


	word_counter_sorted = sorted(word_counter.items(), key = operator.itemgetter(1), reverse = True);

	pos_counter_sorted = sorted(pos_counter.items(), key = operator.itemgetter(1), reverse = True);

	print("Most frequent word: " + word_counter_sorted[0][0]);
	print("Most frequent pos: " + pos_counter_sorted[0][0]);

problem_1();




#########
# Problem 2a:

#########
# Problem 2b:


#########
# Problem 3:





########
# Your name and EID: Brahma S. Pavse, bsp686

#########
# Problem 1:

# Attached in pdf file (uploaded to canvas)


#########
# Problem 2:
'''
a) this_is_a_variable - Valid
b) mylist123 - Valid
c) my-string - Invalid
	- Using substraction operator in between
d) 123list - Invalid
	- Cannot start with a number
e) def - Invalid
	- reserved key word for defining function
f) sum - Valid
g) VAR - Valid
h) my string - Invalid
	- space in between
i) another_variable - Valid
j) var_1005 - Valid


Extra credit:
The variable "String" or "sting" is a valid variable name. But it is not a good
idea to use it because it can be very confusing for those coming
from Java where a String is an array of characters. 

In python you could name 
string = 5
And the above statement would be correct but confusing


''' 

#########
# Problem 3:

import string

def problem_3():
		# for my system: file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/wells.txt");
        file = open("wells.txt"); # same directory
        content = file.read();
        words = content.split();
        puncs_to_remove = string.punctuation;
        # print(words); # old words
        for i, word in enumerate(words):
                words[i] = word.strip(puncs_to_remove);
        # print("\n");
        # print(words); # edited words
        file.close();
problem_3();


#########
# Problem 4:

# Total 10 words of that specification

def problem_4():
        # for my system: file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/wells.txt");
        file = open("wells.txt"); # same directory
        content = file.read();
        words = content.split();
        puncs_to_remove = string.punctuation;
        # print(words);
        for i, word in enumerate(words):
                words[i] = word.strip(puncs_to_remove);
        # print("\n");
        # print(words);

        counter = 0;
        for word in words:
                if word.endswith("ing"):
                        counter = counter + 1;
        # print("words ending with ing is: ", counter)
        file.close();
problem_4();



#########
# Problem 5:

def problem_5():
        # for my system: file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/wells.txt");
        file = open("wells.txt"); # same directory
        content = file.read();
        words = content.split();
        puncs_to_remove = string.punctuation;
        # print(words);
        for i, word in enumerate(words):
                words[i] = word.strip(puncs_to_remove);
        # print("\n");
        # print(words);

        for i, word in enumerate(words):
                if word.endswith("s"):
                        words[i] = word[:-1];
                elif word.endswith("ed"):
                        words[i] = word[:-2];
                elif word.endswith("ing"):
                        words[i] = word[:-3];
        final_text = " ".join(words);
        # print(final_text);
        file.close();
problem_5();


#########
# Problem 6:

# Had to add 60 to skip over the entire part of the string that started with 
# ***START. Can ignore ***END because it excluded in the range

def problem_6():
		# for my system: file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/pg768.txt");
        file = open("pg768.txt"); # same directory
        content = file.read();
        start_index = content.index("***START");
        end_index = content.index("***END");
        actual_content = content[start_index + 60: end_index];
        # print(actual_content);
        file.close();
problem_6();
import string

def main():
	file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/wells.txt");
	content = file.read();
	words = content.split();
	puncs_to_remove = string.punctuation;
	print(words);
	for i, word in enumerate(words):
		words[i] = word.strip(puncs_to_remove);
	print("\n");
	print(words);
main();

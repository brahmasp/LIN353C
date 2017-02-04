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
	
	for i, word in enumerate(words):
		if word.endswith("s"):
			words[i] = word[:-1]; 
		elif word.endswith("ed"):
			words[i] = word[:-2];
		elif word.endswith("ing"):
			words[i] = word[:-3];
	final_text = " ".join(words);
	print(final_text);
main();

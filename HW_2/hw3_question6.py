import string

def main():
	file = open("/Users/BrahmaSPavse/Desktop/introcl_hw2/pg768.txt");
	content = file.read();
	start_index = content.index("***START");
	end_index = content.index("***END");
	actual_content = content[start_index + 60: end_index];
	print(actual_content);
	file.close();
main();

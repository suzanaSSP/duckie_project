import nltk
from nltk.tokenize import sent_tokenize

# Read txt file that includes textbook
file = open("call_expressions.txt", "r")
#Open file
contents = file.read()
# Close file
file.close()

# Tokenize the text into sentences
sentences = sent_tokenize(contents)
for sentence in sentences:
    print(sentence)
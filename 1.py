import nltk
# nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

text = "Hello world! This is working now."
print(sent_tokenize(text))

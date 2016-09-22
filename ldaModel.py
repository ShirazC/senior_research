import sys, os
from nltk import *
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

sys.path.append('/Users/shirazchokshi')

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# import all wikipedia documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 

#compile sample documents into an array to analyze later
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# array for all the documents that were tokenized in the loop
texts = []

# loop through the entire document list
for i in doc_set:
	
	#clean and tokenize all the document strings
	raw = i.lower()
	tokens = tokenize.tokenize(raw)
	
	# remove stop words from tokens
	stopped_tokens = [i for i in tokens if not i in en_stop]

	#stem tokens
	stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

	# add tokens to the list
	texts.append(stemmed_tokens)

#turn each tokenized documents into a id <-> term dictionary 
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus  = [dictionary.doc2bow(tex) for text in texts]  

# generate the LDA model

ldamodel = gensim.models.ldmodel.LdaModel(corpus, numtopics=2, id2word = dictionary, passes=20)
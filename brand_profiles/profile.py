import nltk
nltk.data.path.append('../nltk_data')
import csv, pdb
from nltk import FreqDist, bigrams
from nltk.corpus import stopwords, brown
from nltk.collocations import *
from nltk.tag.util import str2tuple
from nltk.tree import Tree
import re
from textblob import TextBlob

class Profile(object):
	"""docstring for Profile"""
	def __init__(self, data):
		try:
			print "Initializing Profile class"
			super(Profile, self).__init__()
			self.params = data
			
			if data['text']:
				self.input_text = data['text']
			else:
				self.input_text = "This is a sample"
			
			print "Set the input text"
			print "input:-", self.input_text[:50]
			
			self.stopwords_list = stopwords.words('english')
			print "stopwords:-", self.stopwords_list[:20]
		except Exception, e:
			print e
		

		
	def build_content(self):
		try:
			print "Building content"
			print self.input_text[:50]
			words = nltk.word_tokenize(self.input_text)
			print "words", words[:20]
			text = nltk.Text(words)
			print "Built a text"
			content = [w for w in text if w.lower() not in self.stopwords_list]
			content = nltk.Text(content)
			return content
		except Exception, e:
			print e

	def pos_tagging(self, frequent_words):
		try:
			content = self.build_content()
			# frequent_words = self.frequent_words()

			print "============Content============", "\n"
			print content[:50]

			text_tagged = nltk.pos_tag(content[:2000])  
			print "Tagged content"   
			nouns = [word for (word, tag) in text_tagged if tag.startswith('NN')]
			nouns = set(nouns)
			print "nouns", len(nouns)
			print "Found nouns"
			verbs = [word for (word, tag) in text_tagged if tag.startswith('VB')]
			verbs = set(verbs)
			print "Found verbs"
			adjectives = [word for (word, tag) in text_tagged if tag.startswith('JJ')]
			adjectives = set(adjectives)
			print "Found adjectives"
			
			print "Returning POS tags"
			return {'nouns':list(nouns), 'adjectives':list(adjectives), 'verbs':list(verbs)}
		except Exception, e:
			print e

	def sentiment_preprocessing(self, given_text=None):
		try:
			print "In sentiment analysis"
			if given_text == None:
				reviews = re.split(r'\n', self.input_text)
			else:
				reviews = re.split(r'\n', given_text)

			print "Split text"
			reviews = [val for val in reviews if val != '']
			print "Created reviews list"
			reviews_cleaned = []

			for review in reviews:
				review = re.sub(r'[\d\t]', '', review)
				reviews_cleaned.append(review)

			print "Cleaned reviews"
			print len(reviews_cleaned)
			return reviews_cleaned
		except Exception, e:
			print e

	def return_sentiment_count(self):
		try:
			sentiment_dict = {'positive':0, 'negative':0}
			counter = 1
			
			positive_reviews=[]
			negative_reviews=[]

			reviews_cleaned = self.sentiment_preprocessing()

			for review in reviews_cleaned:
				review_t = TextBlob(review)
				try:
					# print counter, "=", review_t.sentiment.polarity
					if review_t.sentiment.polarity > 0:
						sentiment_dict['positive'] += 1	
						positive_reviews.append(review_t)				
					elif review_t.sentiment.polarity < 0:
						sentiment_dict['negative'] += 1	
						negative_reviews.append(review_t)				
				except UnicodeDecodeError:
					print "Unicode Decode Error" 
				counter += 1

			print "Analysed the sentiments"
			print sentiment_dict 
			return sentiment_dict 
		except Exception, e:
			print e

	def create_sentiment_analysis_file(self):
		try:
			csv_file = csv.writer(open('newcorpus/Haw_Par_Villa_sentiments.csv', 'w'), delimiter=',')
			csv_file.writerow(['Sentiment', 'Review'])
			given_text = open('newcorpus/Haw_Par_Villa.txt', 'r').read()

			reviews_cleaned = self.sentiment_preprocessing(given_text)
			# pdb.set_trace()
			print "Starting sentiment analysis"
			for review in reviews_cleaned:
				review_t = TextBlob(review)
				try:
					# print counter, "=", review_t.sentiment.polarity
					if review_t.sentiment.polarity > 0:
						csv_file.writerow(['positive', review])
					elif review_t.sentiment.polarity < 0:
						csv_file.writerow(['positive', review])
				except UnicodeDecodeError:
					print "Unicode Decode Error" 
		except Exception, e:
			print e
		
	def frequent_words(self):
		try:
			content = self.build_content()
			print "Removed stopwords"
			fdist=FreqDist(content)
			frequent_words = [w for w in set(content) if len(w)>3 and fdist[w]>2]
			print "Found frequent words"
			
			freq_words = []
			for w in frequent_words:
				word = (w, fdist[w])
				freq_words.append(word)

			print "Returning frequent words"
			return freq_words
		except Exception, e:
			print e

	def analysis(self):
		try:
			print "In analysis"

			print "Getting frequent words"
			frequent_words = self.frequent_words()

			print "Getting POS tags"
			pos_tags = self.pos_tagging(frequent_words)
			
			sentiments = self.return_sentiment_count()
			print sentiments
			print "Got sentiments"

			return {'freq_words':frequent_words, 'pos_tags':pos_tags, 'sentiments':sentiments}
		except Exception, e:
			print e

	def helper(self):
		# analysis = self.analysis()
		analysis = self.create_sentiment_analysis_file()
		# return analysis
		

# f = open('newcorpus/Bugis_Street', 'r')
# in_dict = {'text':f.read()}
# obj = Profile(in_dict)
# obj.helper()
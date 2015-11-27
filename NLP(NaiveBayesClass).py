'''
Project By: Pritish Yuvraj
Project Name: NLP classifier using Naive Bayes Classification
Accuracy : 83.143%

URL of sample data: https://drive.google.com/folderview?id=0BwXeiCjEpkS8cFJLRXBiWFllbjg&usp=sharing
File: 	"training.json" contains training data in JSON format for training our classifier
	"inputs.json" contains data to be tested again in JSON format
	"correct_output.txt" contains actual answers to the input file earlier mentioned
	"output.txt" contains the output by our pogram

Highlights: This NLP is capable of distinguishing text from multiple fields
'''	
import re
import math
import json
import sys

def getwords(doc):
	#splitter = re.compile('\\W*', re.DEBUG)
	splitter = re.compile('\\W*')
	#Split the words by non-alpha characters
	words = [s.lower() for s in splitter.split(doc)
		if len(s)>2 and len(s)<20]
	
	#Return the unique set of words only
	return dict([(w,1) for w in words])
class classifier:

	def __init__(self, getfeatures, filename=None):
	#Counts of feature/category combinations
		self.fc  = {}
	#Counts of documents in each category 
		self.cc = {}
		self.getfeatures = getfeatures

	#Increase the count of a feature/ category pair
	def incf(self, f, cat):
		self.fc.setdefault(f, {})
		self.fc[f].setdefault(cat, 0)
		self.fc[f][cat] += 1

	#Increase the count of a category
	def incc(self, cat):
		self.cc.setdefault(cat, 0)
		self.cc[cat] += 1

	#The number of times a feature has appeared in a category
	def fcount(self, f, cat):
		#print "cc ", self.cc
		#print "fc ", self.fc
		if f in self.fc and cat in self.fc[f]:
			return float(self.fc[f][cat])
		return 0.0
	#The number of times in a category
	def catcount(self, cat):
		if cat in self.cc:
			return float(self.cc[cat])
		return 0
	#The total number of times
	def totalcount(self):
		return sum(self.cc.values())
	#The list of all categories
	def categories(self):
		return self.cc.keys()

	def train(self, item, cat):
		features = self.getfeatures(item)
		#Increment the count for every feature with this category
		for f in features:
			self.incf(f,cat)
		#Increment the count for this category
		self.incc(cat)
	
	def fprob(self, f, cat):
		if self.catcount(cat)==0: return 0
		#Total number of times this feature appeared 
		#Category divided by the total no of times in this category
		return self.fcount(f,cat)/self.catcount(cat)
	
	def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
		#Calculate current probability
		basicprob = prf(f, cat)
		
		#Count the number of times this feature has appeared in 
		#all categories
		totals = sum([self.fcount(f,c) for c in self.categories()])
		
		#Calculate the weighted average
		bp = ((weight*ap) + (totals*basicprob)) / (weight + totals)
		return bp

#Subclass NaiveBayes Classifier
class naivebayes(classifier):
	def docprob(self, item, cat):
		features = self.getfeatures(item)
		
		#Multiply the probabilities of all features together
		p = 1
		for f in features: p *= self.weightedprob(f, cat, self.fprob)
		return p
			
	def prob(self, item, cat):
		catprob = self.catcount(cat)/self.totalcount()
		docprob = self.docprob(item, cat)
		return docprob*catprob
	

def sampletrain(cl, text, subject):
	cl.train(text, subject)


cl1 = naivebayes(getwords)
#Naive Bayes Classifier
f = open("training.json", "r")
test = open("inputs.json", "r")
i = 0
for line in f:
	if i != 0:
		j = json.loads(line)
		text = j['question'] + j['excerpt']
		sampletrain(cl1, text, j['topic'])
	i += 1
i = 0
for line in test:
	if i!= 0:
		j = json.loads(line)
		text = j['question'] + j['excerpt']
		max_prob = 0
		index = "A"
		for types in cl1.cc:				
			temp = cl1.prob(text, types)
			if temp > max_prob:
				max_prob = temp
				index = types
		index = index + "\n"
		with open("output.txt", "a") as myfile:
			myfile.write(index)
	i += 1
			
	
test = open("output.txt","r")
correction = open("correct_output.txt","r")
test_array = []
correct_array = []
correct = 0
wrong = 0
for line in test:
	test_array.append(line)
for line in correction:
	correct_array.append(line)
for i in range(len(test_array)):
	if test_array[i] == correct_array[i]:
		correct += 1
	else:
		wrong += 1
print "NO of correct Predictions",correct
print "No of wrong predictions", wrong
print "Percentage Sucess", correct/(correct+wrong)

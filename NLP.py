#Program By: Pritish Yuvraj
#In this program we classify text read through a JSON file into 10 different categories. 
#All the supporting files could be downloaded from URL: 
#"training.json" as the name suggests is required to train the algorithm"
#"inputs.json" is the input the file whose outputs need to be known"
#"output.txt" is the output which my program generated
#"corrected_output.txt" is the output which the program should have generated
#This NLP program uses Bayes Classification and accuracy was 72.93%

from __future__ import division
import json
import re
import sys

f = open("training.json","r")

#To remove all special characters and return all words in lower case
def lower_case(line):
	line = re.sub('[^a-zA-Z0-9 ]', '', line)
	return line.lower()

#To remove some of the uncessary common words
def waste_words(line):
	remove_list = ['the','or','and','fuckoff','help','show','api','-','labels','dynamic','results','find','calculate','do','titles','python','possible','cannot','import','not','using','google','name','fields','list','server','merge','[duplicate]','each','source','identify','where','mean','system','application','on','be','are','query','extract','event','best','column','what','network','for','selected','access','unable','between','print','new','esri','issue','correct','converting','10.1','creating','missing','javascript','use','plugin','of','script','through','attributes','analysis','other','cant','load','via','within','file?','number','one','set','table','another','model','[closed]','update','but','data','class','problems','after','why','buffer','used','you','spatial','which','without','data','when','get','make','no','different','if','any','return','importing','in','at','as','need','an','it','is','than','all','text','over','same','adding','based','how','to','only','does','input','save','into','tiles','view','by','/','version','can','add','from','along','legend','change','convert','working','getting','point','image','size','select','given','area','there','custom','way','type','empty','that','tool','export','with','join','this','up','i','r','values','install','error','problem','my','display','function','have','single','file','data?','lines','time','a','sql']
	line = line.split()
	sentence_to_return = ' '.join([i for i in line if i not in remove_list])
	return sentence_to_return
#Calculating the probability of the occurence of a each word given a particular domain. i.e. P(word1|Domain) U P(word2|Domain) U P(word3|Domain)...
# .... P(wordN|Domain)
def cal_prob(d,item,text1):
	probablity = 0
	sum_for_item = sum(d[item].values())
	text1 = text1.split()
	for text in text1:
		if text in d[item]:
			probablity += (d[item][text]/sum_for_item)
	return probablity					


i=0
question = {}
answer = {}
d = {}
final = {}
topic = 'gis'
for line in f:
	if i!=0:
		j = json.loads(line)
		#print j['topic']
		topic = j['topic']
		#print "Found one"
		q = waste_words(lower_case(j['question']))
		a = waste_words(lower_case(j['excerpt']))
		ques = q.split()
		if topic not in d:
			d[topic] = d.get(topic, {})
			final[topic] = final.get(topic, {})
		for word in ques:
			if word not in d[topic]:
				d[topic][word] = d.get(word, {})
				d[topic][word] = 1		
			else:
				d[topic][word] += 1
		ans = a.split()
		for word in ans:
			if word not in d[topic]:
				d[topic][word] = d.get(word, {})
				d[topic][word] = 1		
			else:
				d[topic][word] += 1
	i += 1

#Select only those words with frequeny above 10
for topic in d:
	for i in d[topic]:
		if d[topic][i] >= 10:
			final[topic][i] = final.get(i,{})
			final[topic][i] = d[topic][i]


#json.dump(final,open("brain.txt","w"))	

#Calculating Probability

print "Starting to read"
g = open("inputs.json","r")
l=0
for abc in g:
	if l !=0:
		max_prob = 0
		index = 'gis'
		a= json.loads(abc)
		b = a['question'] + a['excerpt']
		b = waste_words(lower_case(b))
		for i in final:
			prob = cal_prob(final,i,b)
			if max_prob < prob:
				index = i
				max_prob = prob
		index = index + "\n"
		with open("output.txt","a") as myfile:
			myfile.write(index)	
		#print index	
	l += 1
	
#To know the accuracy of the program
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
print correct, wrong

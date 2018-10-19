#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 18:44
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : classifyNB.py
# @Software: PyCharm

from loadDataSet import *
from trainNB0 import *

def classifyNB (vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum (vec2Classify * p1Vec) + np.log (pClass1)
	p0 = sum (vec2Classify * p0Vec) + np.log (1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0

def testingNB():
	listOPosts, listClasses = loadDataSet()
	myVocabList = createVocabList (listOPosts)
	trainMat = []
	for postinDoc in listOPosts:
		trainMat.append (setOfWords2Vec (myVocabList, postinDoc))
	p0V, p1V, pAb = trainNB0 (np.array (trainMat), np.array (listClasses))
	testEntry = ['love', 'my', 'dalmation']
	thisDoc = np.array (setOfWords2Vec (myVocabList, testEntry))
	print (testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
	testEntry = ['stupid', 'garbage']
	thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
	print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))

if __name__ == '__main__':
	testingNB()
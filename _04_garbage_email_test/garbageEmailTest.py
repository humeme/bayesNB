#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:03
# @Author  : Humeme
# @Site    : ??????
# @File    : garbageEmailTest.py
# @Software: PyCharm

from numpy import *
from trainNB0 import trainNB0
from classifyNB import classifyNB
from createVocabList import createVocabList
from bagOfWords2VecMN import bagOfWords2VecMN

def textParse (bigString):
	import re
	# 利用正则表达式进行切分，将特殊符号作为作为切分标志，即非字母、非数字
	listOfTokens = re.split(r'\W+', bigString)
	# 把字符大于两个的单词都变成小写
	return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
	docList=[]; classList = []; fullText =[]
	for i in range(1,26):
		# 读取25个垃圾文件，把字符串转换成字符串列表
		wordList = textParse(open('email/spam/%d.txt' % i, 'r').read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		# 读取25个非垃圾文件，把字符串转换成字符串列表
		wordList = textParse(open('email/ham/%d.txt' % i, 'r').read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	# 创建无重复的词汇表
	vocabList = createVocabList(docList)				#create vocabulary
	# 创建存储训练集的索引值的列表和测试集的索引值的列表，[0...49]
	trainingSet = list(range(50))
	testSet=[]         								    #create test set
	for i in range(10):
		# 从 50 个中随机选取 10 个做测试集索引值
		randIndex = int(random.uniform(0,len(trainingSet)))
		# 根据测试组的索引值添加trainingSet中的数字
		testSet.append(trainingSet[randIndex])
		# 删掉被选中的测试组
		del(trainingSet[randIndex])
	trainMat=[]
	trainClasses = []
	for docIndex in trainingSet:					#train the classifier (get probs) trainNB0
		# 将生成词汇集添加在训练集包中，就是一维的无重复词汇在循环匹配50个数据维组
		trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
		# 将分类类别添加到训练标签中，把40个数据进行分类
		trainClasses.append(classList[docIndex])
	# p0V：非垃圾邮件，p1V：垃圾邮件，pSpam：先验概率
	p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
	print ('p0V=', p0V)
	print ('p1V=', p1V)
	print ('pSpam=', pSpam)
	# 统计错误个数和错误率
	errorCount = 0
	# 遍历测试集
	for docIndex in testSet:        #classify the remaining items
		#
		wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
		print ('wordVector= ', wordVector)
		if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
			errorCount += 1
			print ("classification error",docList[docIndex])
	print ('the error rate is: ',float(errorCount)/len(testSet))

if __name__ == '__main__':
	spamTest()
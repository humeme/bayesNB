#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 19:29
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : loadDataSet.py
# @Software: PyCharm

def loadDataSet ():
	postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
				   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
				   ['my', 'dalmation', 'is', 'so', 'cute', 'i', 'love', 'him'],
				   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
				   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
				   ['quit','buying', 'worthless', 'dog', 'food','stupid']]
	classVec = [0,1,0,1,0,1]
	return postingList,classVec

# 函数说明： 将词汇整理成不重复的词汇列表
def createVocabList (dataSet):
	# set 返回的是无序的集合，于是也就没有了重复的内容, 这里为什么加中括号没想明白，调试去掉仍可以
	vocabSet = set([])
	# 循环处理输入的词汇
	for document in dataSet:
		# 取并集
		vocabSet = vocabSet | set(document)
		# 返回一个列表
	return list (vocabSet)

# 函数说明：根据 vocaList 的无重复词汇表，判断 inputSet 每一个数组中是否有单词是一致的。
# 第一个参数vocabList：createVocabList（）函数的无重复词汇返回值，
# 第二个参数inputSet：loadDataSet () 函数的词汇表取出每一行来进行处理
def setOfWords2Vec (vocabList, inputSet):
	# 创建一个所有元素为 0 的列表
	returnVec = [0] * len(vocabList)
	#print ('returnVec= ',returnVec)
	# 循环取出 inputSet 中的单词，也就是 loadDataSet 中 dataSet
	for word in inputSet:
		# 判断词汇是否存在 vocabList 中
		if word in vocabList:
			# index 是如果 word 存在，则返回该词的下标，并赋值为 1
			returnVec[vocabList.index(word)] = 1
		else:
			print('the word: %s is not in my Vocabulary!' % word)
	return returnVec
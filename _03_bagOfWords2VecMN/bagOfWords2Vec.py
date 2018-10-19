#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 10:35
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : bagOfWords2Vec.py
# @Software: PyCharm

def bagOfWords2VecMN(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec
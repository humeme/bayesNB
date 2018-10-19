#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:15
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : bagOfWords2VecMN.py
# @Software: PyCharm

# 统计每一组数据在整体里出现的次数
def bagOfWords2VecMN(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec
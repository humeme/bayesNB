#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 18:42
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : trainNB0.py
# @Software: PyCharm

import numpy as np

# 函数说明：
# 第一个参数trainMatrix：是 createVocabList 函数的无重复词汇数组
# 第二个参数trainCategory：是 loadDataSet 函数的标记值
def trainNB0(trainMatrix, trainCategory):
	# 计算训练文档的数目
	numTrainDocs = len (trainMatrix)
	# 计算每篇文档的词条数
	numWords = len (trainMatrix[0])
	# 文档属于侮辱类的概率，也就是先验概率
	pAbusive = sum (trainCategory) / float (numTrainDocs)
	# 统计非侮辱和侮辱性词汇个数的向量初始化
	p0Num = np.ones(numWords)
	p1Num = np.ones(numWords)
	#p0Num = np.zeros (numWords)
	#p1Num = np.zeros (numWords)
	# 初始化非侮辱和侮辱性词汇个数
	p0Denom = 2.0
	p1Denom = 2.0
	#p0Denom = 0.0
	#p1Denom = 0.0
	# 循环处理六组数据，计算非侮辱和侮辱性词汇的概率
	for i in range (numTrainDocs):
		# 统计侮辱性词汇的个数和总数
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum (trainMatrix[i])
		# 统计非侮辱性词汇的个数和总数
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	# 计算侮辱性和非侮辱性词汇的概率
	p1Vect = np.log(p1Num / p1Denom)
	p0Vect = np.log(p0Num / p0Denom)			# 不加np会报错，因为python中 numpy与math不通用
	#p1Vect = p1Num / p1Denom
	#p0Vect = p0Num / p0Denom
	return p0Vect, p1Vect, pAbusive
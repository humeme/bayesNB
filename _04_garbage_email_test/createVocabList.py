#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:14
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : createVocabList.py
# @Software: PyCharm

def createVocabList (dataSet):
	# set 返回的是无序的集合，于是也就没有了重复的内容, 这里为什么加中括号没想明白，调试去掉仍可以
	vocabSet = set([])
	# 循环处理输入的词汇
	for document in dataSet:
		# 取并集
		vocabSet = vocabSet | set(document)
		# 返回一个列表
	return list (vocabSet)
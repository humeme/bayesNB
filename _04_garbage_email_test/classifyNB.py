#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:18
# @Author  : Humeme
# @Site    : 湘潭大学
# @File    : classifyNB.py
# @Software: PyCharm

import numpy as np

def classifyNB (vec2Classify, p0Vec, p1Vec, pClass1):
	# print ('sum (vec2Classify * p1Vec)=', sum (vec2Classify * p1Vec))
	p1 = sum (vec2Classify * p1Vec) + np.log (pClass1)
	p0 = sum (vec2Classify * p0Vec) + np.log (1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0
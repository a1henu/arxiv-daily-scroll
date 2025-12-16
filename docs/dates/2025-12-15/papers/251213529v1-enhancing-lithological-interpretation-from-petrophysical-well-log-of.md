---
layout: default
title: Enhancing lithological interpretation from petrophysical well log of IODP expedition 390/393 using machine learning
---

# Enhancing lithological interpretation from petrophysical well log of IODP expedition 390/393 using machine learning
**arXiv**：[2512.13529v1](https://arxiv.org/abs/2512.13529) · [PDF](https://arxiv.org/pdf/2512.13529.pdf)  
**作者**：Raj Sahu, Saumen Maiti  

**一句话要点**：提出联合机器学习方法以增强IODP测井数据的岩性解释

**关键词**：岩性解释, 机器学习, 测井数据分析, 监督学习, 无监督学习, IODP

## 3 点简述
- 核心问题：传统线性统计方法难以区分重叠测井信号中的岩性和岩相。
- 方法要点：开发监督和无监督机器学习算法，联合分析多变量测井数据。
- 实验或效果：决策树和梯度提升模型表现最佳，准确率达0.9950，F1分数为0.9951。

## 摘要（原文）

> Enhanced lithological interpretation from well logs plays a key role in geological resource exploration and mapping, as well as in geo-environmental modeling studies. Core and cutting information is useful for making sound interpretations of well logs; however, these are rarely collected at each depth due to high costs. Moreover, well log interpretation using traditional methods is constrained by poor borehole conditions. Traditional statistical methods are mostly linear, often failing to discriminate between lithology and rock facies, particularly when dealing with overlapping well log signals characterized by the structural and compositional variation of rock types. In this study, we develop multiple supervised and unsupervised machine learning algorithms to jointly analyze multivariate well log data from Integrated Ocean Drilling Program (IODP) expeditions 390 and 393 for enhanced lithological interpretations. Among the algorithms, Logistic Regression, Decision Trees, Gradient Boosting, Support Vector Machines (SVM), k-Nearest Neighbors (KNN), and Multi-Layer Perceptron (MLP) neural network models, the Decision Tree and Gradient Boosting models outperformed the others, achieving an accuracy of 0.9950 and an F1-score of 0.9951. While unsupervised machine learning (ML) provides the foundation for cluster information that inherently supports the classification algorithm, supervised ML is applied to devise a data-driven lithology clustering mechanism for IODP datasets. The joint ML-based method developed here has the potential to be further explored for analyzing other well log datasets from the world's oceans.


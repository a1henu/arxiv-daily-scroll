---
layout: default
title: Consistency-guided semi-supervised outlier detection in heterogeneous data using fuzzy rough sets
---

# Consistency-guided semi-supervised outlier detection in heterogeneous data using fuzzy rough sets
**arXiv**：[2512.18977v1](https://arxiv.org/abs/2512.18977) · [PDF](https://arxiv.org/pdf/2512.18977.pdf)  
**作者**：Baiyang Chen, Zhong Yuan, Dezhong Peng, Xiaoliang Chen, Hongmei Chen  

**一句话要点**：提出一致性引导的半监督异常检测算法，利用模糊粗糙集处理异构数据

**关键词**：半监督异常检测, 异构数据处理, 模糊粗糙集, 分类一致性, 异常因子, 标签信息利用

## 3 点简述
- 核心问题：现有半监督异常检测方法多针对数值数据，忽略异构数据信息，导致假阳性率高。
- 方法要点：基于模糊粗糙集理论，利用少量标记异常构建标签信息模糊相似关系，结合分类一致性和异常因子预测异常。
- 实验或效果：在15个新数据集上评估，算法优于或可比肩领先的异常检测器。

## 摘要（原文）

> Outlier detection aims to find samples that behave differently from the majority of the data. Semi-supervised detection methods can utilize the supervision of partial labels, thus reducing false positive rates. However, most of the current semi-supervised methods focus on numerical data and neglect the heterogeneity of data information. In this paper, we propose a consistency-guided outlier detection algorithm (COD) for heterogeneous data with the fuzzy rough set theory in a semi-supervised manner. First, a few labeled outliers are leveraged to construct label-informed fuzzy similarity relations. Next, the consistency of the fuzzy decision system is introduced to evaluate attributes' contributions to knowledge classification. Subsequently, we define the outlier factor based on the fuzzy similarity class and predict outliers by integrating the classification consistency and the outlier factor. The proposed algorithm is extensively evaluated on 15 freshly proposed datasets. Experimental results demonstrate that COD is better than or comparable with the leading outlier detectors. This manuscript is the accepted author version of a paper published by Elsevier. The final published version is available at https://doi.org/10.1016/j.asoc.2024.112070


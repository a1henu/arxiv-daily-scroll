---
layout: default
title: Bipartite Mode Matching for Vision Training Set Search from a Hierarchical Data Server
---

# Bipartite Mode Matching for Vision Training Set Search from a Hierarchical Data Server
**arXiv**：[2601.09531v1](https://arxiv.org/abs/2601.09531) · [PDF](https://arxiv.org/pdf/2601.09531.pdf)  
**作者**：Yue Yao, Ruining Yang, Tom Gedeon  

**一句话要点**：提出二分模式匹配算法以从分层数据服务器构建替代训练集，减少目标域与源域间的模式差距。

**关键词**：无监督域适应, 训练集搜索, 模式匹配, 分层数据服务器, 对象重识别

## 3 点简述
- 核心问题：目标域可访问但无法实时标注，需从大规模数据服务器搜索训练集以覆盖目标模式。
- 方法要点：引入分层数据服务器和二分模式匹配算法，一对一对齐源域与目标域的模式。
- 实验或效果：在对象重识别和检测任务中，搜索的训练集域差距更小，模型准确率更高。

## 摘要（原文）

> We explore a situation in which the target domain is accessible, but real-time data annotation is not feasible. Instead, we would like to construct an alternative training set from a large-scale data server so that a competitive model can be obtained. For this problem, because the target domain usually exhibits distinct modes (i.e., semantic clusters representing data distribution), if the training set does not contain these target modes, the model performance would be compromised. While prior existing works improve algorithms iteratively, our research explores the often-overlooked potential of optimizing the structure of the data server. Inspired by the hierarchical nature of web search engines, we introduce a hierarchical data server, together with a bipartite mode matching algorithm (BMM) to align source and target modes. For each target mode, we look in the server data tree for the best mode match, which might be large or small in size. Through bipartite matching, we aim for all target modes to be optimally matched with source modes in a one-on-one fashion. Compared with existing training set search algorithms, we show that the matched server modes constitute training sets that have consistently smaller domain gaps with the target domain across object re-identification (re-ID) and detection tasks. Consequently, models trained on our searched training sets have higher accuracy than those trained otherwise. BMM allows data-centric unsupervised domain adaptation (UDA) orthogonal to existing model-centric UDA methods. By combining the BMM with existing UDA methods like pseudo-labeling, further improvement is observed.


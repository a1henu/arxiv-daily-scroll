---
layout: default
title: Hierarchical Ranking Neural Network for Long Document Readability Assessment
---

# Hierarchical Ranking Neural Network for Long Document Readability Assessment
**arXiv**：[2511.21473v1](https://arxiv.org/abs/2511.21473) · [PDF](https://arxiv.org/pdf/2511.21473.pdf)  
**作者**：Yurui Zheng, Yijun Chen, Shaohong Zhang  

**一句话要点**：提出分层排序神经网络以解决长文档可读性评估问题

**关键词**：可读性评估, 分层神经网络, 排序算法, 长文档处理, 双向机制

## 3 点简述
- 核心问题：现有方法忽略文本长度和可读性标签的序关系
- 方法要点：使用双向机制预测句子可读性，结合排序算法建模标签序关系
- 实验或效果：在中英文数据集上表现优于基线模型

## 摘要（原文）

> Readability assessment aims to evaluate the reading difficulty of a text. In recent years, while deep learning technology has been gradually applied to readability assessment, most approaches fail to consider either the length of the text or the ordinal relationship of readability labels. This paper proposes a bidirectional readability assessment mechanism that captures contextual information to identify regions with rich semantic information in the text, thereby predicting the readability level of individual sentences. These sentence-level labels are then used to assist in predicting the overall readability level of the document. Additionally, a pairwise sorting algorithm is introduced to model the ordinal relationship between readability levels through label subtraction. Experimental results on Chinese and English datasets demonstrate that the proposed model achieves competitive performance and outperforms other baseline models.


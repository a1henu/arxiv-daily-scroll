---
layout: default
title: SEAnet: A Deep Learning Architecture for Data Series Similarity Search
---

# SEAnet: A Deep Learning Architecture for Data Series Similarity Search
**arXiv**：[2603.01448v1](https://arxiv.org/abs/2603.01448) · [PDF](https://arxiv.org/pdf/2603.01448.pdf)  
**作者**：Qitong Wang, Themis Palpanas  

**一句话要点**：提出SEAnet架构以提升数据序列相似性搜索性能

**关键词**：数据序列相似性搜索, 深度嵌入近似, SAX索引, 神经网络架构, 大规模数据集训练

## 3 点简述
- 核心问题：SAX索引在高频、弱相关或噪声数据中性能不足
- 方法要点：引入深度嵌入近似和平方和保持属性设计SEAnet
- 实验或效果：在7个数据集上验证了高质量摘要和相似性搜索优势

## 摘要（原文）

> A key operation for massive data series collection analysis is similarity search. According to recent studies, SAX-based indexes offer state-of-the-art performance for similarity search tasks. However, their performance lags under high-frequency, weakly correlated, excessively noisy, or other dataset-specific properties. In this work, we propose Deep Embedding Approximation (DEA), a novel family of data series summarization techniques based on deep neural networks. Moreover, we describe SEAnet, a novel architecture especially designed for learning DEA, that introduces the Sum of Squares preservation property into the deep network design. We further enhance SEAnet with SEAtrans encoder. Finally, we propose novel sampling strategies, SEAsam and SEAsamE, that allow SEAnet to effectively train on massive datasets. Comprehensive experiments on 7 diverse synthetic and real datasets verify the advantages of DEA learned using SEAnet in providing high-quality data series summarizations and similarity search results.


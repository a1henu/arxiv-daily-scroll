---
layout: default
title: TBDFiltering: Sample-Efficient Tree-Based Data Filtering
---

# TBDFiltering: Sample-Efficient Tree-Based Data Filtering
**arXiv**：[2601.22016v1](https://arxiv.org/abs/2601.22016) · [PDF](https://arxiv.org/pdf/2601.22016.pdf)  
**作者**：Robert Istvan Busa-Fekete, Julian Zimmert, Anne Xiangyi Zheng, Claudio Gentile, Andras Gyorgy  

**一句话要点**：提出基于文本嵌入的层次聚类方法，以高效筛选大语言模型训练数据

**关键词**：数据筛选, 层次聚类, 文本嵌入, 大语言模型, 查询效率, 机器学习

## 3 点简述
- 核心问题：缺乏廉价可靠的质量指标，难以从海量文档中筛选高质量训练数据
- 方法要点：通过层次聚类自适应选择文档，利用LLM评估聚类质量，减少查询次数
- 实验或效果：在实验中优于其他基于分类器的过滤方法，证明查询效率高

## 摘要（原文）

> The quality of machine learning models depends heavily on their training data. Selecting high-quality, diverse training sets for large language models (LLMs) is a difficult task, due to the lack of cheap and reliable quality metrics. While querying existing LLMs for document quality is common, this is not scalable to the large number (billions) of documents used in training. Instead, practitioners often use classifiers trained on sparse quality signals. In this paper, we propose a text-embedding-based hierarchical clustering approach that adaptively selects the documents to be evaluated by the LLM to estimate cluster quality. We prove that our method is query efficient: under the assumption that the hierarchical clustering contains a subtree such that each leaf cluster in the tree is pure enough (i.e., it mostly contains either only good or only bad documents), with high probability, the method can correctly predict the quality of each document after querying a small number of documents. The number of such documents is proportional to the size of the smallest subtree with (almost) pure leaves, without the algorithm knowing this subtree in advance. Furthermore, in a comprehensive experimental study, we demonstrate the benefits of our algorithm compared to other classifier-based filtering methods.


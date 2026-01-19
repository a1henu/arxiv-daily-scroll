---
layout: default
title: Optimized Algorithms for Text Clustering with LLM-Generated Constraints
---

# Optimized Algorithms for Text Clustering with LLM-Generated Constraints
**arXiv**：[2601.11118v1](https://arxiv.org/abs/2601.11118) · [PDF](https://arxiv.org/pdf/2601.11118.pdf)  
**作者**：Chaoqi Jia, Weihong Wu, Longkun Guo, Zhigang Lu, Chao Chen, Kok-Leong Ong  

**一句话要点**：提出基于LLM生成约束集的优化算法，以提升文本聚类效率与准确性

**关键词**：文本聚类, LLM约束生成, 优化算法, 置信度阈值, 资源效率

## 3 点简述
- 核心问题：传统聚类方法依赖成对约束，资源消耗大且效率低。
- 方法要点：采用约束集生成减少LLM查询，结合置信度阈值和惩罚机制处理不准确约束。
- 实验或效果：在五个文本数据集上，聚类精度媲美先进方法，LLM查询次数减少20倍以上。

## 摘要（原文）

> Clustering is a fundamental tool that has garnered significant interest across a wide range of applications including text analysis. To improve clustering accuracy, many researchers have incorporated background knowledge, typically in the form of must-link and cannot-link constraints, to guide the clustering process. With the recent advent of large language models (LLMs), there is growing interest in improving clustering quality through LLM-based automatic constraint generation. In this paper, we propose a novel constraint-generation approach that reduces resource consumption by generating constraint sets rather than using traditional pairwise constraints. This approach improves both query efficiency and constraint accuracy compared to state-of-the-art methods. We further introduce a constrained clustering algorithm tailored to the characteristics of LLM-generated constraints. Our method incorporates a confidence threshold and a penalty mechanism to address potentially inaccurate constraints. We evaluate our approach on five text datasets, considering both the cost of constraint generation and the overall clustering performance. The results show that our method achieves clustering accuracy comparable to the state-of-the-art algorithms while reducing the number of LLM queries by more than 20 times.


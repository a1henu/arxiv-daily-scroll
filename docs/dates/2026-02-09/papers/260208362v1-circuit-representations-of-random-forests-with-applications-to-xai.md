---
layout: default
title: Circuit Representations of Random Forests with Applications to XAI
---

# Circuit Representations of Random Forests with Applications to XAI
**arXiv**：[2602.08362v1](https://arxiv.org/abs/2602.08362) · [PDF](https://arxiv.org/pdf/2602.08362.pdf)  
**作者**：Chunxi Ji, Adnan Darwiche  

**一句话要点**：提出随机森林电路编译方法以提升可解释人工智能效率与应用

**关键词**：随机森林, 可解释人工智能, 电路编译, 决策解释, 鲁棒性分析

## 3 点简述
- 核心问题：随机森林分类器缺乏高效可解释性表示，影响决策解释计算。
- 方法要点：编译随机森林为电路，直接编码类别实例，并开发算法计算决策原因与鲁棒性。
- 实验或效果：方法比现有方法更高效，支持枚举充分、必要原因及对比解释，应用于多数据集。

## 摘要（原文）

> We make three contributions in this paper. First, we present an approach for compiling a random forest classifier into a set of circuits, where each circuit directly encodes the instances in some class of the classifier. We show empirically that our proposed approach is significantly more efficient than existing similar approaches. Next, we utilize this approach to further obtain circuits that are tractable for computing the complete and general reasons of a decision, which are instance abstractions that play a fundamental role in computing explanations. Finally, we propose algorithms for computing the robustness of a decision and all shortest ways to flip it. We illustrate the utility of our contributions by using them to enumerate all sufficient reasons, necessary reasons and contrastive explanations of decisions; to compute the robustness of decisions; and to identify all shortest ways to flip the decisions made by random forest classifiers learned from a wide range of datasets.


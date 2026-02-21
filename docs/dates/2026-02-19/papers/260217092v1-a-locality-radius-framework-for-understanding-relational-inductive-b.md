---
layout: default
title: A Locality Radius Framework for Understanding Relational Inductive Bias in Database Learning
---

# A Locality Radius Framework for Understanding Relational Inductive Bias in Database Learning
**arXiv**：[2602.17092v1](https://arxiv.org/abs/2602.17092) · [PDF](https://arxiv.org/pdf/2602.17092.pdf)  
**作者**：Aadi Joshi, Kavya Bhand  

**一句话要点**：提出局部性半径框架以理解数据库学习中关系归纳偏置的影响

**关键词**：关系归纳偏置, 局部性半径, 图神经网络, 数据库学习, 结构推理, 模式预测

## 3 点简述
- 核心问题：关系模式中多跳结构推理何时必要，模型性能与任务结构需求的关系未知
- 方法要点：引入局部性半径作为衡量预测所需最小结构邻域的正式度量，假设性能取决于任务半径与架构聚合深度的对齐
- 实验或效果：通过外键预测等任务进行实证研究，结果显示一致的偏置-半径对齐效应

## 摘要（原文）

> Foreign key discovery and related schema-level prediction tasks are often modeled using graph neural networks (GNNs), implicitly assuming that relational inductive bias improves performance. However, it remains unclear when multi-hop structural reasoning is actually necessary. In this work, we introduce locality radius, a formal measure of the minimum structural neighborhood required to determine a prediction in relational schemas. We hypothesize that model performance depends critically on alignment between task locality radius and architectural aggregation depth. We conduct a controlled empirical study across foreign key prediction, join cost estimation, blast radius regression, cascade impact classification, and additional graph-derived schema tasks. Our evaluation includes multi-seed experiments, capacity-matched comparisons, statistical significance testing, scaling analysis, and synthetic radius-controlled benchmarks. Results reveal a consistent bias-radius alignment effect.


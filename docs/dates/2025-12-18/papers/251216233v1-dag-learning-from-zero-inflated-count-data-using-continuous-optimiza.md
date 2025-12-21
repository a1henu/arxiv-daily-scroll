---
layout: default
title: DAG Learning from Zero-Inflated Count Data Using Continuous Optimization
---

# DAG Learning from Zero-Inflated Count Data Using Continuous Optimization
**arXiv**：[2512.16233v1](https://arxiv.org/abs/2512.16233) · [PDF](https://arxiv.org/pdf/2512.16233.pdf)  
**作者**：Noriaki Sato, Marco Scutari, Shuichi Kawano, Rui Yamaguchi, Seiya Imoto  

**一句话要点**：提出ZICO方法，通过连续优化从零膨胀计数数据学习有向无环图结构。

**关键词**：零膨胀计数数据, 有向无环图学习, 连续优化, 基因调控网络, 可微约束

## 3 点简述
- 核心问题：从零膨胀计数数据中学习网络结构，如基因调控网络。
- 方法要点：将节点建模为零膨胀广义线性模型，使用平滑得分函数和可微无环约束优化。
- 实验或效果：在模拟数据上性能优越、运行更快，在基因网络重构中表现相当或更好。

## 摘要（原文）

> We address network structure learning from zero-inflated count data by casting each node as a zero-inflated generalized linear model and optimizing a smooth, score-based objective under a directed acyclic graph constraint. Our Zero-Inflated Continuous Optimization (ZICO) approach uses node-wise likelihoods with canonical links and enforces acyclicity through a differentiable surrogate constraint combined with sparsity regularization. ZICO achieves superior performance with faster runtimes on simulated data. It also performs comparably to or better than common algorithms for reverse engineering gene regulatory networks. ZICO is fully vectorized and mini-batched, enabling learning on larger variable sets with practical runtimes in a wide range of domains.


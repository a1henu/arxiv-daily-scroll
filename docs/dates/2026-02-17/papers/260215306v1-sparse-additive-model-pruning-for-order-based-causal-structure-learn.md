---
layout: default
title: Sparse Additive Model Pruning for Order-Based Causal Structure Learning
---

# Sparse Additive Model Pruning for Order-Based Causal Structure Learning
**arXiv**：[2602.15306v1](https://arxiv.org/abs/2602.15306) · [PDF](https://arxiv.org/pdf/2602.15306.pdf)  
**作者**：Kentaro Kanamori, Hirofumi Suzuki, Takuya Takagi  

**一句话要点**：提出基于稀疏加性模型的剪枝方法，以提升基于顺序的因果结构学习效率与准确性

**关键词**：因果结构学习, 稀疏加性模型, 剪枝方法, 顺序学习, 计算效率

## 3 点简述
- 核心问题：现有CAM剪枝方法计算开销大且可能因多重检验损害估计质量
- 方法要点：结合随机树嵌入与组稀疏回归，直接剪枝冗余边，避免假设检验
- 实验或效果：在合成与真实数据集上显著加速，保持或超越现有方法准确性

## 摘要（原文）

> Causal structure learning, also known as causal discovery, aims to estimate causal relationships between variables as a form of a causal directed acyclic graph (DAG) from observational data. One of the major frameworks is the order-based approach that first estimates a topological order of the underlying DAG and then prunes spurious edges from the fully-connected DAG induced by the estimated topological order. Previous studies often focus on the former ordering step because it can dramatically reduce the search space of DAGs. In practice, the latter pruning step is equally crucial for ensuring both computational efficiency and estimation accuracy. Most existing methods employ a pruning technique based on generalized additive models and hypothesis testing, commonly known as CAM-pruning. However, this approach can be a computational bottleneck as it requires repeatedly fitting additive models for all variables. Furthermore, it may harm estimation quality due to multiple testing. To address these issues, we introduce a new pruning method based on sparse additive models, which enables direct pruning of redundant edges without relying on hypothesis testing. We propose an efficient algorithm for learning sparse additive models by combining the randomized tree embedding technique with group-wise sparse regression. Experimental results on both synthetic and real datasets demonstrated that our method is significantly faster than existing pruning methods while maintaining comparable or superior accuracy.


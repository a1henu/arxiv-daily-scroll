---
layout: default
title: Balancing Symmetry and Efficiency in Graph Flow Matching
---

# Balancing Symmetry and Efficiency in Graph Flow Matching
**arXiv**：[2602.18084v1](https://arxiv.org/abs/2602.18084) · [PDF](https://arxiv.org/pdf/2602.18084.pdf)  
**作者**：Benjamin Honoré, Alba Carballo-Castro, Yiming Qin, Pascal Frossard  

**一句话要点**：提出可控对称性调制方案以平衡图生成模型中的对称性与效率

**关键词**：图生成模型, 等变性, 流匹配, 对称性调制, 过拟合控制

## 3 点简述
- 核心问题：严格等变性增加计算成本并减缓收敛，需权衡对称性与效率
- 方法要点：基于正弦位置编码和节点排列，在训练中放松离散流匹配模型的等变性
- 实验或效果：对称性破坏加速早期训练但易过拟合，适当调制可延迟过拟合并加速收敛，节省训练周期

## 摘要（原文）

> Equivariance is central to graph generative models, as it ensures the model respects the permutation symmetry of graphs. However, strict equivariance can increase computational cost due to added architectural constraints, and can slow down convergence because the model must be consistent across a large space of possible node permutations. We study this trade-off for graph generative models. Specifically, we start from an equivariant discrete flow-matching model, and relax its equivariance during training via a controllable symmetry modulation scheme based on sinusoidal positional encodings and node permutations. Experiments first show that symmetry-breaking can accelerate early training by providing an easier learning signal, but at the expense of encouraging shortcut solutions that can cause overfitting, where the model repeatedly generates graphs that are duplicates of the training set. On the contrary, properly modulating the symmetry signal can delay overfitting while accelerating convergence, allowing the model to reach stronger performance with $19\%$ of the baseline training epochs.


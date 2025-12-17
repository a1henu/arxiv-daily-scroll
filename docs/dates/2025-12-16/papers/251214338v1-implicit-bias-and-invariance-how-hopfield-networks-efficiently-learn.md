---
layout: default
title: Implicit Bias and Invariance: How Hopfield Networks Efficiently Learn Graph Orbits
---

# Implicit Bias and Invariance: How Hopfield Networks Efficiently Learn Graph Orbits
**arXiv**：[2512.14338v1](https://arxiv.org/abs/2512.14338) · [PDF](https://arxiv.org/pdf/2512.14338.pdf)  
**作者**：Michael Murray, Tenzin Chan, Kedar Karhadker, Christopher J. Hillar  

**一句话要点**：揭示Hopfield网络通过范数效率隐式学习图同构类，实现多项式样本复杂度

**关键词**：Hopfield网络, 隐式偏置, 图同构, 不变子空间, 范数效率, 样本复杂度

## 3 点简述
- 研究神经网络在群结构数据中隐式学习对称性的机制，聚焦图同构类推断问题
- 发现Hopfield网络能将图同构类表示在三维不变子空间，梯度下降最小化能量流具有范数效率隐式偏置
- 实验表明参数随样本增长收敛至不变子空间，支持多项式样本复杂度学习图同构类

## 摘要（原文）

> Many learning problems involve symmetries, and while invariance can be built into neural architectures, it can also emerge implicitly when training on group-structured data. We study this phenomenon in classical Hopfield networks and show they can infer the full isomorphism class of a graph from a small random sample. Our results reveal that: (i) graph isomorphism classes can be represented within a three-dimensional invariant subspace, (ii) using gradient descent to minimize energy flow (MEF) has an implicit bias toward norm-efficient solutions, which underpins a polynomial sample complexity bound for learning isomorphism classes, and (iii) across multiple learning rules, parameters converge toward the invariant subspace as sample sizes grow. Together, these findings highlight a unifying mechanism for generalization in Hopfield networks: a bias toward norm efficiency in learning drives the emergence of approximate invariance under group-structured data.


---
layout: default
title: SNAP: A Self-Consistent Agreement Principle with Application to Robust Computation
---

# SNAP: A Self-Consistent Agreement Principle with Application to Robust Computation
**arXiv**：[2602.02013v1](https://arxiv.org/abs/2602.02013) · [PDF](https://arxiv.org/pdf/2602.02013.pdf)  
**作者**：Xiaoyi Jiang, Andreas Nienkötter  

**一句话要点**：提出SNAP自洽一致原则，用于无监督鲁棒计算，通过权重分配抑制异常值。

**关键词**：鲁棒计算, 自监督学习, 异常值抑制, 权重分配, 向量平均, 子空间估计

## 3 点简述
- 核心问题：高维数据中异常值影响计算鲁棒性，需无监督方法处理。
- 方法要点：基于一致-可靠性假设，SNAP分配权重量化一致性，指数抑制异常值权重。
- 实验或效果：在向量平均和子空间估计中，非迭代SNAP优于迭代Weiszfeld算法和多元中位数均值变体。

## 摘要（原文）

> We introduce SNAP (Self-coNsistent Agreement Principle), a self-supervised framework for robust computation based on mutual agreement. Based on an Agreement-Reliability Hypothesis SNAP assigns weights that quantify agreement, emphasizing trustworthy items and downweighting outliers without supervision or prior knowledge. A key result is the Exponential Suppression of Outlier Weights, ensuring that outliers contribute negligibly to computations, even in high-dimensional settings. We study properties of SNAP weighting scheme and show its practical benefits on vector averaging and subspace estimation. Particularly, we demonstrate that non-iterative SNAP outperforms the iterative Weiszfeld algorithm and two variants of multivariate median of means. SNAP thus provides a flexible, easy-to-use, broadly applicable approach to robust computation.


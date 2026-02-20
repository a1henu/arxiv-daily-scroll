---
layout: default
title: Partial Optimality in the Preordering Problem
---

# Partial Optimality in the Preordering Problem
**arXiv**：[2602.17346v1](https://arxiv.org/abs/2602.17346) · [PDF](https://arxiv.org/pdf/2602.17346.pdf)  
**作者**：David Stein, Jannik Irmai, Bjoern Andres  

**一句话要点**：提出新部分最优性条件与高效算法，以提升预序问题中不可比较对的判定效率

**关键词**：预序问题, 部分最优性, NP难问题, 高效算法, 生物信息学, 社交网络分析

## 3 点简述
- 预序问题推广聚类与偏序，在生物信息学与社交网络分析中应用，旨在最大化满足预序关系的值对总和
- 基于现有部分求解方法，贡献新部分最优性条件及高效判定算法，增强对最优预序中不可比较对的识别
- 在真实与合成数据实验中，新条件显著提高高效判定不可比较对的比例，提升求解效率

## 摘要（原文）

> Preordering is a generalization of clustering and partial ordering with applications in bioinformatics and social network analysis. Given a finite set $V$ and a value $c_{ab} \in \mathbb{R}$ for every ordered pair $ab$ of elements of $V$, the preordering problem asks for a preorder $\lesssim$ on $V$ that maximizes the sum of the values of those pairs $ab$ for which $a \lesssim b$. Building on the state of the art in solving this NP-hard problem partially, we contribute new partial optimality conditions and efficient algorithms for deciding these conditions. In experiments with real and synthetic data, these new conditions increase, in particular, the fraction of pairs $ab$ for which it is decided efficiently that $a \not\lesssim b$ in an optimal preorder.


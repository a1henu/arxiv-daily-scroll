---
layout: default
title: Partial Optimality in the Preordering Problem
---

# Partial Optimality in the Preordering Problem
**arXiv**：[2602.17346v1](https://arxiv.org/abs/2602.17346) · [PDF](https://arxiv.org/pdf/2602.17346.pdf)  
**作者**：David Stein, Jannik Irmai, Bjoern Andres  

**一句话要点**：提出新的部分最优性条件与高效算法，以增强预排序问题的求解能力

**关键词**：预排序问题, 部分最优性, NP难问题, 高效算法, 生物信息学, 社会网络分析

## 3 点简述
- 预排序问题作为聚类和偏序的泛化，应用于生物信息学和社会网络分析
- 贡献新的部分最优性条件，并开发高效算法来判定这些条件
- 在真实和合成数据实验中，新条件提高了高效判定最优预序中不成立对的比例

## 摘要（原文）

> Preordering is a generalization of clustering and partial ordering with applications in bioinformatics and social network analysis. Given a finite set $V$ and a value $c_{ab} \in \mathbb{R}$ for every ordered pair $ab$ of elements of $V$, the preordering problem asks for a preorder $\lesssim$ on $V$ that maximizes the sum of the values of those pairs $ab$ for which $a \lesssim b$. Building on the state of the art in solving this NP-hard problem partially, we contribute new partial optimality conditions and efficient algorithms for deciding these conditions. In experiments with real and synthetic data, these new conditions increase, in particular, the fraction of pairs $ab$ for which it is decided efficiently that $a \not\lesssim b$ in an optimal preorder.


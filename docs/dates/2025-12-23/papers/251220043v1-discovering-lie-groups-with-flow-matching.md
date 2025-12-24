---
layout: default
title: Discovering Lie Groups with Flow Matching
---

# Discovering Lie Groups with Flow Matching
**arXiv**：[2512.20043v1](https://arxiv.org/abs/2512.20043) · [PDF](https://arxiv.org/pdf/2512.20043.pdf)  
**作者**：Jung Yeon Park, Yuxuan Chen, Floor Eijkelboom, Jan-Willem van de Meent, Lawson L. S. Wong, Robin Walters  

**一句话要点**：提出LieFlow方法，通过流匹配学习李群以发现数据中的对称性

**关键词**：对称性发现, 流匹配, 李群学习, 点云分析, 机器学习

## 3 点简述
- 核心问题：数据中的对称性对物理理解和机器学习性能至关重要，但需从数据中直接学习。
- 方法要点：利用流匹配在李群上学习对称性分布，假设更灵活，假设更少。
- 实验或效果：在2D和3D点云上成功发现离散群，包括复数域上的反射，并解决“最后时刻收敛”挑战。

## 摘要（原文）

> Symmetry is fundamental to understanding physical systems, and at the same time, can improve performance and sample efficiency in machine learning. Both pursuits require knowledge of the underlying symmetries in data. To address this, we propose learning symmetries directly from data via flow matching on Lie groups. We formulate symmetry discovery as learning a distribution over a larger hypothesis group, such that the learned distribution matches the symmetries observed in data. Relative to previous works, our method, \lieflow, is more flexible in terms of the types of groups it can discover and requires fewer assumptions. Experiments on 2D and 3D point clouds demonstrate the successful discovery of discrete groups, including reflections by flow matching over the complex domain. We identify a key challenge where the symmetric arrangement of the target modes causes ``last-minute convergence,'' where samples remain stationary until relatively late in the flow, and introduce a novel interpolation scheme for flow matching for symmetry discovery.


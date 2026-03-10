---
layout: default
title: Topologically Stable Hough Transform
---

# Topologically Stable Hough Transform
**arXiv**：[2603.08245v1](https://arxiv.org/abs/2603.08245) · [PDF](https://arxiv.org/pdf/2603.08245.pdf)  
**作者**：Stefan Huber, Kristóf Huszár, Michael Kerber, Martin Uray  

**一句话要点**：提出基于拓扑稳定性的霍夫变换以检测点云中的直线

**关键词**：霍夫变换, 点云处理, 直线检测, 拓扑稳定性, 持久同调

## 3 点简述
- 核心问题：传统霍夫变换在点云直线检测中因离散投票导致稳定性不足
- 方法要点：用连续评分函数替代离散投票，通过持久同调提取候选直线特征
- 实验或效果：设计并实现高效算法计算候选直线，提升检测的鲁棒性

## 摘要（原文）

> We propose an alternative formulation of the well-known Hough transform to detect lines in point clouds. Replacing the discretized voting scheme of the classical Hough transform by a continuous score function, its persistent features in the sense of persistent homology give a set of candidate lines. We also devise and implement an algorithm to efficiently compute these candidate lines.


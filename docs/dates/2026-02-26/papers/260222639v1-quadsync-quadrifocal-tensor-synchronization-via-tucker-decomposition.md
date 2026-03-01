---
layout: default
title: QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition
---

# QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition
**arXiv**：[2602.22639v1](https://arxiv.org/abs/2602.22639) · [PDF](https://arxiv.org/pdf/2602.22639.pdf)  
**作者**：Daniel Miao, Gilad Lerman, Joe Kileel  

**一句话要点**：提出QuadSync框架，通过Tucker分解从四焦张量同步恢复多相机姿态。

**关键词**：四焦张量同步, Tucker分解, 相机姿态恢复, 结构从运动, 多视图几何, 张量分解

## 3 点简述
- 核心问题：从四焦张量集合中高效恢复多个相机姿态，挑战传统认为四焦张量不实用的观点。
- 方法要点：构建块四焦张量，证明其具有Tucker分解，因子矩阵为堆叠相机矩阵，并开发基于Tucker分解、ADMM和IRLS的同步算法。
- 实验或效果：数值实验在现代数据集上验证方法有效性，显示高阶信息在同步中的潜力与重要性。

## 摘要（原文）

> In structure from motion, quadrifocal tensors capture more information than their pairwise counterparts (essential matrices), yet they have often been thought of as impractical and only of theoretical interest. In this work, we challenge such beliefs by providing a new framework to recover $n$ cameras from the corresponding collection of quadrifocal tensors. We form the block quadrifocal tensor and show that it admits a Tucker decomposition whose factor matrices are the stacked camera matrices, and which thus has a multilinear rank of (4,~4,~4,~4) independent of $n$. We develop the first synchronization algorithm for quadrifocal tensors, using Tucker decomposition, alternating direction method of multipliers, and iteratively reweighted least squares. We further establish relationships between the block quadrifocal, trifocal, and bifocal tensors, and introduce an algorithm that jointly synchronizes these three entities. Numerical experiments demonstrate the effectiveness of our methods on modern datasets, indicating the potential and importance of using higher-order information in synchronization.


---
layout: default
title: QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition
---

# QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition
**arXiv**：[2602.22639v1](https://arxiv.org/abs/2602.22639) · [PDF](https://arxiv.org/pdf/2602.22639.pdf)  
**作者**：Daniel Miao, Gilad Lerman, Joe Kileel  

**一句话要点**：提出QuadSync框架，通过Tucker分解同步四焦点张量以恢复多相机姿态

**关键词**：四焦点张量同步, Tucker分解, 相机姿态恢复, 结构从运动, 多线性代数, 交替方向乘子法

## 3 点简述
- 核心问题：从四焦点张量集合中高效恢复多个相机姿态，挑战传统认为其不实用的观点
- 方法要点：构建块四焦点张量，利用Tucker分解、ADMM和IRLS实现同步算法
- 实验或效果：数值实验验证方法在现代数据集上的有效性，展示高阶信息在同步中的潜力

## 摘要（原文）

> In structure from motion, quadrifocal tensors capture more information than their pairwise counterparts (essential matrices), yet they have often been thought of as impractical and only of theoretical interest. In this work, we challenge such beliefs by providing a new framework to recover $n$ cameras from the corresponding collection of quadrifocal tensors. We form the block quadrifocal tensor and show that it admits a Tucker decomposition whose factor matrices are the stacked camera matrices, and which thus has a multilinear rank of (4,~4,~4,~4) independent of $n$. We develop the first synchronization algorithm for quadrifocal tensors, using Tucker decomposition, alternating direction method of multipliers, and iteratively reweighted least squares. We further establish relationships between the block quadrifocal, trifocal, and bifocal tensors, and introduce an algorithm that jointly synchronizes these three entities. Numerical experiments demonstrate the effectiveness of our methods on modern datasets, indicating the potential and importance of using higher-order information in synchronization.


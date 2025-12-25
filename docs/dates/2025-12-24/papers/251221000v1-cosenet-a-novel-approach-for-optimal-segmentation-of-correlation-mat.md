---
layout: default
title: CoSeNet: A Novel Approach for Optimal Segmentation of Correlation Matrices
---

# CoSeNet: A Novel Approach for Optimal Segmentation of Correlation Matrices
**arXiv**：[2512.21000v1](https://arxiv.org/abs/2512.21000) · [PDF](https://arxiv.org/pdf/2512.21000.pdf)  
**作者**：Alberto. Palomo-Alonso, David Casillas-Perez, Silvia Jimenez-Fernandez, Antonio Portilla-Figueras, Sancho Salcedo-Sanz  

**一句话要点**：提出CoSeNet以优化噪声相关矩阵中的相关段分割

**关键词**：相关矩阵分割, 噪声处理, 机器学习算法, 启发式优化, 二进制输出

## 3 点简述
- 核心问题：在噪声相关矩阵中识别相关段，现有方法效果有限
- 方法要点：基于四层架构，包括重叠技术和预训练ML算法，使用启发式算法优化重缩放参数
- 实验或效果：优于先前方法，输出二进制无噪声矩阵，在效率、内存和速度间取得平衡

## 摘要（原文）

> In this paper, we propose a novel approach for the optimal identification of correlated segments in noisy correlation matrices. The proposed model is known as CoSeNet (Correlation Seg-mentation Network) and is based on a four-layer algorithmic architecture that includes several processing layers: input, formatting, re-scaling, and segmentation layer. The proposed model can effectively identify correlated segments in such matrices, better than previous approaches for similar problems. Internally, the proposed model utilizes an overlapping technique and uses pre-trained Machine Learning (ML) algorithms, which makes it robust and generalizable. CoSeNet approach also includes a method that optimizes the parameters of the re-scaling layer using a heuristic algorithm and fitness based on a Window Difference-based metric. The output of the model is a binary noise-free matrix representing optimal segmentation as well as its seg-mentation points and can be used in a variety of applications, obtaining compromise solutions between efficiency, memory, and speed of the proposed deployment model.


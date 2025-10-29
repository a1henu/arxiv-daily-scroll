---
layout: default
title: Improved Accuracy of Robot Localization Using 3-D LiDAR in a Hippocampus-Inspired Model
---

# Improved Accuracy of Robot Localization Using 3-D LiDAR in a Hippocampus-Inspired Model
**arXiv**：[2510.24029v1](https://arxiv.org/abs/2510.24029) · [PDF](https://arxiv.org/pdf/2510.24029.pdf)  
**作者**：Andrew Gerstenslager, Bekarys Dukenbaev, Ali A. Minai  

**一句话要点**：提出3D边界向量细胞模型以提升机器人3D空间定位精度

**关键词**：机器人定位, 边界向量细胞, 3D LiDAR, 空间导航, 生物启发模型

## 3 点简述
- 核心问题：2D边界向量细胞模型在水平对称环境中易产生空间歧义
- 方法要点：引入垂直角度敏感性，处理LiDAR数据以检测3D边界
- 实验效果：在3D复杂环境中显著减少空间混叠，提升定位准确性

## 摘要（原文）

> Boundary Vector Cells (BVCs) are a class of neurons in the brains of
> vertebrates that encode environmental boundaries at specific distances and
> allocentric directions, playing a central role in forming place fields in the
> hippocampus. Most computational BVC models are restricted to two-dimensional
> (2D) environments, making them prone to spatial ambiguities in the presence of
> horizontal symmetries in the environment. To address this limitation, we
> incorporate vertical angular sensitivity into the BVC framework, thereby
> enabling robust boundary detection in three dimensions, and leading to
> significantly more accurate spatial localization in a biologically-inspired
> robot model.
>   The proposed model processes LiDAR data to capture vertical contours, thereby
> disambiguating locations that would be indistinguishable under a purely 2D
> representation. Experimental results show that in environments with minimal
> vertical variation, the proposed 3D model matches the performance of a 2D
> baseline; yet, as 3D complexity increases, it yields substantially more
> distinct place fields and markedly reduces spatial aliasing. These findings
> show that adding a vertical dimension to BVC-based localization can
> significantly enhance navigation and mapping in real-world 3D spaces while
> retaining performance parity in simpler, near-planar scenarios.


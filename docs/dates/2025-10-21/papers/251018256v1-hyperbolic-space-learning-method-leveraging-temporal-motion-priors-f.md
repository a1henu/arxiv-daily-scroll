---
layout: default
title: Hyperbolic Space Learning Method Leveraging Temporal Motion Priors for Human Mesh Recovery
---

# Hyperbolic Space Learning Method Leveraging Temporal Motion Priors for Human Mesh Recovery
**arXiv**：[2510.18256v1](https://arxiv.org/abs/2510.18256) · [PDF](https://arxiv.org/pdf/2510.18256.pdf)  
**作者**：Xiang Zhang, Suping Wu, Weibin Qiu, Zhaocheng Jin, Sheng Yang  

**一句话要点**：提出双曲空间学习方法，利用时序运动先验提升视频中3D人体网格恢复精度

**关键词**：3D人体网格恢复, 双曲空间学习, 时序运动先验, 视频分析, 层次结构建模

## 3 点简述
- 现有视频方法在欧氏空间学习网格，难以捕捉人体层次结构，导致重建错误
- 设计时序运动先验提取模块和双曲空间优化策略，结合3D姿态与运动信息
- 在大型公开数据集上实验，性能优于多数先进方法，恢复网格更准确平滑

## 摘要（原文）

> 3D human meshes show a natural hierarchical structure (like
> torso-limbs-fingers). But existing video-based 3D human mesh recovery methods
> usually learn mesh features in Euclidean space. It's hard to catch this
> hierarchical structure accurately. So wrong human meshes are reconstructed. To
> solve this problem, we propose a hyperbolic space learning method leveraging
> temporal motion prior for recovering 3D human meshes from videos. First, we
> design a temporal motion prior extraction module. This module extracts the
> temporal motion features from the input 3D pose sequences and image feature
> sequences respectively. Then it combines them into the temporal motion prior.
> In this way, it can strengthen the ability to express features in the temporal
> motion dimension. Since data representation in non-Euclidean space has been
> proved to effectively capture hierarchical relationships in real-world datasets
> (especially in hyperbolic space), we further design a hyperbolic space
> optimization learning strategy. This strategy uses the temporal motion prior
> information to assist learning, and uses 3D pose and pose motion information
> respectively in the hyperbolic space to optimize and learn the mesh features.
> Then, we combine the optimized results to get an accurate and smooth human
> mesh. Besides, to make the optimization learning process of human meshes in
> hyperbolic space stable and effective, we propose a hyperbolic mesh
> optimization loss. Extensive experimental results on large publicly available
> datasets indicate superiority in comparison with most state-of-the-art.


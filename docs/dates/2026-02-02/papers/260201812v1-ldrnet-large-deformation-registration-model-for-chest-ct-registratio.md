---
layout: default
title: LDRNet: Large Deformation Registration Model for Chest CT Registration
---

# LDRNet: Large Deformation Registration Model for Chest CT Registration
**arXiv**：[2602.01812v1](https://arxiv.org/abs/2602.01812) · [PDF](https://arxiv.org/pdf/2602.01812.pdf)  
**作者**：Cheng Wang, Qiyu Gao, Fandong Zhang, Shu Zhang, Yizhou Yu  

**一句话要点**：提出LDRNet用于胸部CT大变形配准，通过粗到精策略提升性能与速度。

**关键词**：医学图像配准, 胸部CT, 大变形配准, 深度学习, 粗到精策略, 无监督学习

## 3 点简述
- 核心问题：胸部CT配准面临大变形、复杂背景和区域重叠，现有方法多针对脑部图像。
- 方法要点：采用粗到精配准流程，引入细化块优化不同分辨率配准场，刚性块学习高层特征变换矩阵。
- 实验或效果：在私有和公开数据集SegTHOR上评估，相比传统方法和深度学习模型VoxelMorph等，实现更优性能与更快速度。

## 摘要（原文）

> Most of the deep learning based medical image registration algorithms focus on brain image registration tasks.Compared with brain registration, the chest CT registration has larger deformation, more complex background and region over-lap. In this paper, we propose a fast unsupervised deep learning method, LDRNet, for large deformation image registration of chest CT images. We first predict a coarse resolution registration field, then refine it from coarse to fine. We propose two innovative technical components: 1) a refine block that is used to refine the registration field in different resolutions, 2) a rigid block that is used to learn transformation matrix from high-level features. We train and evaluate our model on the private dataset and public dataset SegTHOR. We compare our performance with state-of-the-art traditional registration methods as well as deep learning registration models VoxelMorph, RCN, and LapIRN. The results demonstrate that our model achieves state-of-the-art performance for large deformation images registration and is much faster.


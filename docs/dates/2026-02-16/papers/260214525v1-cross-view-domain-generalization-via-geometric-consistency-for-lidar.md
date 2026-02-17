---
layout: default
title: Cross-view Domain Generalization via Geometric Consistency for LiDAR Semantic Segmentation
---

# Cross-view Domain Generalization via Geometric Consistency for LiDAR Semantic Segmentation
**arXiv**：[2602.14525v1](https://arxiv.org/abs/2602.14525) · [PDF](https://arxiv.org/pdf/2602.14525.pdf)  
**作者**：Jindong Zhao, Yuan Gao, Yang Xia, Sheng Nie, Jun Yue, Weiwei Sun, Shaobo Xia  

**一句话要点**：提出CVGC框架，通过几何一致性增强跨视图域泛化能力，解决LiDAR语义分割中的视角差异问题。

**关键词**：LiDAR语义分割, 域泛化, 跨视图学习, 几何一致性, 点云增强

## 3 点简述
- 核心问题：现有方法在跨视图场景中因视角依赖的结构不完整性和点密度不均而泛化能力受限。
- 方法要点：引入跨视图几何增强模块建模视角变化，并通过几何一致性模块强制语义和占用预测的一致性。
- 实验或效果：在六个公开数据集上验证，CVGC在从单一源域泛化到多目标域时优于现有方法。

## 摘要（原文）

> Domain-generalized LiDAR semantic segmentation (LSS) seeks to train models on source-domain point clouds that generalize reliably to multiple unseen target domains, which is essential for real-world LiDAR applications. However, existing approaches assume similar acquisition views (e.g., vehicle-mounted) and struggle in cross-view scenarios, where observations differ substantially due to viewpoint-dependent structural incompleteness and non-uniform point density. Accordingly, we formulate cross-view domain generalization for LiDAR semantic segmentation and propose a novel framework, termed CVGC (Cross-View Geometric Consistency). Specifically, we introduce a cross-view geometric augmentation module that models viewpoint-induced variations in visibility and sampling density, generating multiple cross-view observations of the same scene. Subsequently, a geometric consistency module enforces consistent semantic and occupancy predictions across geometrically augmented point clouds of the same scene. Extensive experiments on six public LiDAR datasets establish the first systematic evaluation of cross-view domain generalization for LiDAR semantic segmentation, demonstrating that CVGC consistently outperforms state-of-the-art methods when generalizing from a single source domain to multiple target domains with heterogeneous acquisition viewpoints. The source code will be publicly available at https://github.com/KintomZi/CVGC-DG


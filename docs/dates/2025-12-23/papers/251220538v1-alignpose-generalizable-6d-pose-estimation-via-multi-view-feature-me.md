---
layout: default
title: AlignPose: Generalizable 6D Pose Estimation via Multi-view Feature-metric Alignment
---

# AlignPose: Generalizable 6D Pose Estimation via Multi-view Feature-metric Alignment
**arXiv**：[2512.20538v1](https://arxiv.org/abs/2512.20538) · [PDF](https://arxiv.org/pdf/2512.20538.pdf)  
**作者**：Anna Šárová Mikeštíková, Médéric Fourmy, Martin Cífka, Josef Sivic, Vladimir Petrik  

**一句话要点**：提出AlignPose，通过多视角特征度量对齐实现泛化性6D姿态估计

**关键词**：6D姿态估计, 多视角对齐, 特征度量细化, 泛化性, RGB图像, BOP基准

## 3 点简述
- 单视角RGB姿态估计受深度模糊、遮挡限制，多视角方法可解决但泛化性不足
- 核心是多视角特征度量细化，优化一致世界坐标系姿态以最小化特征差异
- 在BOP基准测试中，于工业数据集上优于现有方法，未知泛化性细节

## 摘要（原文）

> Single-view RGB model-based object pose estimation methods achieve strong generalization but are fundamentally limited by depth ambiguity, clutter, and occlusions. Multi-view pose estimation methods have the potential to solve these issues, but existing works rely on precise single-view pose estimates or lack generalization to unseen objects. We address these challenges via the following three contributions. First, we introduce AlignPose, a 6D object pose estimation method that aggregates information from multiple extrinsically calibrated RGB views and does not require any object-specific training or symmetry annotation. Second, the key component of this approach is a new multi-view feature-metric refinement specifically designed for object pose. It optimizes a single, consistent world-frame object pose minimizing the feature discrepancy between on-the-fly rendered object features and observed image features across all views simultaneously. Third, we report extensive experiments on four datasets (YCB-V, T-LESS, ITODD-MV, HouseCat6D) using the BOP benchmark evaluation and show that AlignPose outperforms other published methods, especially on challenging industrial datasets where multiple views are readily available in practice.


---
layout: default
title: AHAP: Reconstructing Arbitrary Humans from Arbitrary Perspectives with Geometric Priors
---

# AHAP: Reconstructing Arbitrary Humans from Arbitrary Perspectives with Geometric Priors
**arXiv**：[2602.23951v1](https://arxiv.org/abs/2602.23951) · [PDF](https://arxiv.org/pdf/2602.23951.pdf)  
**作者**：Xiaozhen Qiao, Wenjia Wang, Zhiyuan Zhao, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li  

**一句话要点**：提出AHAP框架，无需相机标定从任意视角重建任意人体

**关键词**：多视角人体重建, 相机标定无关, 几何先验, SMPL预测, 身份关联

## 3 点简述
- 核心问题：多视角人体重建依赖预标定，限制实际应用。
- 方法要点：融合多视角几何，通过身份关联模块和头部网络预测SMPL参数。
- 实验效果：在EgoHumans和EgoExo4D上实现高效重建，速度提升180倍。

## 摘要（原文）

> Reconstructing 3D humans from images captured at multiple perspectives typically requires pre-calibration, like using checkerboards or MVS algorithms, which limits scalability and applicability in diverse real-world scenarios. In this work, we present \textbf{AHAP} (Reconstructing \textbf{A}rbitrary \textbf{H}umans from \textbf{A}rbitrary \textbf{P}erspectives), a feed-forward framework for reconstructing arbitrary humans from arbitrary camera perspectives without requiring camera calibration. Our core lies in the effective fusion of multi-view geometry to assist human association, reconstruction and localization. Specifically, we use a Cross-View Identity Association module through learnable person queries and soft assignment, supervised by contrastive learning to resolve cross-view human identity association. A Human Head fuses cross-view features and scene context for SMPL prediction, guided by cross-view reprojection losses to enforce body pose consistency. Additionally, multi-view geometry eliminates the depth ambiguity inherent in monocular methods, providing more precise 3D human localization through multi-view triangulation. Experiments on EgoHumans and EgoExo4D demonstrate that AHAP achieves competitive performance on both world-space human reconstruction and camera pose estimation, while being 180$\times$ faster than optimization-based approaches.


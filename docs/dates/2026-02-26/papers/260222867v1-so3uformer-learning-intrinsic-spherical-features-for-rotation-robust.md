---
layout: default
title: SO3UFormer: Learning Intrinsic Spherical Features for Rotation-Robust Panoramic Segmentation
---

# SO3UFormer: Learning Intrinsic Spherical Features for Rotation-Robust Panoramic Segmentation
**arXiv**：[2602.22867v1](https://arxiv.org/abs/2602.22867) · [PDF](https://arxiv.org/pdf/2602.22867.pdf)  
**作者**：Qinfeng Zhu, Yunxi Jiang, Lei Fan  

**一句话要点**：提出SO3UFormer以解决全景分割在相机旋转下的性能崩溃问题

**关键词**：全景语义分割, 旋转鲁棒性, 球面Transformer, 内在特征学习, SO(3)一致性, 几何建模

## 3 点简述
- 全景分割模型依赖重力对齐假设，但实际相机运动导致旋转偏差，使现有方法性能下降。
- SO3UFormer通过移除绝对纬度编码、设计球面注意力与相对位置机制，学习内在球面特征。
- 在Pose35数据集上，SO3UFormer在±35°旋转下达到72.03 mIoU，全SO(3)旋转下保持70.67 mIoU，表现稳定。

## 摘要（原文）

> Panoramic semantic segmentation models are typically trained under a strict gravity-aligned assumption. However, real-world captures often deviate from this canonical orientation due to unconstrained camera motions, such as the rotational jitter of handheld devices or the dynamic attitude shifts of aerial platforms. This discrepancy causes standard spherical Transformers to overfit global latitude cues, leading to performance collapse under 3D reorientations. To address this, we introduce SO3UFormer, a rotation-robust architecture designed to learn intrinsic spherical features that are less sensitive to the underlying coordinate frame. Our approach rests on three geometric pillars: (1) an intrinsic feature formulation that decouples the representation from the gravity vector by removing absolute latitude encoding; (2) quadrature-consistent spherical attention that accounts for non-uniform sampling densities; and (3) a gauge-aware relative positional mechanism that encodes local angular geometry using tangent-plane projected angles and discrete gauge pooling, avoiding reliance on global axes. We further use index-based spherical resampling together with a logit-level SO(3)-consistency regularizer during training. To rigorously benchmark robustness, we introduce Pose35, a dataset variant of Stanford2D3D perturbed by random rotations within $\pm 35^\circ$. Under the extreme test of arbitrary full SO(3) rotations, existing SOTAs fail catastrophically: the baseline SphereUFormer drops from 67.53 mIoU to 25.26 mIoU. In contrast, SO3UFormer demonstrates remarkable stability, achieving 72.03 mIoU on Pose35 and retaining 70.67 mIoU under full SO(3) rotations.


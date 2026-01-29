---
layout: default
title: GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction
---

# GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction
**arXiv**：[2601.20331v1](https://arxiv.org/abs/2601.20331) · [PDF](https://arxiv.org/pdf/2601.20331.pdf)  
**作者**：Mai Su, Qihan Yu, Zhongtao Wang, Yilong Li, Chengwei Pan, Yisong Chen, Guoping Wang  

**一句话要点**：提出高斯可见性感知多视角几何约束与渐进四叉树校准单目深度约束，以提升基于高斯泼溅的表面重建精度。

**关键词**：高斯泼溅, 表面重建, 多视角几何, 深度先验, 可见性感知, 渐进校准

## 3 点简述
- 核心问题：现有方法在大几何差异下多视角约束不可靠，单目深度先验存在尺度模糊和局部不一致，导致高斯深度监督不准确。
- 方法要点：引入高斯可见性感知多视角几何一致性约束，聚合共享高斯基元可见性；提出渐进四叉树校准单目深度约束，从粗到细进行块状仿射校准。
- 实验或效果：在DTU和TNT数据集上实验，几何精度优于先前基于高斯和隐式表面重建方法。

## 摘要（原文）

> 3D Gaussian Splatting enables efficient optimization and high-quality rendering, yet accurate surface reconstruction remains challenging. Prior methods improve surface reconstruction by refining Gaussian depth estimates, either via multi-view geometric consistency or through monocular depth priors. However, multi-view constraints become unreliable under large geometric discrepancies, while monocular priors suffer from scale ambiguity and local inconsistency, ultimately leading to inaccurate Gaussian depth supervision. To address these limitations, we introduce a Gaussian visibility-aware multi-view geometric consistency constraint that aggregates the visibility of shared Gaussian primitives across views, enabling more accurate and stable geometric supervision. In addition, we propose a progressive quadtree-calibrated Monocular depth constraint that performs block-wise affine calibration from coarse to fine spatial scales, mitigating the scale ambiguity of depth priors while preserving fine-grained surface details. Extensive experiments on DTU and TNT datasets demonstrate consistent improvements in geometric accuracy over prior Gaussian-based and implicit surface reconstruction methods. Codes are available at an anonymous repository: https://github.com/GVGScode/GVGS.


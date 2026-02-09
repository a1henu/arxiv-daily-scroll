---
layout: default
title: GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification
---

# GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification
**arXiv**：[2602.06830v1](https://arxiv.org/abs/2602.06830) · [PDF](https://arxiv.org/pdf/2602.06830.pdf)  
**作者**：Soonbin Lee, Yeong-Gyu Kim, Simon Sasse, Tomas M. Borges, Yago Sanchez, Eun-Seok Ryu, Thomas Schierl, Cornelius Hellge  

**一句话要点**：提出GaussianPOP框架，通过误差量化实现紧凑3D高斯溅射的简化

**关键词**：3D高斯溅射, 模型简化, 误差量化, 渲染保真度, 剪枝算法, 紧凑模型

## 3 点简述
- 现有简化方法依赖重要性评分，未基于视觉误差，导致紧凑性与渲染保真度权衡不佳
- 基于渲染方程推导新误差准则，高效算法单次前向计算误差，支持训练中剪枝和训练后简化
- 实验表明在两种场景下优于现有方法，实现更优的模型紧凑性与高质量渲染平衡

## 摘要（原文）

> Existing 3D Gaussian Splatting simplification methods commonly use importance scores, such as blending weights or sensitivity, to identify redundant Gaussians. However, these scores are not driven by visual error metrics, often leading to suboptimal trade-offs between compactness and rendering fidelity. We present GaussianPOP, a principled simplification framework based on analytical Gaussian error quantification. Our key contribution is a novel error criterion, derived directly from the 3DGS rendering equation, that precisely measures each Gaussian's contribution to the rendered image. By introducing a highly efficient algorithm, our framework enables practical error calculation in a single forward pass. The framework is both accurate and flexible, supporting on-training pruning as well as post-training simplification via iterative error re-quantification for improved stability. Experimental results show that our method consistently outperforms existing state-of-the-art pruning methods across both application scenarios, achieving a superior trade-off between model compactness and high rendering quality.


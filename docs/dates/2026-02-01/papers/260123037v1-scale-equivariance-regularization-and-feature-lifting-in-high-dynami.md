---
layout: default
title: Scale Equivariance Regularization and Feature Lifting in High Dynamic Range Modulo Imaging
---

# Scale Equivariance Regularization and Feature Lifting in High Dynamic Range Modulo Imaging
**arXiv**：[2601.23037v1](https://arxiv.org/abs/2601.23037) · [PDF](https://arxiv.org/pdf/2601.23037.pdf)  
**作者**：Brayan Monroy, Jorge Bacca  

**一句话要点**：提出基于尺度等变正则化和特征提升的HDR模数成像恢复框架，以区分真实结构与包裹伪影。

**关键词**：高动态范围成像, 模数成像, 尺度等变性, 特征提升, 图像恢复, 深度学习

## 3 点简述
- 核心问题：模数成像中自然边缘与人工包裹不连续性难以区分，导致HDR重建不准确。
- 方法要点：结合尺度等变正则化确保曝光变化一致性，以及特征提升输入设计增强网络区分能力。
- 实验或效果：在感知和线性HDR质量指标上实现先进性能，提升重建准确性。

## 摘要（原文）

> Modulo imaging enables high dynamic range (HDR) acquisition by cyclically wrapping saturated intensities, but accurate reconstruction remains challenging due to ambiguities between natural image edges and artificial wrap discontinuities. This work proposes a learning-based HDR restoration framework that incorporates two key strategies: (i) a scale-equivariant regularization that enforces consistency under exposure variations, and (ii) a feature lifting input design combining the raw modulo image, wrapped finite differences, and a closed-form initialization. Together, these components enhance the network's ability to distinguish true structure from wrapping artifacts, yielding state-of-the-art performance across perceptual and linear HDR quality metrics.


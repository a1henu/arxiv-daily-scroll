---
layout: default
title: Latent attention on masked patches for flow reconstruction
---

# Latent attention on masked patches for flow reconstruction
**arXiv**：[2603.02028v1](https://arxiv.org/abs/2603.02028) · [PDF](https://arxiv.org/pdf/2603.02028.pdf)  
**作者**：Ben Eze, Luca Magri, Andrea Nóvoa  

**一句话要点**：提出LAMP模型，基于掩码补丁的潜在注意力，用于流体动力学中的掩码流场重建。

**关键词**：掩码流场重建, 视觉变换器, 流体动力学, 潜在注意力, 线性回归, 传感器布局优化

## 3 点简述
- 核心问题：视觉变换器在流体动力学等科学领域应用有限，需高效重建掩码流场。
- 方法要点：采用分块、降维和单层变换器，通过闭式线性回归训练，实现可解释重建。
- 实验或效果：在二维非定常尾流中，LAMP能从90%掩码和噪声输入中准确重建，并优化传感器布局。

## 摘要（原文）

> Vision transformers have demonstrated outstanding performance on image generation applications, but their adoption in scientific disciplines, like fluid dynamics, has been limited. We introduce the Latent Attention on Masked Patches (LAMP) model, an interpretable regression-based modified vision transformer designed for masked flow reconstruction. LAMP follows a three-fold strategy: (i) partition of each flow snapshot into patches, (ii) dimensionality reduction of each patch via patch-wise proper orthogonal decomposition, and (iii) reconstruction of the full field from a masked input using a single-layer transformer trained via closed-form linear regression. We test the method on two canonical 2D unsteady wakes: a wake past a bluff body, and a chaotic wake past a flat plate. We show that the LAMP accurately reconstructs the full flow field from a 90\%-masked and noisy input, across signal-to-noise ratios between 10 and 30\,dB. Incorporating nonlinear measurement states can reduce the prediction error by up to an order of magnitude. The learned attention matrix yields physically interpretable multi-fidelity optimal sensor-placement maps. The modularity of the framework enables nonlinear compression and deep attention blocks, thereby providing an efficient baseline for nonlinear and high-dimensional masked flow reconstruction.


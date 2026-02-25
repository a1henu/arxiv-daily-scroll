---
layout: default
title: Mask-HybridGNet: Graph-based segmentation with emergent anatomical correspondence from pixel-level supervision
---

# Mask-HybridGNet: Graph-based segmentation with emergent anatomical correspondence from pixel-level supervision
**arXiv**：[2602.21179v1](https://arxiv.org/abs/2602.21179) · [PDF](https://arxiv.org/pdf/2602.21179.pdf)  
**作者**：Nicolás Gaggion, Maria J. Ledesma-Carbayo, Stergios Christodoulidis, Maria Vakalopoulou, Enzo Ferrante  

**一句话要点**：提出Mask-HybridGNet框架，利用像素级监督训练基于图的医学图像分割模型，无需手动标注地标。

**关键词**：医学图像分割, 图神经网络, 像素级监督, 解剖对应, 可微分光栅化, 边界图

## 3 点简述
- 核心问题：基于图的医学图像分割需手动标注地标，但临床数据中此类标注稀缺。
- 方法要点：结合Chamfer距离监督和边缘正则化，通过可微分光栅化对齐变长边界与固定地标预测。
- 实验或效果：在多种医学影像上实现竞争性分割性能，并隐式学习解剖对应关系，支持形态分析。

## 摘要（原文）

> Graph-based medical image segmentation represents anatomical structures using boundary graphs, providing fixed-topology landmarks and inherent population-level correspondences. However, their clinical adoption has been hindered by a major requirement: training datasets with manually annotated landmarks that maintain point-to-point correspondences across patients rarely exist in practice. We introduce Mask-HybridGNet, a framework that trains graph-based models directly using standard pixel-wise masks, eliminating the need for manual landmark annotations. Our approach aligns variable-length ground truth boundaries with fixed-length landmark predictions by combining Chamfer distance supervision and edge-based regularization to ensure local smoothness and regular landmark distribution, further refined via differentiable rasterization. A significant emergent property of this framework is that predicted landmark positions become consistently associated with specific anatomical locations across patients without explicit correspondence supervision. This implicit atlas learning enables temporal tracking, cross-slice reconstruction, and morphological population analyses. Beyond direct segmentation, Mask-HybridGNet can extract correspondences from existing segmentation masks, allowing it to generate stable anatomical atlases from any high-quality pixel-based model. Experiments across chest radiography, cardiac ultrasound, cardiac MRI, and fetal imaging demonstrate that our model achieves competitive results against state-of-the-art pixel-based methods, while ensuring anatomical plausibility by enforcing boundary connectivity through a fixed graph adjacency matrix. This framework leverages the vast availability of standard segmentation masks to build structured models that maintain topological integrity and provide implicit correspondences.


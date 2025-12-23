---
layout: default
title: Initialization of a Polyharmonic Cascade, Launch and Testing
---

# Initialization of a Polyharmonic Cascade, Launch and Testing
**arXiv**：[2512.19524v1](https://arxiv.org/abs/2512.19524) · [PDF](https://arxiv.org/pdf/2512.19524.pdf)  
**作者**：Yuriy N. Bakhvalov  

**一句话要点**：提出基于超八面体对称星座的初始化方法，以稳定训练深层多谐级联网络。

**关键词**：多谐级联网络, 初始化方法, 深层网络训练, GPU优化, 对称星座, 可扩展性

## 3 点简述
- 核心问题：深层多谐级联网络训练不稳定，传统方法难以处理数百层无跳跃连接的网络。
- 方法要点：采用超八面体对称星座初始化，简化计算为2D操作，提升GPU效率。
- 实验效果：在MNIST、HIGGS和Epsilon数据集上验证了可扩展性和鲁棒性，最高达500层。

## 摘要（原文）

> This paper concludes a series of studies on the polyharmonic cascade, a deep machine learning architecture theoretically derived from indifference principles and the theory of random functions. A universal initialization procedure is proposed, based on symmetric constellations in the form of hyperoctahedra with a central point. This initialization not only ensures stable training of cascades with tens and hundreds of layers (up to 500 layers without skip connections), but also radically simplifies the computations. Scalability and robustness are demonstrated on MNIST (98.3% without convolutions or augmentations), HIGGS (AUC approximately 0.885 on 11M examples), and Epsilon (AUC approximately 0.963 with 2000 features). All linear algebra is reduced to 2D operations and is efficiently executed on GPUs. A public repository and an archived snapshot are provided for full reproducibility.


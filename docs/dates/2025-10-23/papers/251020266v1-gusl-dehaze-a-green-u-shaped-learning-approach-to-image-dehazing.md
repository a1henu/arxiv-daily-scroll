---
layout: default
title: GUSL-Dehaze: A Green U-Shaped Learning Approach to Image Dehazing
---

# GUSL-Dehaze: A Green U-Shaped Learning Approach to Image Dehazing
**arXiv**：[2510.20266v1](https://arxiv.org/abs/2510.20266) · [PDF](https://arxiv.org/pdf/2510.20266.pdf)  
**作者**：Mahtab Movaheddrad, Laurence Palmer, C. -C. Jay Kuo  

**一句话要点**：提出GUSL-Dehaze方法以解决图像去雾任务中的高计算成本问题

**关键词**：图像去雾, 绿色学习, U形架构, 物理模型, 特征工程, 轻量模型

## 3 点简述
- 核心问题：传统深度学习方法计算成本高，不适合资源受限设备
- 方法要点：结合物理模型与绿色学习框架，避免深度学习，使用U形架构
- 实验或效果：参数显著减少，性能与先进模型相当，保持数学可解释性

## 摘要（原文）

> Image dehazing is a restoration task that aims to recover a clear image from
> a single hazy input. Traditional approaches rely on statistical priors and the
> physics-based atmospheric scattering model to reconstruct the haze-free image.
> While recent state-of-the-art methods are predominantly based on deep learning
> architectures, these models often involve high computational costs and large
> parameter sizes, making them unsuitable for resource-constrained devices. In
> this work, we propose GUSL-Dehaze, a Green U-Shaped Learning approach to image
> dehazing. Our method integrates a physics-based model with a green learning
> (GL) framework, offering a lightweight, transparent alternative to conventional
> deep learning techniques. Unlike neural network-based solutions, GUSL-Dehaze
> completely avoids deep learning. Instead, we begin with an initial dehazing
> step using a modified Dark Channel Prior (DCP), which is followed by a green
> learning pipeline implemented through a U-shaped architecture. This
> architecture employs unsupervised representation learning for effective feature
> extraction, together with feature-engineering techniques such as the Relevant
> Feature Test (RFT) and the Least-Squares Normal Transform (LNT) to maintain a
> compact model size. Finally, the dehazed image is obtained via a transparent
> supervised learning strategy. GUSL-Dehaze significantly reduces parameter count
> while ensuring mathematical interpretability and achieving performance on par
> with state-of-the-art deep learning models.


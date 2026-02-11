---
layout: default
title: Fully Differentiable Bidirectional Dual-Task Synergistic Learning for Semi-Supervised 3D Medical Image Segmentation
---

# Fully Differentiable Bidirectional Dual-Task Synergistic Learning for Semi-Supervised 3D Medical Image Segmentation
**arXiv**：[2602.09378v1](https://arxiv.org/abs/2602.09378) · [PDF](https://arxiv.org/pdf/2602.09378.pdf)  
**作者**：Jun Li  

**一句话要点**：提出全可微双向双任务协同学习框架以解决半监督3D医学图像分割中双向交互不足的问题

**关键词**：半监督学习, 3D医学图像分割, 双任务协同学习, 全可微框架, 一致性正则化, 伪监督学习

## 3 点简述
- 核心问题：现有双任务协同学习方法局限于单向交互，无法充分利用在线双向跨任务协作的潜力
- 方法要点：设计全可微框架，无缝整合监督学习、一致性正则化、伪监督学习和不确定性估计四个关键组件
- 实验或效果：在两个基准数据集上实现最先进性能，为统一半监督学习框架设计提供新见解

## 摘要（原文）

> Semi-supervised learning relaxes the need of large pixel-wise labeled datasets for image segmentation by leveraging unlabeled data. The scarcity of high-quality labeled data remains a major challenge in medical image analysis due to the high annotation costs and the need for specialized clinical expertise. Semi-supervised learning has demonstrated significant potential in addressing this bottleneck, with pseudo-labeling and consistency regularization emerging as two predominant paradigms. Dual-task collaborative learning, an emerging consistency-aware paradigm, seeks to derive supplementary supervision by establishing prediction consistency between related tasks. However, current methodologies are limited to unidirectional interaction mechanisms (typically regression-to-segmentation), as segmentation results can only be transformed into regression outputs in an offline manner, thereby failing to fully exploit the potential benefits of online bidirectional cross-task collaboration. Thus, we propose a fully Differentiable Bidirectional Synergistic Learning (DBiSL) framework, which seamlessly integrates and enhances four critical SSL components: supervised learning, consistency regularization, pseudo-supervised learning, and uncertainty estimation. Experiments on two benchmark datasets demonstrate our method's state-of-the-art performance. Beyond technical contributions, this work provides new insights into unified SSL framework design and establishes a new architectural foundation for dual-task-driven SSL, while offering a generic multitask learning framework applicable to broader computer vision applications. The code will be released on github upon acceptance.


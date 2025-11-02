---
layout: default
title: Exploring Object-Aware Attention Guided Frame Association for RGB-D SLAM
---

# Exploring Object-Aware Attention Guided Frame Association for RGB-D SLAM
**arXiv**：[2510.26131v1](https://arxiv.org/abs/2510.26131) · [PDF](https://arxiv.org/pdf/2510.26131.pdf)  
**作者**：Ali Caglayan, Nevrez Imamoglu, Oguzhan Guclu, Ali Osman Serhatoglu, Ahmet Burak Can, Ryosuke Nakamura  

**一句话要点**：提出对象感知注意力引导的帧关联方法以改进RGB-D室内SLAM性能

**关键词**：RGB-D SLAM, 注意力机制, 帧关联, 对象感知, 网络梯度, CNN特征

## 3 点简述
- 核心问题：RGB-D SLAM中CNN表示缺乏显式语义对象理解，影响帧关联准确性。
- 方法要点：集成网络梯度注意力与CNN特征，增强对象位置的空间注意力表示。
- 实验或效果：实验显示在大环境中性能优于基线方法，提升帧关联效果。

## 摘要（原文）

> Attention models have recently emerged as a powerful approach, demonstrating
> significant progress in various fields. Visualization techniques, such as class
> activation mapping, provide visual insights into the reasoning of convolutional
> neural networks (CNNs). Using network gradients, it is possible to identify
> regions where the network pays attention during image recognition tasks.
> Furthermore, these gradients can be combined with CNN features to localize more
> generalizable, task-specific attentive (salient) regions within scenes.
> However, explicit use of this gradient-based attention information integrated
> directly into CNN representations for semantic object understanding remains
> limited. Such integration is particularly beneficial for visual tasks like
> simultaneous localization and mapping (SLAM), where CNN representations
> enriched with spatially attentive object locations can enhance performance. In
> this work, we propose utilizing task-specific network attention for RGB-D
> indoor SLAM. Specifically, we integrate layer-wise attention information
> derived from network gradients with CNN feature representations to improve
> frame association performance. Experimental results indicate improved
> performance compared to baseline methods, particularly for large environments.


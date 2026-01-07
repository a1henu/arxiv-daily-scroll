---
layout: default
title: Towards Agnostic and Holistic Universal Image Segmentation with Bit Diffusion
---

# Towards Agnostic and Holistic Universal Image Segmentation with Bit Diffusion
**arXiv**：[2601.02881v1](https://arxiv.org/abs/2601.02881) · [PDF](https://arxiv.org/pdf/2601.02881.pdf)  
**作者**：Jakob Lønborg Christensen, Morten Rieger Hannemose, Anders Bjorholm Dahl, Vedrana Andersen Dahl  

**一句话要点**：提出基于扩散的通用图像分割框架，实现不依赖掩码的全面分割。

**关键词**：通用图像分割, 扩散模型, 位置感知调色板, 2D格雷码排序, 模糊性建模

## 3 点简述
- 核心问题：现有通用分割依赖掩码框架，缺乏整体性和模糊性建模能力。
- 方法要点：采用扩散模型，引入位置感知调色板和2D格雷码排序，优化激活函数和损失权重。
- 实验或效果：模型缩小与领先掩码架构的性能差距，支持原则性模糊建模，但未超越现有最佳。

## 摘要（原文）

> This paper introduces a diffusion-based framework for universal image segmentation, making agnostic segmentation possible without depending on mask-based frameworks and instead predicting the full segmentation in a holistic manner. We present several key adaptations to diffusion models, which are important in this discrete setting. Notably, we show that a location-aware palette with our 2D gray code ordering improves performance. Adding a final tanh activation function is crucial for discrete data. On optimizing diffusion parameters, the sigmoid loss weighting consistently outperforms alternatives, regardless of the prediction type used, and we settle on x-prediction. While our current model does not yet surpass leading mask-based architectures, it narrows the performance gap and introduces unique capabilities, such as principled ambiguity modeling, that these models lack. All models were trained from scratch, and we believe that combining our proposed improvements with large-scale pretraining or promptable conditioning could lead to competitive models.


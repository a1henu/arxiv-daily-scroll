---
layout: default
title: Image augmentation with invertible networks in interactive satellite image change detection
---

# Image augmentation with invertible networks in interactive satellite image change detection
**arXiv**：[2510.18660v1](https://arxiv.org/abs/2510.18660) · [PDF](https://arxiv.org/pdf/2510.18660.pdf)  
**作者**：Hichem Sahbi  

**一句话要点**：提出可逆网络增强显示图像，用于交互式卫星图像变化检测

**关键词**：卫星图像变化检测, 可逆网络, 数据增强, 主动学习, 交互式系统

## 3 点简述
- 核心问题：卫星图像变化检测中，如何高效利用用户交互优化模型。
- 方法要点：使用可逆网络将图像映射到潜在空间，实现线性数据增强。
- 实验或效果：实验显示，该方法在性能上优于相关现有工作。

## 摘要（原文）

> This paper devises a novel interactive satellite image change detection
> algorithm based on active learning. Our framework employs an iterative process
> that leverages a question-and-answer model. This model queries the oracle
> (user) about the labels of a small subset of images (dubbed as display), and
> based on the oracle's responses, change detection model is dynamically updated.
> The main contribution of our framework resides in a novel invertible network
> that allows augmenting displays, by mapping them from highly nonlinear input
> spaces to latent ones, where augmentation transformations become linear and
> more tractable. The resulting augmented data are afterwards mapped back to the
> input space, and used to retrain more effective change detection criteria in
> the subsequent iterations of active learning. Experimental results demonstrate
> superior performance of our proposed method compared to the related work.


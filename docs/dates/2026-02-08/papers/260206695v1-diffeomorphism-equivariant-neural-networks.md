---
layout: default
title: Diffeomorphism-Equivariant Neural Networks
---

# Diffeomorphism-Equivariant Neural Networks
**arXiv**：[2602.06695v1](https://arxiv.org/abs/2602.06695) · [PDF](https://arxiv.org/pdf/2602.06695.pdf)  
**作者**：Josephine Elisabeth Oettinger, Zakhar Shumaylov, Johannes Bostelmann, Jan Lellmann, Carola-Bibiane Schönlieb  

**一句话要点**：提出基于能量规范化的方法，在预训练神经网络中实现微分同胚等变性，以处理无限维群变换。

**关键词**：微分同胚等变性, 能量规范化, 无限维群, 图像配准, 神经网络泛化

## 3 点简述
- 核心问题：现有等变性方法多针对有限或低维线性群，难以扩展到无限维微分同胚群。
- 方法要点：将等变性转化为优化问题，利用可微图像配准工具实现能量规范化诱导等变性。
- 实验或效果：在分割和分类任务中验证近似等变性，无需大量数据增强或重训练即可泛化到未见变换。

## 摘要（原文）

> Incorporating group symmetries via equivariance into neural networks has emerged as a robust approach for overcoming the efficiency and data demands of modern deep learning. While most existing approaches, such as group convolutions and averaging-based methods, focus on compact, finite, or low-dimensional groups with linear actions, this work explores how equivariance can be extended to infinite-dimensional groups. We propose a strategy designed to induce diffeomorphism equivariance in pre-trained neural networks via energy-based canonicalisation. Formulating equivariance as an optimisation problem allows us to access the rich toolbox of already established differentiable image registration methods. Empirical results on segmentation and classification tasks confirm that our approach achieves approximate equivariance and generalises to unseen transformations without relying on extensive data augmentation or retraining.


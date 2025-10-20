---
layout: default
title: Dissecting Mahalanobis: How Feature Geometry and Normalization Shape OOD Detection
---

# Dissecting Mahalanobis: How Feature Geometry and Normalization Shape OOD Detection
**arXiv**：[2510.15202v1](https://arxiv.org/abs/2510.15202) · [PDF](https://arxiv.org/pdf/2510.15202.pdf)  
**作者**：Denis Janiak, Jakub Binkowski, Tomasz Kajdanowicz  

**一句话要点**：提出径向缩放L2归一化以改进分布外检测性能

**关键词**：分布外检测, Mahalanobis距离, 特征几何, 归一化方法, 深度学习可靠性

## 3 点简述
- 核心问题：Mahalanobis距离方法在分布外检测中可靠性不足，受特征几何和归一化影响
- 方法要点：定义理想特征几何，使用谱和本征维度指标预测性能，提出径向缩放L2归一化
- 实验或效果：通过多模型和数据集实证，归一化方法显著提升分布外检测性能

## 摘要（原文）

> Out-of-distribution (OOD) detection is critical for the reliable deployment
> of deep learning models. hile Mahalanobis distance methods are widely used, the
> impact of representation geometry and normalization on their performance is not
> fully understood, which may limit their downstream application. To address this
> gap, we conducted a comprehensive empirical study across diverse image
> foundation models, datasets, and distance normalization schemes. First, our
> analysis shows that Mahalanobis-based methods aren't universally reliable.
> Second, we define the ideal geometry for data representations and demonstrate
> that spectral and intrinsic-dimensionality metrics can accurately predict a
> model's OOD performance. Finally, we analyze how normalization impacts OOD
> performance. Building upon these studies, we propose radially scaled $\ell_2$
> normalization, a method that generalizes the standard $\ell_2$ normalization
> recently applied to Mahalanobis-based OOD detection. Our approach introduces a
> tunable parameter to directly control the radial geometry of the feature space,
> systematically contracting or expanding representations to significantly
> improve OOD detection performance. By bridging the gap between representation
> geometry, normalization, and OOD performance, our findings offer new insights
> into the design of more effective and reliable deep learning models.


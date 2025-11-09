---
layout: default
title: Room Envelopes: A Synthetic Dataset for Indoor Layout Reconstruction from Images
---

# Room Envelopes: A Synthetic Dataset for Indoor Layout Reconstruction from Images
**arXiv**：[2511.03970v1](https://arxiv.org/abs/2511.03970) · [PDF](https://arxiv.org/pdf/2511.03970.pdf)  
**作者**：Sam Bahrami, Dylan Campbell  

**一句话要点**：提出Room Envelopes合成数据集以支持室内布局重建研究

**关键词**：室内场景重建, 合成数据集, 单目几何估计, 布局预测, 点图监督

## 3 点简述
- 核心问题：现有场景重建方法无法恢复被遮挡的结构表面，导致重建不完整。
- 方法要点：提供RGB图像和两个点图，分别表示可见表面和移除家具后的结构布局。
- 实验或效果：支持前馈单目几何估计器直接监督，预测场景范围和物体形状位置。

## 摘要（原文）

> Modern scene reconstruction methods are able to accurately recover 3D
> surfaces that are visible in one or more images. However, this leads to
> incomplete reconstructions, missing all occluded surfaces. While much progress
> has been made on reconstructing entire objects given partial observations using
> generative models, the structural elements of a scene, like the walls, floors
> and ceilings, have received less attention. We argue that these scene elements
> should be relatively easy to predict, since they are typically planar,
> repetitive and simple, and so less costly approaches may be suitable. In this
> work, we present a synthetic dataset -- Room Envelopes -- that facilitates
> progress on this task by providing a set of RGB images and two associated
> pointmaps for each image: one capturing the visible surface and one capturing
> the first surface once fittings and fixtures are removed, that is, the
> structural layout. As we show, this enables direct supervision for feed-forward
> monocular geometry estimators that predict both the first visible surface and
> the first layout surface. This confers an understanding of the scene's extent,
> as well as the shape and location of its objects.


---
layout: default
title: StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion
---

# StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion
**arXiv**：[2512.13147v1](https://arxiv.org/abs/2512.13147) · [PDF](https://arxiv.org/pdf/2512.13147.pdf)  
**作者**：Sangmin Hong, Suyoung Lee, Kyoung Mu Lee  

**一句话要点**：提出StarryGazer框架，利用单目深度估计模型实现领域无关的单深度图像补全

**关键词**：深度补全, 单目深度估计, 无监督学习, 领域无关, 稀疏深度图, 图像合成

## 3 点简述
- 核心问题：现有无监督深度补全方法依赖辅助数据，单目深度估计模型无法直接结合稀疏深度图
- 方法要点：使用预训练单目深度估计模型生成相对深度图，通过分割和随机缩放合成伪真值对训练细化网络
- 实验或效果：在多个数据集上优于现有无监督方法，有效利用单目深度估计模型并修正误差

## 摘要（原文）

> The problem of depth completion involves predicting a dense depth image from a single sparse depth map and an RGB image. Unsupervised depth completion methods have been proposed for various datasets where ground truth depth data is unavailable and supervised methods cannot be applied. However, these models require auxiliary data to estimate depth values, which is far from real scenarios. Monocular depth estimation (MDE) models can produce a plausible relative depth map from a single image, but there is no work to properly combine the sparse depth map with MDE for depth completion; a simple affine transformation to the depth map will yield a high error since MDE are inaccurate at estimating depth difference between objects. We introduce StarryGazer, a domain-agnostic framework that predicts dense depth images from a single sparse depth image and an RGB image without relying on ground-truth depth by leveraging the power of large MDE models. First, we employ a pre-trained MDE model to produce relative depth images. These images are segmented and randomly rescaled to form synthetic pairs for dense pseudo-ground truth and corresponding sparse depths. A refinement network is trained with the synthetic pairs, incorporating the relative depth maps and RGB images to improve the model's accuracy and robustness. StarryGazer shows superior results over existing unsupervised methods and transformed MDE results on various datasets, demonstrating that our framework exploits the power of MDE models while appropriately fixing errors using sparse depth information.


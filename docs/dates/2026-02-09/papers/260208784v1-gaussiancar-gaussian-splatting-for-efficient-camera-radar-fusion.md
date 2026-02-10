---
layout: default
title: GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion
---

# GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion
**arXiv**：[2602.08784v1](https://arxiv.org/abs/2602.08784) · [PDF](https://arxiv.org/pdf/2602.08784.pdf)  
**作者**：Santiago Montiel-Marín, Miguel Antunes-García, Fabio Sánchez-García, Angel Llamazares, Holger Caesar, Luis M. Bergasa  

**一句话要点**：提出GaussianCaR，利用高斯泼溅实现高效相机-雷达融合，用于自动驾驶BEV分割。

**关键词**：自动驾驶感知, 相机-雷达融合, 高斯泼溅, BEV分割, 视图变换, 多尺度融合

## 3 点简述
- 核心问题：自动驾驶中动态物体和地图元素的鲁棒感知，需融合相机和雷达数据以提升性能。
- 方法要点：采用高斯泼溅作为通用视图变换器，将图像像素和雷达点映射到BEV表示，结合多尺度融合与Transformer解码器。
- 实验或效果：在nuScenes数据集上，BEV分割性能达到或超越SOTA，推理速度提升3.2倍。

## 摘要（原文）

> Robust and accurate perception of dynamic objects and map elements is crucial for autonomous vehicles performing safe navigation in complex traffic scenarios. While vision-only methods have become the de facto standard due to their technical advances, they can benefit from effective and cost-efficient fusion with radar measurements. In this work, we advance fusion methods by repurposing Gaussian Splatting as an efficient universal view transformer that bridges the view disparity gap, mapping both image pixels and radar points into a common Bird's-Eye View (BEV) representation. Our main contribution is GaussianCaR, an end-to-end network for BEV segmentation that, unlike prior BEV fusion methods, leverages Gaussian Splatting to map raw sensor information into latent features for efficient camera-radar fusion. Our architecture combines multi-scale fusion with a transformer decoder to efficiently extract BEV features. Experimental results demonstrate that our approach achieves performance on par with, or even surpassing, the state of the art on BEV segmentation tasks (57.3%, 82.9%, and 50.1% IoU for vehicles, roads, and lane dividers) on the nuScenes dataset, while maintaining a 3.2x faster inference runtime. Code and project page are available online.


---
layout: default
title: Learning Image-based Tree Crown Segmentation from Enhanced Lidar-based Pseudo-labels
---

# Learning Image-based Tree Crown Segmentation from Enhanced Lidar-based Pseudo-labels
**arXiv**：[2602.13022v1](https://arxiv.org/abs/2602.13022) · [PDF](https://arxiv.org/pdf/2602.13022.pdf)  
**作者**：Julius Pesonen, Stefan Rua, Josef Taher, Niko Koivumäki, Xiaowei Yu, Eija Honkavaara  

**一句话要点**：提出基于增强激光雷达伪标签的图像树冠分割方法，以低成本实现高精度个体树冠识别。

**关键词**：树冠分割, 激光雷达伪标签, 深度学习训练, 零样本实例分割, 航空影像分析

## 3 点简述
- 核心问题：航空影像中树冠纹理复杂和重叠导致自动分割困难。
- 方法要点：利用激光雷达数据生成伪标签，并通过SAM 2模型增强以训练深度学习模型。
- 实验或效果：无需人工标注，模型在光学图像分割任务上优于通用领域部署模型。

## 摘要（原文）

> Mapping individual tree crowns is essential for tasks such as maintaining urban tree inventories and monitoring forest health, which help us understand and care for our environment. However, automatically separating the crowns from each other in aerial imagery is challenging due to factors such as the texture and partial tree crown overlaps. In this study, we present a method to train deep learning models that segment and separate individual trees from RGB and multispectral images, using pseudo-labels derived from aerial laser scanning (ALS) data. Our study shows that the ALS-derived pseudo-labels can be enhanced using a zero-shot instance segmentation model, Segment Anything Model 2 (SAM 2). Our method offers a way to obtain domain-specific training annotations for optical image-based models without any manual annotation cost, leading to segmentation models which outperform any available models which have been targeted for general domain deployment on the same task.


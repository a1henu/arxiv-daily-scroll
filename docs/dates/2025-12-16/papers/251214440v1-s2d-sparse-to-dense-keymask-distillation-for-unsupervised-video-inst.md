---
layout: default
title: S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation
---

# S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation
**arXiv**：[2512.14440v1](https://arxiv.org/abs/2512.14440) · [PDF](https://arxiv.org/pdf/2512.14440.pdf)  
**作者**：Leon Sick, Lukas Hoyer, Dominik Engel, Pedro Hermosilla, Timo Ropinski  

**一句话要点**：提出S2D稀疏到稠密关键掩码蒸馏方法，以解决无监督视频实例分割中合成数据运动建模不准确的问题。

**关键词**：无监督视频实例分割, 稀疏到稠密蒸馏, 时序一致性, 关键掩码识别, 真实视频训练

## 3 点简述
- 核心问题：现有方法依赖合成视频数据，无法准确建模真实视频中的运动，如视角变化或相机运动。
- 方法要点：从真实视频的单帧无监督分割出发，利用深度运动先验识别高质量关键掩码，通过稀疏到稠密蒸馏和时序DropLoss训练分割模型。
- 实验或效果：在多个基准测试中，该方法优于当前最先进的无监督视频实例分割模型。

## 摘要（原文）

> In recent years, the state-of-the-art in unsupervised video instance segmentation has heavily relied on synthetic video data, generated from object-centric image datasets such as ImageNet. However, video synthesis by artificially shifting and scaling image instance masks fails to accurately model realistic motion in videos, such as perspective changes, movement by parts of one or multiple instances, or camera motion. To tackle this issue, we propose an unsupervised video instance segmentation model trained exclusively on real video data. We start from unsupervised instance segmentation masks on individual video frames. However, these single-frame segmentations exhibit temporal noise and their quality varies through the video. Therefore, we establish temporal coherence by identifying high-quality keymasks in the video by leveraging deep motion priors. The sparse keymask pseudo-annotations are then used to train a segmentation model for implicit mask propagation, for which we propose a Sparse-To-Dense Distillation approach aided by a Temporal DropLoss. After training the final model on the resulting dense labelset, our approach outperforms the current state-of-the-art across various benchmarks.


---
layout: default
title: Self-Supervised Learning with a Multi-Task Latent Space Objective
---

# Self-Supervised Learning with a Multi-Task Latent Space Objective
**arXiv**：[2602.05845v1](https://arxiv.org/abs/2602.05845) · [PDF](https://arxiv.org/pdf/2602.05845.pdf)  
**作者**：Pierre-François De Plaen, Abhishek Jha, Luc Van Gool, Tinne Tuytelaars, Marc Proesmans  

**一句话要点**：提出多任务潜在空间目标的自监督学习方法，通过分配独立预测器稳定多裁剪训练并提升性能。

**关键词**：自监督学习, 多裁剪策略, 预测器架构, 多任务学习, 非对称孪生网络, 图像表示学习

## 3 点简述
- 核心问题：多裁剪策略在BYOL等预测器架构中导致训练不稳定，源于共享预测器。
- 方法要点：为每种视图类型分配独立预测器，并引入掩码视图，形成多任务非对称孪生网络框架。
- 实验或效果：方法稳定，适用于多种骨干网络，在ImageNet上显著提升ResNet和ViT模型性能。

## 摘要（原文）

> Self-supervised learning (SSL) methods based on Siamese networks learn visual representations by aligning different views of the same image. The multi-crop strategy, which incorporates small local crops to global ones, enhances many SSL frameworks but causes instability in predictor-based architectures such as BYOL, SimSiam, and MoCo v3. We trace this failure to the shared predictor used across all views and demonstrate that assigning a separate predictor to each view type stabilizes multi-crop training, resulting in significant performance gains. Extending this idea, we treat each spatial transformation as a distinct alignment task and add cutout views, where part of the image is masked before encoding. This yields a simple multi-task formulation of asymmetric Siamese SSL that combines global, local, and masked views into a single framework. The approach is stable, generally applicable across backbones, and consistently improves the performance of ResNet and ViT models on ImageNet.


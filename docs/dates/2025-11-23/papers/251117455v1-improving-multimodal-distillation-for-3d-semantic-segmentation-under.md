---
layout: default
title: Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift
---

# Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift
**arXiv**：[2511.17455v1](https://arxiv.org/abs/2511.17455) · [PDF](https://arxiv.org/pdf/2511.17455.pdf)  
**作者**：Björn Michele, Alexandre Boulch, Gilles Puy, Tuan-Hung Vu, Renaud Marlet, Nicolas Courty  

**一句话要点**：改进多模态蒸馏以提升激光雷达语义分割在域偏移下的性能

**关键词**：语义分割, 域适应, 知识蒸馏, 激光雷达点云, 视觉基础模型

## 3 点简述
- 核心问题：激光雷达语义分割模型在域偏移下泛化能力差，需跨域适应。
- 方法要点：利用视觉基础模型特征，通过无监督图像到激光雷达知识蒸馏优化。
- 实验或效果：在四个挑战性设置中达到最先进结果，代码将开源。

## 摘要（原文）

> Semantic segmentation networks trained under full supervision for one type of lidar fail to generalize to unseen lidars without intervention. To reduce the performance gap under domain shifts, a recent trend is to leverage vision foundation models (VFMs) providing robust features across domains. In this work, we conduct an exhaustive study to identify recipes for exploiting VFMs in unsupervised domain adaptation for semantic segmentation of lidar point clouds. Building upon unsupervised image-to-lidar knowledge distillation, our study reveals that: (1) the architecture of the lidar backbone is key to maximize the generalization performance on a target domain; (2) it is possible to pretrain a single backbone once and for all, and use it to address many domain shifts; (3) best results are obtained by keeping the pretrained backbone frozen and training an MLP head for semantic segmentation. The resulting pipeline achieves state-of-the-art results in four widely-recognized and challenging settings. The code will be available at: https://github.com/valeoai/muddos.


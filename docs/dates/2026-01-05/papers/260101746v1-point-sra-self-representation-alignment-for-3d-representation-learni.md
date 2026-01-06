---
layout: default
title: Point-SRA: Self-Representation Alignment for 3D Representation Learning
---

# Point-SRA: Self-Representation Alignment for 3D Representation Learning
**arXiv**：[2601.01746v1](https://arxiv.org/abs/2601.01746) · [PDF](https://arxiv.org/pdf/2601.01746.pdf)  
**作者**：Lintong Wei, Jian Lu, Haozhe Cheng, Jihua Zhu, Kaibing Zhang  

**一句话要点**：提出Point-SRA方法，通过自蒸馏和概率建模解决3D表示学习中掩码固定和点级重建假设问题。

**关键词**：3D表示学习, 掩码自编码器, 概率建模, 自蒸馏, 点云处理, 多模态对齐

## 3 点简述
- 核心问题：现有MAE方法掩码比率固定，忽略多级表示相关性和点云多样性，导致重建假设冲突。
- 方法要点：采用可变掩码比率捕获互补信息，引入MeanFlow Transformer进行概率重建，并设计双自表示对齐机制。
- 实验或效果：在ScanObjectNN上超越Point-MAE 5.37%，颅内动脉瘤分割和3D目标检测任务表现优异。

## 摘要（原文）

> Masked autoencoders (MAE) have become a dominant paradigm in 3D representation learning, setting new performance benchmarks across various downstream tasks. Existing methods with fixed mask ratio neglect multi-level representational correlations and intrinsic geometric structures, while relying on point-wise reconstruction assumptions that conflict with the diversity of point cloud. To address these issues, we propose a 3D representation learning method, termed Point-SRA, which aligns representations through self-distillation and probabilistic modeling. Specifically, we assign different masking ratios to the MAE to capture complementary geometric and semantic information, while the MeanFlow Transformer (MFT) leverages cross-modal conditional embeddings to enable diverse probabilistic reconstruction. Our analysis further reveals that representations at different time steps in MFT also exhibit complementarity. Therefore, a Dual Self-Representation Alignment mechanism is proposed at both the MAE and MFT levels. Finally, we design a Flow-Conditioned Fine-Tuning Architecture to fully exploit the point cloud distribution learned via MeanFlow. Point-SRA outperforms Point-MAE by 5.37% on ScanObjectNN. On intracranial aneurysm segmentation, it reaches 96.07% mean IoU for arteries and 86.87% for aneurysms. For 3D object detection, Point-SRA achieves 47.3% AP@50, surpassing MaskPoint by 5.12%.


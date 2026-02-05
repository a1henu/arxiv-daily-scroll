---
layout: default
title: S-MUSt3R: Sliding Multi-view 3D Reconstruction
---

# S-MUSt3R: Sliding Multi-view 3D Reconstruction
**arXiv**：[2602.04517v1](https://arxiv.org/abs/2602.04517) · [PDF](https://arxiv.org/pdf/2602.04517.pdf)  
**作者**：Leonid Antsfeld, Boris Chidlovskii, Yohann Cabon, Vincent Leroy, Jerome Revaud  

**一句话要点**：提出S-MUSt3R以解决基础模型在大规模RGB流3D重建中的内存限制问题。

**关键词**：单目3D重建, 基础模型扩展, 序列分割, 轻量优化, 度量空间预测, RGB流处理

## 3 点简述
- 核心问题：基础模型在未标定图像3D感知中表现优异，但扩展至大规模RGB流重建时受内存限制。
- 方法要点：通过序列分割、段对齐和轻量闭环优化，无需模型重训练，提升MUSt3R模型的可扩展性。
- 实验或效果：在TUM、7-Scenes等数据集上验证，S-MUSt3R能处理长序列并产生准确一致的度量空间3D重建。

## 摘要（原文）

> The recent paradigm shift in 3D vision led to the rise of foundation models with remarkable capabilities in 3D perception from uncalibrated images. However, extending these models to large-scale RGB stream 3D reconstruction remains challenging due to memory limitations. This work proposes S-MUSt3R, a simple and efficient pipeline that extends the limits of foundation models for monocular 3D reconstruction. Our approach addresses the scalability bottleneck of foundation models through a simple strategy of sequence segmentation followed by segment alignment and lightweight loop closure optimization. Without model retraining, we benefit from remarkable 3D reconstruction capacities of MUSt3R model and achieve trajectory and reconstruction performance comparable to traditional methods with more complex architecture. We evaluate S-MUSt3R on TUM, 7-Scenes and proprietary robot navigation datasets and show that S-MUSt3R runs successfully on long RGB sequences and produces accurate and consistent 3D reconstruction. Our results highlight the potential of leveraging the MUSt3R model for scalable monocular 3D scene in real-world settings, with an important advantage of making predictions directly in the metric space.


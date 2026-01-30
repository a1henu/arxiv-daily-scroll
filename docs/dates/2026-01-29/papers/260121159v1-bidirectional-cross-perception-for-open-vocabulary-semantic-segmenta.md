---
layout: default
title: Bidirectional Cross-Perception for Open-Vocabulary Semantic Segmentation in Remote Sensing Imagery
---

# Bidirectional Cross-Perception for Open-Vocabulary Semantic Segmentation in Remote Sensing Imagery
**arXiv**：[2601.21159v1](https://arxiv.org/abs/2601.21159) · [PDF](https://arxiv.org/pdf/2601.21159.pdf)  
**作者**：Jianzheng Wang, Huan Ni  

**一句话要点**：提出SDCI框架以解决遥感图像中开放词汇语义分割的几何定位与语义预测难题。

**关键词**：开放词汇语义分割, 遥感图像分析, 跨模型注意力融合, 图扩散细化, 超像素协同预测, 免训练方法

## 3 点简述
- 核心问题：现有免训练开放词汇语义分割方法采用单向注入和浅层后处理，难以处理高分辨率遥感图像的密集对象和复杂边界。
- 方法要点：引入跨模型注意力融合模块、双向交叉图扩散细化模块和基于凸优化的超像素协同预测机制，实现双分支协同推理。
- 实验或效果：在多个遥感语义分割基准测试中表现优于现有方法，消融研究证实超像素结构在深度学习框架中仍有效。

## 摘要（原文）

> High-resolution remote sensing imagery is characterized by densely distributed land-cover objects and complex boundaries, which places higher demands on both geometric localization and semantic prediction. Existing training-free open-vocabulary semantic segmentation (OVSS) methods typically fuse CLIP and vision foundation models (VFMs) using "one-way injection" and "shallow post-processing" strategies, making it difficult to satisfy these requirements. To address this issue, we propose a spatial-regularization-aware dual-branch collaborative inference framework for training-free OVSS, termed SDCI. First, during feature encoding, SDCI introduces a cross-model attention fusion (CAF) module, which guides collaborative inference by injecting self-attention maps into each other. Second, we propose a bidirectional cross-graph diffusion refinement (BCDR) module that enhances the reliability of dual-branch segmentation scores through iterative random-walk diffusion. Finally, we incorporate low-level superpixel structures and develop a convex-optimization-based superpixel collaborative prediction (CSCP) mechanism to further refine object boundaries. Experiments on multiple remote sensing semantic segmentation benchmarks demonstrate that our method achieves better performance than existing approaches. Moreover, ablation studies further confirm that traditional object-based remote sensing image analysis methods leveraging superpixel structures remain effective within deep learning frameworks. Code: https://github.com/yu-ni1989/SDCI.


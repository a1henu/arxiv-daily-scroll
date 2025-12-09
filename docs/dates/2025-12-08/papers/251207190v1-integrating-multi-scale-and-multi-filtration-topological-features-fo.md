---
layout: default
title: Integrating Multi-scale and Multi-filtration Topological Features for Medical Image Classification
---

# Integrating Multi-scale and Multi-filtration Topological Features for Medical Image Classification
**arXiv**：[2512.07190v1](https://arxiv.org/abs/2512.07190) · [PDF](https://arxiv.org/pdf/2512.07190.pdf)  
**作者**：Pengfei Gu, Huimin Li, Haoteng Tang, Dongkuan, Xu, Erik Enriquez, DongChul Kim, Bin Fu, Danny Z. Chen  

**一句话要点**：提出多尺度多过滤拓扑特征集成框架以增强医学图像分类的解剖结构识别能力

**关键词**：医学图像分类, 拓扑数据分析, 多尺度特征, 持久同调, 深度学习集成

## 3 点简述
- 核心问题：现有深度网络忽视解剖结构，仅依赖像素强度或简单拓扑特征。
- 方法要点：计算多尺度立方体持久图，通过vineyard算法整合，并设计跨注意力网络处理。
- 实验或效果：在三个公开数据集上超越基线方法，验证了拓扑特征的有效性。

## 摘要（原文）

> Modern deep neural networks have shown remarkable performance in medical image classification. However, such networks either emphasize pixel-intensity features instead of fundamental anatomical structures (e.g., those encoded by topological invariants), or they capture only simple topological features via single-parameter persistence. In this paper, we propose a new topology-guided classification framework that extracts multi-scale and multi-filtration persistent topological features and integrates them into vision classification backbones. For an input image, we first compute cubical persistence diagrams (PDs) across multiple image resolutions/scales. We then develop a ``vineyard'' algorithm that consolidates these PDs into a single, stable diagram capturing signatures at varying granularities, from global anatomy to subtle local irregularities that may indicate early-stage disease. To further exploit richer topological representations produced by multiple filtrations, we design a cross-attention-based neural network that directly processes the consolidated final PDs. The resulting topological embeddings are fused with feature maps from CNNs or Transformers. By integrating multi-scale and multi-filtration topologies into an end-to-end architecture, our approach enhances the model's capacity to recognize complex anatomical structures. Evaluations on three public datasets show consistent, considerable improvements over strong baselines and state-of-the-art methods, demonstrating the value of our comprehensive topological perspective for robust and interpretable medical image classification.


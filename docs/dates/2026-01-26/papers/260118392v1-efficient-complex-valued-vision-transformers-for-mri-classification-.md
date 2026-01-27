---
layout: default
title: Efficient Complex-Valued Vision Transformers for MRI Classification Directly from k-Space
---

# Efficient Complex-Valued Vision Transformers for MRI Classification Directly from k-Space
**arXiv**：[2601.18392v1](https://arxiv.org/abs/2601.18392) · [PDF](https://arxiv.org/pdf/2601.18392.pdf)  
**作者**：Moritz Rempe, Lukas T. Rotkopf, Marco Schlimbach, Helmut Becker, Fabian Hörst, Johannes Haubold, Philipp Dammann, Kevin Kröninger, Jens Kleesiek  

**一句话要点**：提出复数视觉变换器直接处理k空间数据，以提升MRI分类效率与鲁棒性。

**关键词**：复数视觉变换器, k空间分类, MRI深度学习, 径向分块策略, 计算效率优化

## 3 点简述
- MRI深度学习中，传统方法丢弃相位信息且计算成本高，标准架构不适用于k空间全局数据。
- 引入径向k空间分块策略，设计复数视觉变换器，直接处理k空间数据以保留完整信息。
- 实验显示，该方法性能媲美图像域基准，对高加速因子更鲁棒，训练VRAM消耗降低达68倍。

## 摘要（原文）

> Deep learning applications in Magnetic Resonance Imaging (MRI) predominantly operate on reconstructed magnitude images, a process that discards phase information and requires computationally expensive transforms. Standard neural network architectures rely on local operations (convolutions or grid-patches) that are ill-suited for the global, non-local nature of raw frequency-domain (k-Space) data. In this work, we propose a novel complex-valued Vision Transformer (kViT) designed to perform classification directly on k-Space data. To bridge the geometric disconnect between current architectures and MRI physics, we introduce a radial k-Space patching strategy that respects the spectral energy distribution of the frequency-domain. Extensive experiments on the fastMRI and in-house datasets demonstrate that our approach achieves classification performance competitive with state-of-the-art image-domain baselines (ResNet, EfficientNet, ViT). Crucially, kViT exhibits superior robustness to high acceleration factors and offers a paradigm shift in computational efficiency, reducing VRAM consumption during training by up to 68$\times$ compared to standard methods. This establishes a pathway for resource-efficient, direct-from-scanner AI analysis.


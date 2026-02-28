---
layout: default
title: ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation
---

# ManifoldGD: Training-Free Hierarchical Manifold Guidance for Diffusion-Based Dataset Distillation
**arXiv**：[2602.23295v1](https://arxiv.org/abs/2602.23295) · [PDF](https://arxiv.org/pdf/2602.23295.pdf)  
**作者**：Ayush Roy, Wei-Yang Alex Lee, Rudrasis Chakraborty, Vishnu Suresh Lokhande  

**一句话要点**：提出ManifoldGD，通过分层流形引导实现无训练扩散数据集蒸馏

**关键词**：数据集蒸馏, 扩散模型, 无训练蒸馏, 流形引导, 分层聚类, 几何感知

## 3 点简述
- 核心问题：现有无训练扩散蒸馏方法依赖简单原型引导，缺乏几何感知，导致子优结果。
- 方法要点：基于VAE特征分层聚类提取多尺度原型，在去噪步投影对齐向量到局部切空间，保持流形一致性和语义。
- 实验或效果：在FID、嵌入距离和分类准确率上优于现有无训练和基于训练基线，提升代表性、多样性和图像保真度。

## 摘要（原文）

> In recent times, large datasets hinder efficient model training while also containing redundant concepts. Dataset distillation aims to synthesize compact datasets that preserve the knowledge of large-scale training sets while drastically reducing storage and computation. Recent advances in diffusion models have enabled training-free distillation by leveraging pre-trained generative priors; however, existing guidance strategies remain limited. Current score-based methods either perform unguided denoising or rely on simple mode-based guidance toward instance prototype centroids (IPC centroids), which often are rudimentary and suboptimal. We propose Manifold-Guided Distillation (ManifoldGD), a training-free diffusion-based framework that integrates manifold consistent guidance at every denoising timestep. Our method employs IPCs computed via a hierarchical, divisive clustering of VAE latent features, yielding a multi-scale coreset of IPCs that captures both coarse semantic modes and fine intra-class variability. Using a local neighborhood of the extracted IPC centroids, we create the latent manifold for each diffusion denoising timestep. At each denoising step, we project the mode-alignment vector onto the local tangent space of the estimated latent manifold, thus constraining the generation trajectory to remain manifold-faithful while preserving semantic consistency. This formulation improves representativeness, diversity, and image fidelity without requiring any model retraining. Empirical results demonstrate consistent gains over existing training-free and training-based baselines in terms of FID, l2 distance among real and synthetic dataset embeddings, and classification accuracy, establishing ManifoldGD as the first geometry-aware training-free data distillation framework.


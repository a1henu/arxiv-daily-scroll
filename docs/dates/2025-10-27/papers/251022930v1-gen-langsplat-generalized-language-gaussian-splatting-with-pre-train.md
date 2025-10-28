---
layout: default
title: Gen-LangSplat: Generalized Language Gaussian Splatting with Pre-Trained Feature Compression
---

# Gen-LangSplat: Generalized Language Gaussian Splatting with Pre-Trained Feature Compression
**arXiv**：[2510.22930v1](https://arxiv.org/abs/2510.22930) · [PDF](https://arxiv.org/pdf/2510.22930.pdf)  
**作者**：Pranav Saxena  

**一句话要点**：提出Gen-LangSplat以消除3D语言场构建中的场景特定训练瓶颈

**关键词**：3D高斯泼溅, 语言场建模, 预训练特征压缩, 开放词汇查询, 自编码器优化

## 3 点简述
- 核心问题：现有方法需为每个场景训练语言自编码器，导致部署扩展性差。
- 方法要点：使用预训练通用自编码器替代场景特定模型，实现跨场景固定潜在空间。
- 实验或效果：在ScanNet数据集验证，性能与原方法相当或更优，提升效率。

## 摘要（原文）

> Modeling open-vocabulary language fields in 3D is essential for intuitive
> human-AI interaction and querying within physical environments.
> State-of-the-art approaches, such as LangSplat, leverage 3D Gaussian Splatting
> to efficiently construct these language fields, encoding features distilled
> from high-dimensional models like CLIP. However, this efficiency is currently
> offset by the requirement to train a scene-specific language autoencoder for
> feature compression, introducing a costly, per-scene optimization bottleneck
> that hinders deployment scalability. In this work, we introduce Gen-LangSplat,
> that eliminates this requirement by replacing the scene-wise autoencoder with a
> generalized autoencoder, pre-trained extensively on the large-scale ScanNet
> dataset. This architectural shift enables the use of a fixed, compact latent
> space for language features across any new scene without any scene-specific
> training. By removing this dependency, our entire language field construction
> process achieves a efficiency boost while delivering querying performance
> comparable to, or exceeding, the original LangSplat method. To validate our
> design choice, we perform a thorough ablation study empirically determining the
> optimal latent embedding dimension and quantifying representational fidelity
> using Mean Squared Error and cosine similarity between the original and
> reprojected 512-dimensional CLIP embeddings. Our results demonstrate that
> generalized embeddings can efficiently and accurately support open-vocabulary
> querying in novel 3D scenes, paving the way for scalable, real-time interactive
> 3D AI applications.


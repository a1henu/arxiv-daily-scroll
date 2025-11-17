---
layout: default
title: Rethinking Autoregressive Models for Lossless Image Compression via Hierarchical Parallelism and Progressive Adaptation
---

# Rethinking Autoregressive Models for Lossless Image Compression via Hierarchical Parallelism and Progressive Adaptation
**arXiv**：[2511.10991v1](https://arxiv.org/abs/2511.10991) · [PDF](https://arxiv.org/pdf/2511.10991.pdf)  
**作者**：Daxin Li, Yuanchao Bai, Kai Wang, Wenbo Zhao, Junjun Jiang, Xianming Liu  

**一句话要点**：提出分层并行与渐进适应框架，使自回归模型在无损图像压缩中实用高效

**关键词**：无损图像压缩, 自回归模型, 分层并行, 渐进适应, 内容感知卷积, 低秩适配器

## 3 点简述
- 自回归模型理论性能优但计算成本高，阻碍实际应用
- 采用分层并行结构和内容感知卷积门控，高效捕获空间依赖
- 在自然、卫星和医学数据集上验证，实现新SOTA压缩性能

## 摘要（原文）

> Autoregressive (AR) models, the theoretical performance benchmark for learned lossless image compression, are often dismissed as impractical due to prohibitive computational cost. This work re-thinks this paradigm, introducing a framework built on hierarchical parallelism and progressive adaptation that re-establishes pure autoregression as a top-performing and practical solution. Our approach is embodied in the Hierarchical Parallel Autoregressive ConvNet (HPAC), an ultra-lightweight pre-trained model using a hierarchical factorized structure and content-aware convolutional gating to efficiently capture spatial dependencies. We introduce two key optimizations for practicality: Cache-then-Select Inference (CSI), which accelerates coding by eliminating redundant computations, and Adaptive Focus Coding (AFC), which efficiently extends the framework to high bit-depth images. Building on this efficient foundation, our progressive adaptation strategy is realized by Spatially-Aware Rate-Guided Progressive Fine-tuning (SARP-FT). This instance-level strategy fine-tunes the model for each test image by optimizing low-rank adapters on progressively larger, spatially-continuous regions selected via estimated information density. Experiments on diverse datasets (natural, satellite, medical) validate that our method achieves new state-of-the-art compression. Notably, our approach sets a new benchmark in learned lossless compression, showing a carefully designed AR framework can offer significant gains over existing methods with a small parameter count and competitive coding speeds.


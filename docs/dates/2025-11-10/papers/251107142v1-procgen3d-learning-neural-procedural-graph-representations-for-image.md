---
layout: default
title: ProcGen3D: Learning Neural Procedural Graph Representations for Image-to-3D Reconstruction
---

# ProcGen3D: Learning Neural Procedural Graph Representations for Image-to-3D Reconstruction
**arXiv**：[2511.07142v1](https://arxiv.org/abs/2511.07142) · [PDF](https://arxiv.org/pdf/2511.07142.pdf)  
**作者**：Xinyi Zhang, Daoyi Gao, Naiqi Li, Angela Dai  

**一句话要点**：提出ProcGen3D方法，通过图像生成程序化图以重建3D对象

**关键词**：图像到3D重建, 程序化图表示, Transformer模型, Monte Carlo树搜索, 3D内容生成

## 3 点简述
- 核心问题：从RGB图像重建复杂3D资产，需高效表示与生成方法
- 方法要点：使用基于图的程序化表示，结合Transformer和MCTS采样优化对齐
- 实验或效果：在仙人掌、树木和桥梁上优于现有方法，提升真实图像泛化能力

## 摘要（原文）

> We introduce ProcGen3D, a new approach for 3D content creation by generating
> procedural graph abstractions of 3D objects, which can then be decoded into
> rich, complex 3D assets. Inspired by the prevalent use of procedural generators
> in production 3D applications, we propose a sequentialized, graph-based
> procedural graph representation for 3D assets. We use this to learn to
> approximate the landscape of a procedural generator for image-based 3D
> reconstruction. We employ edge-based tokenization to encode the procedural
> graphs, and train a transformer prior to predict the next token conditioned on
> an input RGB image. Crucially, to enable better alignment of our generated
> outputs to an input image, we incorporate Monte Carlo Tree Search (MCTS) guided
> sampling into our generation process, steering output procedural graphs towards
> more image-faithful reconstructions. Our approach is applicable across a
> variety of objects that can be synthesized with procedural generators.
> Extensive experiments on cacti, trees, and bridges show that our neural
> procedural graph generation outperforms both state-of-the-art generative 3D
> methods and domain-specific modeling techniques. Furthermore, this enables
> improved generalization on real-world input images, despite training only on
> synthetic data.


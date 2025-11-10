---
layout: default
title: How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?
---

# How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?
**arXiv**：[2511.05449v1](https://arxiv.org/abs/2511.05449) · [PDF](https://arxiv.org/pdf/2511.05449.pdf)  
**作者**：Tuan Anh Tran, Duy M. H. Nguyen, Hoai-Chau Tran, Michael Barz, Khoa D. Doan, Roger Wattenhofer, Ngo Anh Vien, Mathias Niepert, Daniel Sonntag, Paul Swoboda  

**一句话要点**：提出gitmerge3D方法以减少3D点云变换器中的令牌冗余，提升计算效率。

**关键词**：3D点云变换器, 令牌冗余, 计算效率优化, 语义分割, 图令牌合并, 3D基础架构

## 3 点简述
- 核心问题：3D点云变换器依赖密集令牌，导致高计算和内存成本。
- 方法要点：引入全局信息图令牌合并，可减少90-95%令牌数。
- 实验效果：在多个3D视觉任务中保持性能，显著提升效率。

## 摘要（原文）

> Recent advances in 3D point cloud transformers have led to state-of-the-art
> results in tasks such as semantic segmentation and reconstruction. However,
> these models typically rely on dense token representations, incurring high
> computational and memory costs during training and inference. In this work, we
> present the finding that tokens are remarkably redundant, leading to
> substantial inefficiency. We introduce gitmerge3D, a globally informed graph
> token merging method that can reduce the token count by up to 90-95% while
> maintaining competitive performance. This finding challenges the prevailing
> assumption that more tokens inherently yield better performance and highlights
> that many current models are over-tokenized and under-optimized for
> scalability. We validate our method across multiple 3D vision tasks and show
> consistent improvements in computational efficiency. This work is the first to
> assess redundancy in large-scale 3D transformer models, providing insights into
> the development of more efficient 3D foundation architectures. Our code and
> checkpoints are publicly available at https://gitmerge3d.github.io


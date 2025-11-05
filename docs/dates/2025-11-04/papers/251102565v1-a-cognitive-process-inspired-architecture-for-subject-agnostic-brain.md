---
layout: default
title: A Cognitive Process-Inspired Architecture for Subject-Agnostic Brain Visual Decoding
---

# A Cognitive Process-Inspired Architecture for Subject-Agnostic Brain Visual Decoding
**arXiv**：[2511.02565v1](https://arxiv.org/abs/2511.02565) · [PDF](https://arxiv.org/pdf/2511.02565.pdf)  
**作者**：Jingyu Lu, Haonan Wang, Qixiang Zhang, Xiaomeng Li  

**一句话要点**：提出VCFlow架构以解决跨被试脑视觉解码的泛化问题

**关键词**：脑视觉解码, 跨被试泛化, 视觉系统建模, 对比学习, 快速重建

## 3 点简述
- 核心问题：跨被试脑信号解码泛化难，需大量个体数据与计算
- 方法要点：模拟视觉系统腹背流，解耦特征并采用对比学习
- 实验或效果：牺牲7%精度，10秒生成视频，无需重训练

## 摘要（原文）

> Subject-agnostic brain decoding, which aims to reconstruct continuous visual
> experiences from fMRI without subject-specific training, holds great potential
> for clinical applications. However, this direction remains underexplored due to
> challenges in cross-subject generalization and the complex nature of brain
> signals. In this work, we propose Visual Cortex Flow Architecture (VCFlow), a
> novel hierarchical decoding framework that explicitly models the ventral-dorsal
> architecture of the human visual system to learn multi-dimensional
> representations. By disentangling and leveraging features from early visual
> cortex, ventral, and dorsal streams, VCFlow captures diverse and complementary
> cognitive information essential for visual reconstruction. Furthermore, we
> introduce a feature-level contrastive learning strategy to enhance the
> extraction of subject-invariant semantic representations, thereby enhancing
> subject-agnostic applicability to previously unseen subjects. Unlike
> conventional pipelines that need more than 12 hours of per-subject data and
> heavy computation, VCFlow sacrifices only 7\% accuracy on average yet generates
> each reconstructed video in 10 seconds without any retraining, offering a fast
> and clinically scalable solution. The source code will be released upon
> acceptance of the paper.


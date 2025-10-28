---
layout: default
title: HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling
---

# HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling
**arXiv**：[2510.23043v1](https://arxiv.org/abs/2510.23043) · [PDF](https://arxiv.org/pdf/2510.23043.pdf)  
**作者**：Joungbin An, Kristen Grauman  

**一句话要点**：提出HieraMamba架构以解决长视频中语言查询的时序定位问题

**关键词**：视频时序定位, 分层架构, 锚点令牌, 对比学习, 长视频理解, Mamba模型

## 3 点简述
- 核心问题：长视频时序定位需平衡全局上下文与细粒度时序细节，现有方法易因过度下采样或固定窗口而损失精度。
- 方法要点：采用分层Anchor-MambaPooling块，通过选择性扫描生成多粒度锚点令牌，结合对比损失保留局部细节与全局区分性。
- 实验或效果：在Ego4D-NLQ、MAD和TACoS数据集上达到新SOTA，实现长未修剪视频的精确时序定位。

## 摘要（原文）

> Video temporal grounding, the task of localizing the start and end times of a
> natural language query in untrimmed video, requires capturing both global
> context and fine-grained temporal detail. This challenge is particularly
> pronounced in long videos, where existing methods often compromise temporal
> fidelity by over-downsampling or relying on fixed windows. We present
> HieraMamba, a hierarchical architecture that preserves temporal structure and
> semantic richness across scales. At its core are Anchor-MambaPooling (AMP)
> blocks, which utilize Mamba's selective scanning to produce compact anchor
> tokens that summarize video content at multiple granularities. Two
> complementary objectives, anchor-conditioned and segment-pooled contrastive
> losses, encourage anchors to retain local detail while remaining globally
> discriminative. HieraMamba sets a new state-of-the-art on Ego4D-NLQ, MAD, and
> TACoS, demonstrating precise, temporally faithful localization in long,
> untrimmed videos.


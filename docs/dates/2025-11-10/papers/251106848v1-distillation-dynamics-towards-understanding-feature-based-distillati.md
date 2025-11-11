---
layout: default
title: Distillation Dynamics: Towards Understanding Feature-Based Distillation in Vision Transformers
---

# Distillation Dynamics: Towards Understanding Feature-Based Distillation in Vision Transformers
**arXiv**：[2511.06848v1](https://arxiv.org/abs/2511.06848) · [PDF](https://arxiv.org/pdf/2511.06848.pdf)  
**作者**：Huiyuan Tian, Bonan Xu Shijian Li  

**一句话要点**：提出蒸馏动力学框架以解决ViT特征蒸馏负迁移问题

**关键词**：视觉Transformer, 知识蒸馏, 特征蒸馏, 负迁移, 模型压缩, 表示学习

## 3 点简述
- 核心问题：特征蒸馏在ViT中失效，导致负迁移，性能不如简单logit蒸馏
- 方法要点：结合频谱分析、信息熵和激活幅度追踪，揭示ViT的U形信息处理模式
- 实验或效果：发现师生模型表示范式不匹配，需超越特征模仿设计压缩策略

## 摘要（原文）

> While feature-based knowledge distillation has proven highly effective for
> compressing CNNs, these techniques unexpectedly fail when applied to Vision
> Transformers (ViTs), often performing worse than simple logit-based
> distillation. We provide the first comprehensive analysis of this phenomenon
> through a novel analytical framework termed as ``distillation dynamics",
> combining frequency spectrum analysis, information entropy metrics, and
> activation magnitude tracking. Our investigation reveals that ViTs exhibit a
> distinctive U-shaped information processing pattern: initial compression
> followed by expansion. We identify the root cause of negative transfer in
> feature distillation: a fundamental representational paradigm mismatch between
> teacher and student models. Through frequency-domain analysis, we show that
> teacher models employ distributed, high-dimensional encoding strategies in
> later layers that smaller student models cannot replicate due to limited
> channel capacity. This mismatch causes late-layer feature alignment to actively
> harm student performance. Our findings reveal that successful knowledge
> transfer in ViTs requires moving beyond naive feature mimicry to methods that
> respect these fundamental representational constraints, providing essential
> theoretical guidance for designing effective ViTs compression strategies. All
> source code and experimental logs are provided in the supplementary material.


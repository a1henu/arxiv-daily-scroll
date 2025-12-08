---
layout: default
title: Interleaved Latent Visual Reasoning with Selective Perceptual Modeling
---

# Interleaved Latent Visual Reasoning with Selective Perceptual Modeling
**arXiv**：[2512.05665v1](https://arxiv.org/abs/2512.05665) · [PDF](https://arxiv.org/pdf/2512.05665.pdf)  
**作者**：Shuai Dong, Siyuan Wang, Xingyu Liu, Zhongyu Wei  

**一句话要点**：提出ILVR框架以解决多模态大语言模型中视觉推理的计算成本与感知精度权衡问题

**关键词**：多模态大语言模型, 潜在视觉推理, 交错推理, 选择性感知建模, 动量蒸馏, 动态状态演化

## 3 点简述
- 核心问题：现有潜在视觉推理方法在计算效率与精确感知建模间存在矛盾，导致动态问题建模困难
- 方法要点：ILVR通过交错文本生成与潜在视觉表示，结合动量教师模型选择性蒸馏特征，实现自适应视觉信号生成
- 实验或效果：在多项多模态推理基准测试中，ILVR显著优于现有方法，有效连接细粒度感知与序列推理

## 摘要（原文）

> Interleaved reasoning paradigms enhance Multimodal Large Language Models (MLLMs) with visual feedback but are hindered by the prohibitive computational cost of repeatedly re-encoding pixel-dense images. A promising alternative, latent visual reasoning, circumvents this bottleneck yet currently forces a critical trade-off: methods either sacrifice precise perceptual modeling by over-compressing features or fail to model dynamic problems due to static, non-interleaved structures. We introduce Interleaved Latent Visual Reasoning (ILVR), a framework that unifies dynamic state evolution with precise perceptual modeling. ILVR interleaves textual generation with latent visual representations that act as specific, evolving cues for subsequent reasoning. To enable this, we employ a self-supervision strategy where a Momentum Teacher Model selectively distills relevant features from helper images into sparse supervision targets. This adaptive selection mechanism guides the model to autonomously generate context-aware visual signals. Extensive experiments on multimodal reasoning benchmarks demonstrate that ILVR significantly outperforms existing approaches, effectively bridging the gap between fine-grained perception and sequential multimodal reasoning.


---
layout: default
title: Visual Diversity and Region-aware Prompt Learning for Zero-shot HOI Detection
---

# Visual Diversity and Region-aware Prompt Learning for Zero-shot HOI Detection
**arXiv**：[2510.25094v1](https://arxiv.org/abs/2510.25094) · [PDF](https://arxiv.org/pdf/2510.25094.pdf)  
**作者**：Chanhyeong Yang, Taehoon Song, Jihwan Park, Hyunwoo J. Kim  

**一句话要点**：提出VDRP框架以解决零样本人-物交互检测中的视觉多样性和区域感知问题

**关键词**：零样本学习, 人-物交互检测, 提示学习, 视觉多样性, 区域感知, CLIP模型

## 3 点简述
- 核心问题：零样本HOI检测中，动词类内视觉多样性和类间视觉纠缠导致识别困难
- 方法要点：采用视觉多样性感知提示学习和区域特定概念检索，增强提示嵌入
- 实验或效果：在HICO-DET基准上实现SOTA性能，有效处理多样性和纠缠问题

## 摘要（原文）

> Zero-shot Human-Object Interaction detection aims to localize humans and
> objects in an image and recognize their interaction, even when specific
> verb-object pairs are unseen during training. Recent works have shown promising
> results using prompt learning with pretrained vision-language models such as
> CLIP, which align natural language prompts with visual features in a shared
> embedding space. However, existing approaches still fail to handle the visual
> complexity of interaction, including (1) intra-class visual diversity, where
> instances of the same verb appear in diverse poses and contexts, and (2)
> inter-class visual entanglement, where distinct verbs yield visually similar
> patterns. To address these challenges, we propose VDRP, a framework for Visual
> Diversity and Region-aware Prompt learning. First, we introduce a visual
> diversity-aware prompt learning strategy that injects group-wise visual
> variance into the context embedding. We further apply Gaussian perturbation to
> encourage the prompts to capture diverse visual variations of a verb. Second,
> we retrieve region-specific concepts from the human, object, and union regions.
> These are used to augment the diversity-aware prompt embeddings, yielding
> region-aware prompts that enhance verb-level discrimination. Experiments on the
> HICO-DET benchmark demonstrate that our method achieves state-of-the-art
> performance under four zero-shot evaluation settings, effectively addressing
> both intra-class diversity and inter-class visual entanglement. Code is
> available at https://github.com/mlvlab/VDRP.


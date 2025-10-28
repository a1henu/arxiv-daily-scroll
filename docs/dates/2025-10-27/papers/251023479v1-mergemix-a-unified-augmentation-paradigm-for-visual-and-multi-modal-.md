---
layout: default
title: MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding
---

# MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding
**arXiv**：[2510.23479v1](https://arxiv.org/abs/2510.23479) · [PDF](https://arxiv.org/pdf/2510.23479.pdf)  
**作者**：Xin Jin, Siyuan Li, Siyong Jian, Kai Yu, Huan Wang  

**一句话要点**：提出MergeMix以解决多模态大语言模型中的对齐质量与效率权衡问题

**关键词**：多模态大语言模型, 训练增强, 偏好对齐, 图像混合, SimPO损失

## 3 点简述
- 核心问题：SFT依赖大量人工标注且无法捕捉细微偏好，RL效率低且不稳定。
- 方法要点：通过注意力感知图像混合和偏好驱动训练，结合SimPO损失优化。
- 实验或效果：在分类任务中实现竞争性准确率，提升效率与对齐质量。

## 摘要（原文）

> Vision-language alignment in multi-modal large language models (MLLMs)
> typically relies on supervised fine-tuning (SFT) or reinforcement learning
> (RL). SFT is stable and efficient but requires large-scale human annotations
> and cannot capture subtle preferences, while RL brings in a reward signal for
> training, but suffers from overhead and instability. These limitations
> highlight a trade-off between scalability, robustness, and alignment quality.
> To address this, we propose MergeMix, a training-time augmentation paradigm
> that bridges SFT and RL. It first applies an attention-aware image mixing via
> token merge with more cluster representation and spatial context, and then
> presents a preference-driven training paradigm for MLLMs by building preference
> pairs with mixed images and raw images, and optimizing via SimPO loss. As a
> mixup augmentation, MergeMix enhances attention consistency and efficiency,
> surpassing other heuristic-based methods in classification. Extensive
> experiments demonstrate that MergeMix achieves competitive accuracy with
> improved efficiency, providing a scalable approach to preference alignment in
> classification and MLLMs.


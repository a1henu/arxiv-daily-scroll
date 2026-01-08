---
layout: default
title: Mind the Generative Details: Direct Localized Detail Preference Optimization for Video Diffusion Models
---

# Mind the Generative Details: Direct Localized Detail Preference Optimization for Video Diffusion Models
**arXiv**：[2601.04068v1](https://arxiv.org/abs/2601.04068) · [PDF](https://arxiv.org/pdf/2601.04068.pdf)  
**作者**：Zitong Huang, Kaidong Zhang, Yukang Ding, Chao Gao, Rui Ding, Ying Chen, Wangmeng Zuo  

**一句话要点**：提出LocalDPO框架，通过局部偏好优化提升视频扩散模型对齐效率与质量。

**关键词**：视频扩散模型, 偏好优化, 局部对齐, 后训练框架, 时空区域学习

## 3 点简述
- 核心问题：现有DPO方法依赖多样本排序和外部评判模型，效率低且全局监督模糊。
- 方法要点：从真实视频自动构建局部偏好对，在时空区域级别优化对齐，无需外部模型或人工标注。
- 实验或效果：在Wan2.1和CogVideoX上验证，提升视频保真度、时序一致性和人类偏好得分。

## 摘要（原文）

> Aligning text-to-video diffusion models with human preferences is crucial for generating high-quality videos. Existing Direct Preference Otimization (DPO) methods rely on multi-sample ranking and task-specific critic models, which is inefficient and often yields ambiguous global supervision. To address these limitations, we propose LocalDPO, a novel post-training framework that constructs localized preference pairs from real videos and optimizes alignment at the spatio-temporal region level. We design an automated pipeline to efficiently collect preference pair data that generates preference pairs with a single inference per prompt, eliminating the need for external critic models or manual annotation. Specifically, we treat high-quality real videos as positive samples and generate corresponding negatives by locally corrupting them with random spatio-temporal masks and restoring only the masked regions using the frozen base model. During training, we introduce a region-aware DPO loss that restricts preference learning to corrupted areas for rapid convergence. Experiments on Wan2.1 and CogVideoX demonstrate that LocalDPO consistently improves video fidelity, temporal coherence and human preference scores over other post-training approaches, establishing a more efficient and fine-grained paradigm for video generator alignment.


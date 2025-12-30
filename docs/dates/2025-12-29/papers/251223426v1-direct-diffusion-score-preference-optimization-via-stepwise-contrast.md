---
layout: default
title: Direct Diffusion Score Preference Optimization via Stepwise Contrastive Policy-Pair Supervision
---

# Direct Diffusion Score Preference Optimization via Stepwise Contrastive Policy-Pair Supervision
**arXiv**：[2512.23426v1](https://arxiv.org/abs/2512.23426) · [PDF](https://arxiv.org/pdf/2512.23426.pdf)  
**作者**：Dohyun Kim, Seungwoo Lyu, Seung Wook Kim, Paul Hongsuck Seo  

**一句话要点**：提出DDSPO以解决扩散模型在文本到图像生成中与用户意图对齐和美学质量一致性的问题。

**关键词**：扩散模型, 偏好优化, 文本到图像生成, 无监督学习, 对比监督

## 3 点简述
- 核心问题：扩散模型在文本到图像生成中难以完全对齐用户意图和保持美学质量，现有方法依赖昂贵且可能嘈杂的人工标注数据。
- 方法要点：DDSPO通过对比获胜和失败策略，在去噪轨迹上提供密集的逐时间步监督，无需显式奖励建模或手动标注。
- 实验或效果：DDSPO在文本图像对齐和视觉质量上优于或匹配现有偏好方法，且需要更少的监督。

## 摘要（原文）

> Diffusion models have achieved impressive results in generative tasks such as text-to-image synthesis, yet they often struggle to fully align outputs with nuanced user intent and maintain consistent aesthetic quality. Existing preference-based training methods like Diffusion Direct Preference Optimization help address these issues but rely on costly and potentially noisy human-labeled datasets. In this work, we introduce Direct Diffusion Score Preference Optimization (DDSPO), which directly derives per-timestep supervision from winning and losing policies when such policies are available. Unlike prior methods that operate solely on final samples, DDSPO provides dense, transition-level signals across the denoising trajectory. In practice, we avoid reliance on labeled data by automatically generating preference signals using a pretrained reference model: we contrast its outputs when conditioned on original prompts versus semantically degraded variants. This practical strategy enables effective score-space preference supervision without explicit reward modeling or manual annotations. Empirical results demonstrate that DDSPO improves text-image alignment and visual quality, outperforming or matching existing preference-based methods while requiring significantly less supervision. Our implementation is available at: https://dohyun-as.github.io/DDSPO


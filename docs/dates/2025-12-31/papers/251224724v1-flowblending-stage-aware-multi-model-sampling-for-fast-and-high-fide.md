---
layout: default
title: FlowBlending: Stage-Aware Multi-Model Sampling for Fast and High-Fidelity Video Generation
---

# FlowBlending: Stage-Aware Multi-Model Sampling for Fast and High-Fidelity Video Generation
**arXiv**：[2512.24724v1](https://arxiv.org/abs/2512.24724) · [PDF](https://arxiv.org/pdf/2512.24724.pdf)  
**作者**：Jibin Song, Mingi Kwon, Jaeseok Jeong, Youngjung Uh  

**一句话要点**：提出FlowBlending，一种阶段感知多模型采样策略，以加速视频生成并保持高保真度。

**关键词**：视频生成, 多模型采样, 阶段感知, 速度发散分析, 推理加速

## 3 点简述
- 核心问题：模型容量在不同时间步的影响差异，早期和晚期阶段关键，中间阶段可忽略。
- 方法要点：使用大模型和小模型分别处理容量敏感阶段和中间阶段，基于速度发散分析确定阶段边界。
- 实验或效果：在LTX-Video和WAN 2.1上实现最高1.65倍加速和57.35% FLOPs减少，保持视觉保真度和时间连贯性。

## 摘要（原文）

> In this work, we show that the impact of model capacity varies across timesteps: it is crucial for the early and late stages but largely negligible during the intermediate stage. Accordingly, we propose FlowBlending, a stage-aware multi-model sampling strategy that employs a large model and a small model at capacity-sensitive stages and intermediate stages, respectively. We further introduce simple criteria to choose stage boundaries and provide a velocity-divergence analysis as an effective proxy for identifying capacity-sensitive regions. Across LTX-Video (2B/13B) and WAN 2.1 (1.3B/14B), FlowBlending achieves up to 1.65x faster inference with 57.35% fewer FLOPs, while maintaining the visual fidelity, temporal coherence, and semantic alignment of the large models. FlowBlending is also compatible with existing sampling-acceleration techniques, enabling up to 2x additional speedup. Project page is available at: https://jibin86.github.io/flowblending_project_page.


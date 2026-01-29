---
layout: default
title: Latent Temporal Discrepancy as Motion Prior: A Loss-Weighting Strategy for Dynamic Fidelity in T2V
---

# Latent Temporal Discrepancy as Motion Prior: A Loss-Weighting Strategy for Dynamic Fidelity in T2V
**arXiv**：[2601.20504v1](https://arxiv.org/abs/2601.20504) · [PDF](https://arxiv.org/pdf/2601.20504.pdf)  
**作者**：Meiqi Wu, Bingze Song, Ruimin Lin, Chen Zhu, Xiaokun Feng, Jiahong Wu, Xiangxiang Chu, Kaiqi Huang  

**一句话要点**：提出潜在时间差异作为运动先验，通过损失加权策略提升视频生成中的动态保真度。

**关键词**：视频生成, 扩散模型, 运动先验, 损失加权, 动态保真度, 潜在空间分析

## 3 点简述
- 核心问题：现有扩散模型在动态视频生成中，因静态损失限制，难以处理剧烈运动变化，导致质量下降。
- 方法要点：引入潜在时间差异作为运动先验，基于潜在空间帧间变化进行损失加权，对高动态区域施加更大惩罚。
- 实验或效果：在VBench和VMBench基准测试中，分别提升3.31%和3.58%，显著改善运动质量。

## 摘要（原文）

> Video generation models have achieved notable progress in static scenarios, yet their performance in motion video generation remains limited, with quality degrading under drastic dynamic changes. This is due to noise disrupting temporal coherence and increasing the difficulty of learning dynamic regions. {Unfortunately, existing diffusion models rely on static loss for all scenarios, constraining their ability to capture complex dynamics.} To address this issue, we introduce Latent Temporal Discrepancy (LTD) as a motion prior to guide loss weighting. LTD measures frame-to-frame variation in the latent space, assigning larger penalties to regions with higher discrepancy while maintaining regular optimization for stable regions. This motion-aware strategy stabilizes training and enables the model to better reconstruct high-frequency dynamics. Extensive experiments on the general benchmark VBench and the motion-focused VMBench show consistent gains, with our method outperforming strong baselines by 3.31% on VBench and 3.58% on VMBench, achieving significant improvements in motion quality.


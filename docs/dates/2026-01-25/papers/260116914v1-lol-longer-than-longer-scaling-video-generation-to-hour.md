---
layout: default
title: LoL: Longer than Longer, Scaling Video Generation to Hour
---

# LoL: Longer than Longer, Scaling Video Generation to Hour
**arXiv**：[2601.16914v1](https://arxiv.org/abs/2601.16914) · [PDF](https://arxiv.org/pdf/2601.16914.pdf)  
**作者**：Justin Cui, Jie Wu, Ming Li, Tao Yang, Xiaojie Li, Rui Wang, Andrew Bai, Yuanhao Ban, Cho-Jui Hsieh  

**一句话要点**：提出多头RoPE抖动方法以解决长视频生成中的sink-collapse问题

**关键词**：长视频生成, 自回归模型, 注意力机制, RoPE位置编码, sink-collapse, 流式生成

## 3 点简述
- 核心问题：现有长视频生成模型存在sink-collapse现象，导致场景重置和循环运动
- 方法要点：通过引入多头RoPE抖动打破注意力同质化，抑制性能衰减
- 实验效果：实现实时、流式、无限长度视频生成，最长生成12小时视频

## 摘要（原文）

> Recent research in long-form video generation has shifted from bidirectional to autoregressive models, yet these methods commonly suffer from error accumulation and a loss of long-term coherence. While attention sink frames have been introduced to mitigate this performance decay, they often induce a critical failure mode we term sink-collapse: the generated content repeatedly reverts to the sink frame, resulting in abrupt scene resets and cyclic motion patterns. Our analysis reveals that sink-collapse originates from an inherent conflict between the periodic structure of Rotary Position Embedding (RoPE) and the multi-head attention mechanisms prevalent in current generative models. To address it, we propose a lightweight, training-free approach that effectively suppresses this behavior by introducing multi-head RoPE jitter that breaks inter-head attention homogenization and mitigates long-horizon collapse. Extensive experiments show that our method successfully alleviates sink-collapse while preserving generation quality. To the best of our knowledge, this work achieves the first demonstration of real-time, streaming, and infinite-length video generation with little quality decay. As an illustration of this robustness, we generate continuous videos up to 12 hours in length, which, to our knowledge, is among the longest publicly demonstrated results in streaming video generation.


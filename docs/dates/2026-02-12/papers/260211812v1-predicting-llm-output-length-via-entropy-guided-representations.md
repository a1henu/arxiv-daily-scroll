---
layout: default
title: Predicting LLM Output Length via Entropy-Guided Representations
---

# Predicting LLM Output Length via Entropy-Guided Representations
**arXiv**：[2602.11812v1](https://arxiv.org/abs/2602.11812) · [PDF](https://arxiv.org/pdf/2602.11812.pdf)  
**作者**：Huanyi Xie, Yubin Chen, Liangyu Wang, Lijie Hu, Di Wang  

**一句话要点**：提出基于熵引导表示的轻量级框架，以解决LLM批处理推理中因序列长度长尾分布导致的填充浪费问题。

**关键词**：LLM推理优化, 序列长度预测, 熵引导表示, 批处理效率, 轻量级框架

## 3 点简述
- 核心问题：LLM服务与强化学习采样中序列长度的长尾分布导致批处理推理时填充过多，造成显著计算浪费。
- 方法要点：引入熵引导令牌池化和渐进长度预测，重用主模型内部隐藏状态，实现高效长度预测。
- 实验或效果：在ForeLen基准上，熵引导令牌池化将MAE降低29.16%，结合长度感知调度器提升端到端吞吐量。

## 摘要（原文）

> The long-tailed distribution of sequence lengths in LLM serving and reinforcement learning (RL) sampling causes significant computational waste due to excessive padding in batched inference. Existing methods rely on auxiliary models for static length prediction, but they incur high overhead, generalize poorly, and fail in stochastic "one-to-many" sampling scenarios. We introduce a lightweight framework that reuses the main model's internal hidden states for efficient length prediction. Our framework features two core components: 1) Entropy-Guided Token Pooling (EGTP), which uses on-the-fly activations and token entropy for highly accurate static prediction with negligible cost, and 2) Progressive Length Prediction (PLP), which dynamically estimates the remaining length at each decoding step to handle stochastic generation. To validate our approach, we build and release ForeLen, a comprehensive benchmark with long-sequence, Chain-of-Thought, and RL data. On ForeLen, EGTP achieves state-of-the-art accuracy, reducing MAE by 29.16\% over the best baseline. Integrating our methods with a length-aware scheduler yields significant end-to-end throughput gains. Our work provides a new technical and evaluation baseline for efficient LLM inference.


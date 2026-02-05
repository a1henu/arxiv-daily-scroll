---
layout: default
title: OAT: Ordered Action Tokenization
---

# OAT: Ordered Action Tokenization
**arXiv**：[2602.04215v1](https://arxiv.org/abs/2602.04215) · [PDF](https://arxiv.org/pdf/2602.04215.pdf)  
**作者**：Chaoqi Liu, Xiaoshen Han, Jiawei Gao, Yue Zhao, Haonan Chen, Yilun Du  

**一句话要点**：提出有序动作标记化以解决机器人学习中自回归策略的动作离散化问题

**关键词**：机器人学习, 自回归策略, 动作标记化, Transformer, 有限标量量化, 推理灵活性

## 3 点简述
- 核心问题：现有动作标记化方法导致过长序列或缺乏结构，限制自回归预测兼容性
- 方法要点：基于Transformer、有限标量量化和排序诱导训练，实现高压缩、可解码和有序的标记空间
- 实验或效果：在20多个任务中超越先前标记化方案和扩散基线，提供推理时灵活性

## 摘要（原文）

> Autoregressive policies offer a compelling foundation for scalable robot learning by enabling discrete abstraction, token-level reasoning, and flexible inference. However, applying autoregressive modeling to continuous robot actions requires an effective action tokenization scheme. Existing approaches either rely on analytical discretization methods that produce prohibitively long token sequences, or learned latent tokenizers that lack structure, limiting their compatibility with next-token prediction. In this work, we identify three desiderata for action tokenization - high compression, total decodability, and a left-to-right causally ordered token space - and introduce Ordered Action Tokenization (OAT), a learned action tokenizer that satisfies all three. OAT discretizes action chunks into an ordered sequence of tokens using transformer with registers, finite scalar quantization, and ordering-inducing training mechanisms. The resulting token space aligns naturally with autoregressive generation and enables prefix-based detokenization, yielding an anytime trade-off between inference cost and action fidelity. Across more than 20 tasks spanning four simulation benchmarks and real-world settings, autoregressive policies equipped with OAT consistently outperform prior tokenization schemes and diffusion-based baselines, while offering significantly greater flexibility at inference time.


---
layout: default
title: State Rank Dynamics in Linear Attention LLMs
---

# State Rank Dynamics in Linear Attention LLMs
**arXiv**：[2602.02195v1](https://arxiv.org/abs/2602.02195) · [PDF](https://arxiv.org/pdf/2602.02195.pdf)  
**作者**：Ao Sun, Hongtao Zhang, Heng Zhou, Yixuan Ma, Yiran Qin, Tongrui Su, Yan Liu, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He  

**一句话要点**：揭示线性注意力LLM状态秩分层现象并提出联合秩范数剪枝以降低KV缓存开销

**关键词**：线性注意力, 状态秩分层, KV缓存剪枝, 大语言模型, 模型压缩

## 3 点简述
- 核心问题：线性注意力LLM压缩状态内部动态不透明，影响模型理解与优化
- 方法要点：发现状态秩分层现象，低秩头与高秩头功能分化，提出零剪枝策略
- 实验或效果：实验验证动态一致性，剪枝减少38.9% KV缓存开销且保持精度

## 摘要（原文）

> Linear Attention Large Language Models (LLMs) offer a compelling recurrent formulation that compresses context into a fixed-size state matrix, enabling constant-time inference. However, the internal dynamics of this compressed state remain largely opaque. In this work, we present a comprehensive study on the runtime state dynamics of state-of-the-art Linear Attention models. We uncover a fundamental phenomenon termed State Rank Stratification, characterized by a distinct spectral bifurcation among linear attention heads: while one group maintains an effective rank oscillating near zero, the other exhibits rapid growth that converges to an upper bound. Extensive experiments across diverse inference contexts reveal that these dynamics remain strikingly consistent, indicating that the identity of a head,whether low-rank or high-rank,is an intrinsic structural property acquired during pre-training, rather than a transient state dependent on the input data. Furthermore, our diagnostic probes reveal a surprising functional divergence: low-rank heads are indispensable for model reasoning, whereas high-rank heads exhibit significant redundancy. Leveraging this insight, we propose Joint Rank-Norm Pruning, a zero-shot strategy that achieves a 38.9\% reduction in KV-cache overhead while largely maintaining model accuracy.


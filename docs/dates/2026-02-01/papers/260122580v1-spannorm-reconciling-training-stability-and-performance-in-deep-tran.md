---
layout: default
title: SpanNorm: Reconciling Training Stability and Performance in Deep Transformers
---

# SpanNorm: Reconciling Training Stability and Performance in Deep Transformers
**arXiv**：[2601.22580v1](https://arxiv.org/abs/2601.22580) · [PDF](https://arxiv.org/pdf/2601.22580.pdf)  
**作者**：Chao Wang, Bei Li, Jiaqi Zhang, Xinyu Liu, Yuchun Fan, Linkun Lyu, Xin Chen, Jingang Wang, Tong Xiao, Peng Pei, Xunliang Cai  

**一句话要点**：提出SpanNorm以解决深度Transformer中训练稳定性与性能的权衡问题。

**关键词**：Transformer架构, 归一化层, 训练稳定性, 信号传播, 残差连接, 混合专家模型

## 3 点简述
- 核心问题：PreNorm架构稳定但性能受限，PostNorm架构性能强但训练不稳定。
- 方法要点：SpanNorm结合残差连接和PostNorm式计算，稳定信号传播并提升性能。
- 实验或效果：在密集和MoE场景中优于标准归一化方案，理论分析支持其有效性。

## 摘要（原文）

> The success of Large Language Models (LLMs) hinges on the stable training of deep Transformer architectures. A critical design choice is the placement of normalization layers, leading to a fundamental trade-off: the ``PreNorm'' architecture ensures training stability at the cost of potential performance degradation in deep models, while the ``PostNorm'' architecture offers strong performance but suffers from severe training instability. In this work, we propose SpanNorm, a novel technique designed to resolve this dilemma by integrating the strengths of both paradigms. Structurally, SpanNorm establishes a clean residual connection that spans the entire transformer block to stabilize signal propagation, while employing a PostNorm-style computation that normalizes the aggregated output to enhance model performance. We provide a theoretical analysis demonstrating that SpanNorm, combined with a principled scaling strategy, maintains bounded signal variance throughout the network, preventing the gradient issues that plague PostNorm models, and also alleviating the representation collapse of PreNorm. Empirically, SpanNorm consistently outperforms standard normalization schemes in both dense and Mixture-of-Experts (MoE) scenarios, paving the way for more powerful and stable Transformer architectures.


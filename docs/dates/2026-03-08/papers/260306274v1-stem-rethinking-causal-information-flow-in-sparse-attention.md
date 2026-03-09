---
layout: default
title: Stem: Rethinking Causal Information Flow in Sparse Attention
---

# Stem: Rethinking Causal Information Flow in Sparse Attention
**arXiv**：[2603.06274v1](https://arxiv.org/abs/2603.06274) · [PDF](https://arxiv.org/pdf/2603.06274.pdf)  
**作者**：Lin Niu, Xin Luo, Linchuan Xie, Yifu Sun, Guanghua Yu, Jianchen Zhu, S Kevin Zhou  

**一句话要点**：提出Stem稀疏注意力模块，通过位置衰减和输出感知策略优化长上下文预填充计算效率。

**关键词**：稀疏注意力, 长上下文建模, 因果信息流, 预填充优化, 大语言模型

## 3 点简述
- 核心问题：自注意力二次复杂度限制LLM长上下文扩展，现有稀疏方法忽略因果架构的累积依赖。
- 方法要点：采用Token位置衰减策略和输出感知度量，保留初始令牌和高影响力令牌以对齐信息流。
- 实验或效果：评估显示Stem在减少计算和预填充延迟的同时保持高准确性。

## 摘要（原文）

> The quadratic computational complexity of self-attention remains a fundamental bottleneck for scaling Large Language Models (LLMs) to long contexts, particularly during the pre-filling phase. In this paper, we rethink the causal attention mechanism from the perspective of information flow. Due to causal constraints, tokens at initial positions participate in the aggregation of every subsequent token. However, existing sparse methods typically apply a uniform top-k selection across all token positions within a layer, ignoring the cumulative dependency of token information inherent in causal architectures. To address this, we propose Stem, a novel, plug-and-play sparsity module aligned with information flow. First, Stem employs the Token Position-Decay strategy, applying position-dependent top-k within each layer to retain initial tokens for recursive dependencies. Second, to preserve information-rich tokens, Stem utilizes the Output-Aware Metric. It prioritizes high-impact tokens based on approximate output magnitude. Extensive evaluations demonstrate that Stem achieves superior accuracy with reduced computation and pre-filling latency.


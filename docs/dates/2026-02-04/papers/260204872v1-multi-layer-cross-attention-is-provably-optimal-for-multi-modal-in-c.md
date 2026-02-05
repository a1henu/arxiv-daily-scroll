---
layout: default
title: Multi-layer Cross-Attention is Provably Optimal for Multi-modal In-context Learning
---

# Multi-layer Cross-Attention is Provably Optimal for Multi-modal In-context Learning
**arXiv**：[2602.04872v1](https://arxiv.org/abs/2602.04872) · [PDF](https://arxiv.org/pdf/2602.04872.pdf)  
**作者**：Nicholas Barnfield, Subhabrata Sen, Pragya Sur  

**一句话要点**：提出多层交叉注意力机制，证明其在多模态上下文学习中达到贝叶斯最优性能。

**关键词**：多模态学习, 上下文学习, 交叉注意力, 贝叶斯最优, 理论分析, Transformer架构

## 3 点简述
- 研究多模态上下文学习的理论机制，现有工作局限于单模态数据。
- 引入数学可处理框架，基于潜在因子模型建模多模态问题。
- 证明多层线性交叉注意力在梯度流优化下可恢复贝叶斯最优预测器。

## 摘要（原文）

> Recent progress has rapidly advanced our understanding of the mechanisms underlying in-context learning in modern attention-based neural networks. However, existing results focus exclusively on unimodal data; in contrast, the theoretical underpinnings of in-context learning for multi-modal data remain poorly understood. We introduce a mathematically tractable framework for studying multi-modal learning and explore when transformer-like architectures can recover Bayes-optimal performance in-context. To model multi-modal problems, we assume the observed data arises from a latent factor model. Our first result comprises a negative take on expressibility: we prove that single-layer, linear self-attention fails to recover the Bayes-optimal predictor uniformly over the task distribution. To address this limitation, we introduce a novel, linearized cross-attention mechanism, which we study in the regime where both the number of cross-attention layers and the context length are large. We show that this cross-attention mechanism is provably Bayes optimal when optimized using gradient flow. Our results underscore the benefits of depth for in-context learning and establish the provable utility of cross-attention for multi-modal distributions.


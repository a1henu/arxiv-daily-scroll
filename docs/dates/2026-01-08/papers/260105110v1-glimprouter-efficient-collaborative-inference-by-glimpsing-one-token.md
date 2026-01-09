---
layout: default
title: GlimpRouter: Efficient Collaborative Inference by Glimpsing One Token of Thoughts
---

# GlimpRouter: Efficient Collaborative Inference by Glimpsing One Token of Thoughts
**arXiv**：[2601.05110v1](https://arxiv.org/abs/2601.05110) · [PDF](https://arxiv.org/pdf/2601.05110.pdf)  
**作者**：Wenhao Zeng, Xuteng Zhang, Yuling Shi, Chao Hu, Yuting Chen, Beijun Shen, Xiaodong Gu  

**一句话要点**：提出GlimpRouter框架，通过首个令牌熵预测推理难度，实现高效协作推理。

**关键词**：协作推理, 推理路由, 令牌熵预测, 训练免费框架, 推理效率优化

## 3 点简述
- 核心问题：协作推理中难以动态分配大模型与小模型任务，现有路由策略开销大。
- 方法要点：基于首个令牌熵作为难度预测器，训练免费地路由推理步骤至大模型。
- 实验或效果：在多个基准上显著降低推理延迟并保持准确性，如AIME25上延迟减少25.9%。

## 摘要（原文）

> Large Reasoning Models (LRMs) achieve remarkable performance by explicitly generating multi-step chains of thought, but this capability incurs substantial inference latency and computational cost. Collaborative inference offers a promising solution by selectively allocating work between lightweight and large models, yet a fundamental challenge remains: determining when a reasoning step requires the capacity of a large model or the efficiency of a small model. Existing routing strategies either rely on local token probabilities or post-hoc verification, introducing significant inference overhead. In this work, we propose a novel perspective on step-wise collaboration: the difficulty of a reasoning step can be inferred from its very first token. Inspired by the "Aha Moment" phenomenon in LRMs, we show that the entropy of the initial token serves as a strong predictor of step difficulty. Building on this insight, we introduce GlimpRouter, a training-free step-wise collaboration framework. GlimpRouter employs a lightweight model to generate only the first token of each reasoning step and routes the step to a larger model only when the initial token entropy exceeds a threshold. Experiments on multiple benchmarks demonstrate that our approach significantly reduces inference latency while preserving accuracy. For instance, GlimpRouter attains a substantial 10.7% improvement in accuracy while reducing inference latency by 25.9% compared to a standalone large model on AIME25. These results suggest a simple yet effective mechanism for reasoning: allocating computation based on a glimpse of thought rather than full-step evaluation.


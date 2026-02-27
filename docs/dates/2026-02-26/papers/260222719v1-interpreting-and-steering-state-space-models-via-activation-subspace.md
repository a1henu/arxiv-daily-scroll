---
layout: default
title: Interpreting and Steering State-Space Models via Activation Subspace Bottlenecks
---

# Interpreting and Steering State-Space Models via Activation Subspace Bottlenecks
**arXiv**：[2602.22719v1](https://arxiv.org/abs/2602.22719) · [PDF](https://arxiv.org/pdf/2602.22719.pdf)  
**作者**：Vamshi Sunku Mohan, Kaustubh Gupta, Aneesha Das, Chandan Singh  

**一句话要点**：提出激活子空间瓶颈识别与标量乘干预方法，以提升状态空间模型的性能与可解释性。

**关键词**：状态空间模型, 机制可解释性, 激活子空间瓶颈, 测试时干预, 长上下文性能, Mamba模型

## 3 点简述
- 核心问题：状态空间模型（SSMs）在语言建模中高效但可解释性和可操控性不足。
- 方法要点：利用机制可解释性工具识别Mamba系列SSMs中的激活子空间瓶颈，并引入测试时标量乘干预。
- 实验或效果：在5个SSMs和6个基准测试中，干预平均提升性能8.27%，无需任务特定调优。

## 摘要（原文）

> State-space models (SSMs) have emerged as an efficient strategy for building powerful language models, avoiding the quadratic complexity of computing attention in transformers. Despite their promise, the interpretability and steerability of modern SSMs remain relatively underexplored. We take a major step in this direction by identifying activation subspace bottlenecks in the Mamba family of SSM models using tools from mechanistic interpretability. We then introduce a test-time steering intervention that simply multiplies the activations of the identified bottlenecks by a scalar. Across 5 SSMs and 6 diverse benchmarks, this intervention improves performance by an average of 8.27%, without requiring any task-specific tuning. Finally, we validate that the identified bottlenecks are indeed hindering performance by modifying them to yield an architecture we call Stable-Mamba, which achieves long-context performance gains when retrained from scratch.


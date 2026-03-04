---
layout: default
title: Next Embedding Prediction Makes World Models Stronger
---

# Next Embedding Prediction Makes World Models Stronger
**arXiv**：[2603.02765v1](https://arxiv.org/abs/2603.02765) · [PDF](https://arxiv.org/pdf/2603.02765.pdf)  
**作者**：George Bredis, Nikita Balagansky, Daniil Gavrilov, Ruslan Rakhimov  

**一句话要点**：提出NE-Dreamer，通过预测下一嵌入增强模型强化学习在部分可观测环境中的性能

**关键词**：模型强化学习, 部分可观测环境, 时间Transformer, 嵌入预测, 表示学习, 无解码器方法

## 3 点简述
- 核心问题：部分可观测高维域中，模型强化学习需有效捕获时间依赖以提升性能
- 方法要点：使用时间Transformer预测下一编码器嵌入，直接在表示空间优化时间预测对齐，无需解码器或重构损失
- 实验或效果：在DeepMind Control Suite匹配或超越DreamerV3，在DMLab记忆与空间推理任务中取得显著提升

## 摘要（原文）

> Capturing temporal dependencies is critical for model-based reinforcement learning (MBRL) in partially observable, high-dimensional domains. We introduce NE-Dreamer, a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space. This approach enables NE-Dreamer to learn coherent, predictive state representations without reconstruction losses or auxiliary supervision. On the DeepMind Control Suite, NE-Dreamer matches or exceeds the performance of DreamerV3 and leading decoder-free agents. On a challenging subset of DMLab tasks involving memory and spatial reasoning, NE-Dreamer achieves substantial gains. These results establish next-embedding prediction with temporal transformers as an effective, scalable framework for MBRL in complex, partially observable environments.


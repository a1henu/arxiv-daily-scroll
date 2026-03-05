---
layout: default
title: Specialization of softmax attention heads: insights from the high-dimensional single-location model
---

# Specialization of softmax attention heads: insights from the high-dimensional single-location model
**arXiv**：[2603.03993v1](https://arxiv.org/abs/2603.03993) · [PDF](https://arxiv.org/pdf/2603.03993.pdf)  
**作者**：M. Sagitova, O. Duranthon, L. Zdeborová  

**一句话要点**：提出高维单位置模型以分析多头注意力头专业化现象及优化性能

**关键词**：多头注意力, 头专业化, 训练动态, softmax注意力, 高维模型, 理论分析

## 3 点简述
- 核心问题：多头注意力头在训练中如何专业化，许多头保持冗余且学习相似表示。
- 方法要点：基于多索引和单位置回归框架，分析SGD下多头softmax注意力的训练动态。
- 实验或效果：引入Bayes-softmax注意力，在该设置中实现最优预测性能。

## 摘要（原文）

> Multi-head attention enables transformer models to represent multiple attention patterns simultaneously. Empirically, head specialization emerges in distinct stages during training, while many heads remain redundant and learn similar representations. We propose a theoretical model capturing this phenomenon, based on the multi-index and single-location regression frameworks. In the first part, we analyze the training dynamics of multi-head softmax attention under SGD, revealing an initial unspecialized phase followed by a multi-stage specialization phase in which different heads sequentially align with latent signal directions. In the second part, we study the impact of attention activation functions on performance. We show that softmax-1 significantly reduces noise from irrelevant heads. Finally, we introduce the Bayes-softmax attention, which achieves optimal prediction performance in this setting.


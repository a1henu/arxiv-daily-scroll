---
layout: default
title: Memory Caching: RNNs with Growing Memory
---

# Memory Caching: RNNs with Growing Memory
**arXiv**：[2602.24281v1](https://arxiv.org/abs/2602.24281) · [PDF](https://arxiv.org/pdf/2602.24281.pdf)  
**作者**：Ali Behrouz, Zeman Li, Yuan Deng, Peilin Zhong, Meisam Razaviyayn, Vahab Mirrokni  

**一句话要点**：提出Memory Caching技术以增强循环模型在长序列任务中的记忆能力

**关键词**：循环神经网络, 记忆缓存, 长序列建模, 语言建模, 长上下文理解

## 3 点简述
- 核心问题：循环模型因固定大小记忆在召回密集型任务中表现不佳
- 方法要点：通过缓存记忆状态检查点，使循环模型记忆容量随序列长度增长
- 实验或效果：在语言建模和长上下文理解任务中提升性能，接近Transformer

## 摘要（原文）

> Transformers have been established as the de-facto backbones for most recent advances in sequence modeling, mainly due to their growing memory capacity that scales with the context length. While plausible for retrieval tasks, it causes quadratic complexity and so has motivated recent studies to explore viable subquadratic recurrent alternatives. Despite showing promising preliminary results in diverse domains, such recurrent architectures underperform Transformers in recall-intensive tasks, often attributed to their fixed-size memory. In this paper, we introduce Memory Caching (MC), a simple yet effective technique that enhances recurrent models by caching checkpoints of their memory states (a.k.a. hidden states). Memory Caching allows the effective memory capacity of RNNs to grow with sequence length, offering a flexible trade-off that interpolates between the fixed memory (i.e., $O(L)$ complexity) of RNNs and the growing memory (i.e., $O(L^2)$ complexity) of Transformers. We propose four variants of MC, including gated aggregation and sparse selective mechanisms, and discuss their implications on both linear and deep memory modules. Our experimental results on language modeling, and long-context understanding tasks show that MC enhances the performance of recurrent models, supporting its effectiveness. The results of in-context recall tasks indicate that while Transformers achieve the best accuracy, our MC variants show competitive performance, close the gap with Transformers, and performs better than state-of-the-art recurrent models.


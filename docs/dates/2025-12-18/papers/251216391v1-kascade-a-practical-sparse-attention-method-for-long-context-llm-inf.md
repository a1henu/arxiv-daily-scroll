---
layout: default
title: Kascade: A Practical Sparse Attention Method for Long-Context LLM Inference
---

# Kascade: A Practical Sparse Attention Method for Long-Context LLM Inference
**arXiv**：[2512.16391v1](https://arxiv.org/abs/2512.16391) · [PDF](https://arxiv.org/pdf/2512.16391.pdf)  
**作者**：Dhruv Deshmukh, Saurabh Goyal, Nipun Kwatra, Ramachandran Ramjee  

**一句话要点**：提出Kascade稀疏注意力方法以加速长上下文LLM推理中的注意力计算

**关键词**：稀疏注意力, 长上下文推理, LLM加速, 训练无关方法, 注意力优化

## 3 点简述
- 核心问题：注意力是长上下文LLM推理延迟的主要来源，影响推理模型和RAG应用。
- 方法要点：基于训练后注意力稀疏性和键权重跨层稳定性，在锚层计算精确Top-k索引并在重用层复用。
- 实验效果：在H100 GPU上，解码注意力加速达4.1倍，预填充注意力加速2.2倍，长上下文基准测试精度接近稠密注意力。

## 摘要（原文）

> Attention is the dominant source of latency during long-context LLM inference, an increasingly popular workload with reasoning models and RAG. We propose Kascade, a training-free sparse attention method that leverages known observations such as 1) post-softmax attention is intrinsically sparse, and 2) the identity of high-weight keys is stable across nearby layers. Kascade computes exact Top-k indices in a small set of anchor layers, then reuses those indices in intermediate reuse layers. The anchor layers are selected algorithmically, via a dynamic-programming objective that maximizes cross-layer similarity over a development set, allowing easy deployment across models. The method incorporates efficient implementation constraints (e.g. tile-level operations), across both prefill and decode attention. The Top-k selection and reuse in Kascade is head-aware and we show in our experiments that this is critical for high accuracy. Kascade achieves up to 4.1x speedup in decode attention and 2.2x speedup in prefill attention over FlashAttention-3 baseline on H100 GPUs while closely matching dense attention accuracy on long-context benchmarks such as LongBench and AIME-24.


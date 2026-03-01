---
layout: default
title: Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators
---

# Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators
**arXiv**：[2602.22647v1](https://arxiv.org/abs/2602.22647) · [PDF](https://arxiv.org/pdf/2602.22647.pdf)  
**作者**：Zhengyang Su, Isay Katsman, Yueqi Wang, Ruining He, Lukasz Heldt, Raghunandan Keshavan, Shao-Chuan Wang, Xinyang Yi, Mingyan Gao, Onkar Dalal, Lichan Hong, Ed Chi, Ningren Han  

**一句话要点**：提出STATIC方法，通过向量化前缀树实现高效约束解码，用于加速器上的LLM生成式检索。

**关键词**：约束解码, 生成式检索, 前缀树向量化, 稀疏矩阵加速, 硬件加速器优化, 工业推荐系统

## 3 点简述
- 工业推荐系统需约束输出空间，但现有基于前缀树的解码方法在加速器上延迟高。
- STATIC将前缀树扁平化为静态CSR矩阵，将不规则树遍历转为向量化稀疏矩阵操作。
- 在大规模视频推荐平台部署，延迟开销极低，相比基线实现高达1033倍加速。

## 摘要（原文）

> Generative retrieval has emerged as a powerful paradigm for LLM-based recommendation. However, industrial recommender systems often benefit from restricting the output space to a constrained subset of items based on business logic (e.g. enforcing content freshness or product category), which standard autoregressive decoding cannot natively support. Moreover, existing constrained decoding methods that make use of prefix trees (Tries) incur severe latency penalties on hardware accelerators (TPUs/GPUs). In this work, we introduce STATIC (Sparse Transition Matrix-Accelerated Trie Index for Constrained Decoding), an efficient and scalable constrained decoding technique designed specifically for high-throughput LLM-based generative retrieval on TPUs/GPUs. By flattening the prefix tree into a static Compressed Sparse Row (CSR) matrix, we transform irregular tree traversals into fully vectorized sparse matrix operations, unlocking massive efficiency gains on hardware accelerators. We deploy STATIC on a large-scale industrial video recommendation platform serving billions of users. STATIC produces significant product metric impact with minimal latency overhead (0.033 ms per step and 0.25% of inference time), achieving a 948x speedup over a CPU trie implementation and a 47-1033x speedup over a hardware-accelerated binary-search baseline. Furthermore, the runtime overhead of STATIC remains extremely low across a wide range of practical configurations. To the best of our knowledge, STATIC enables the first production-scale deployment of strictly constrained generative retrieval. In addition, evaluation on academic benchmarks demonstrates that STATIC can considerably improve cold-start performance for generative retrieval. Our code is available at https://github.com/youtube/static-constraint-decoding.


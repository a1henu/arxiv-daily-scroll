---
layout: default
title: db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism
---

# db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism
**arXiv**：[2511.23113v1](https://arxiv.org/abs/2511.23113) · [PDF](https://arxiv.org/pdf/2511.23113.pdf)  
**作者**：Siqi Chen, Ke Hong, Tianchen Zhao, Ruiqi Xie, Zhenhua Zhu, Xudong Zhang, Yu Wang  

**一句话要点**：提出db-SP以解决视觉生成模型中稀疏注意力序列并行的工作负载不平衡问题

**关键词**：序列并行, 稀疏注意力, 视觉生成模型, 工作负载平衡, 扩散变换器

## 3 点简述
- 核心问题：序列并行应用于块稀疏注意力时，因稀疏度变化和块分布不规则导致工作负载严重失衡
- 方法要点：采用双级分区策略，在头和块维度实现近完美负载平衡，并动态调整并行度以适应稀疏模式变化
- 实验或效果：相比现有序列并行方法，平均端到端加速1.25倍，注意力部分加速1.40倍

## 摘要（原文）

> Scaling Diffusion Transformer (DiT) inference via sequence parallelism is critical for reducing latency in visual generation, but is severely hampered by workload imbalance when applied to models employing block-wise sparse attention. The imbalance stems from the inherent variation in sparsity across attention heads and the irregular distribution of dense blocks within the sparse mask, when sequence parallelism is applied along the head dimension (as in Ulysses) or the block dimension (as in Ring Attention). In this paper, we formalize a sparse imbalance ratio to quantify the imbalance, and propose db-SP, a sparsity-aware sequence parallelism technique that tackles the challenge. db-SP contains a dual-level partitioning approach that achieves near-perfect workload balance at both the head and block levels with negligible overhead. Furthermore, to handle the evolving sparsity patterns across denoising steps and layers, db-SP dynamically determines the parallel degrees for the head and block dimensions at runtime. Experimental results demonstrate that db-SP delivers an end-to-end speedup of 1.25x and an attention-specific speedup of 1.40x over state-of-the-art sequence parallel methods on average. Code is available at https://github.com/thu-nics/db-SP.


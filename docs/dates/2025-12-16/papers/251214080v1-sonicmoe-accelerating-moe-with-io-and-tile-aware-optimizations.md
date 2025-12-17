---
layout: default
title: SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations
---

# SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations
**arXiv**：[2512.14080v1](https://arxiv.org/abs/2512.14080) · [PDF](https://arxiv.org/pdf/2512.14080.pdf)  
**作者**：Wentao Guo, Mayank Mishra, Xinle Cheng, Ion Stoica, Tri Dao  

**一句话要点**：提出SonicMoE以加速MoE模型训练，通过内存高效算法、IO与计算重叠及令牌舍入优化解决激活内存和计算效率问题。

**关键词**：MoE模型加速, 内存优化, GPU内核设计, 令牌舍入, 训练效率

## 3 点简述
- 核心问题：细粒度MoE激活内存大、IO成本高，稀疏MoE分组GEMM填充浪费计算。
- 方法要点：设计内存高效算法减少激活缓存，GPU内核重叠IO与计算，令牌舍入最小化填充浪费。
- 实验或效果：在Hopper GPU上激活内存减少45%，计算吞吐提升1.86倍，高稀疏设置下内核执行加速1.16倍。

## 摘要（原文）

> Mixture of Experts (MoE) models have emerged as the de facto architecture for scaling up language models without significantly increasing the computational cost. Recent MoE models demonstrate a clear trend towards high expert granularity (smaller expert intermediate dimension) and higher sparsity (constant number of activated experts with higher number of total experts), which improve model quality per FLOP. However, fine-grained MoEs suffer from increased activation memory footprint and reduced hardware efficiency due to higher IO costs, while sparser MoEs suffer from wasted computations due to padding in Grouped GEMM kernels. In response, we propose a memory-efficient algorithm to compute the forward and backward passes of MoEs with minimal activation caching for the backward pass. We also design GPU kernels that overlap memory IO with computation benefiting all MoE architectures. Finally, we propose a novel "token rounding" method that minimizes the wasted compute due to padding in Grouped GEMM kernels. As a result, our method SonicMoE reduces activation memory by 45% and achieves a 1.86x compute throughput improvement on Hopper GPUs compared to ScatterMoE's BF16 MoE kernel for a fine-grained 7B MoE. Concretely, SonicMoE on 64 H100s achieves a training throughput of 213 billion tokens per day comparable to ScatterMoE's 225 billion tokens per day on 96 H100s for a 7B MoE model training with FSDP-2 using the lm-engine codebase. Under high MoE sparsity settings, our tile-aware token rounding algorithm yields an additional 1.16x speedup on kernel execution time compared to vanilla top-$K$ routing while maintaining similar downstream performance. We open-source all our kernels to enable faster MoE model training.


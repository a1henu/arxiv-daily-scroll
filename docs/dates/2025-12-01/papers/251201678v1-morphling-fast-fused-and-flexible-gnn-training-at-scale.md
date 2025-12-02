---
layout: default
title: Morphling: Fast, Fused, and Flexible GNN Training at Scale
---

# Morphling: Fast, Fused, and Flexible GNN Training at Scale
**arXiv**：[2512.01678v1](https://arxiv.org/abs/2512.01678) · [PDF](https://arxiv.org/pdf/2512.01678.pdf)  
**作者**：Anubhab, Rupesh Nasre  

**一句话要点**：提出Morphling代码合成器以解决GNN训练中图遍历与矩阵运算融合的性能瓶颈

**关键词**：图神经网络训练, 代码合成, 异构计算优化, 稀疏感知执行, 高性能计算

## 3 点简述
- GNN训练面临图遍历与矩阵运算的异构执行挑战，现有框架依赖通用内核导致性能低下
- Morphling通过编译GNN规范为后端专用实现，集成优化原语和运行时稀疏感知引擎
- 实验显示在CPU和GPU上平均提速20倍和19倍，内存消耗降低达15倍

## 摘要（原文）

> Graph Neural Networks (GNNs) present a fundamental hardware challenge by fusing irregular, memory-bound graph traversals with regular, compute-intensive dense matrix operations. While frameworks such as PyTorch Geometric (PyG) and Deep Graph Library (DGL) prioritize high-level usability, they fail to address these divergent execution characteristics. As a result, they rely on generic kernels that suffer from poor cache locality, excessive memory movement, and substantial intermediate allocations. To address these limitations, we present Morphling, a domain-specific code synthesizer designed to bridge this gap. Morphling compiles high-level GNN specifications into portable, backend-specialized implementations targeting OpenMP, CUDA, and MPI. It achieves this by instantiating a library of optimized, architecture-aware primitives tailored to each execution environment. Morphling also incorporates a runtime sparsity-aware execution engine that dynamically selects dense or sparse execution paths using input feature statistics, reducing unnecessary computation on zero-valued entries. We evaluate Morphling on eleven real-world datasets spanning diverse graph structures, feature dimensionalities, and sparsity regimes. The results show that Morphling improves per-epoch training throughput by an average of 20X on CPUs and 19X on GPUs over PyG and DGL, with peak speedups reaching 66X. Morphling's memory-efficient layouts further reduce peak memory consumption by up to 15X, enabling large-scale GNN training on commodity hardware. These findings demonstrate that specialized, architecture-aware code synthesis provides an effective and scalable path toward high-performance GNN execution across diverse parallel and distributed platforms.


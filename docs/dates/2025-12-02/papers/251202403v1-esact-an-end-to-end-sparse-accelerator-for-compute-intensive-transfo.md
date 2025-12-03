---
layout: default
title: ESACT: An End-to-End Sparse Accelerator for Compute-Intensive Transformers via Local Similarity
---

# ESACT: An End-to-End Sparse Accelerator for Compute-Intensive Transformers via Local Similarity
**arXiv**：[2512.02403v1](https://arxiv.org/abs/2512.02403) · [PDF](https://arxiv.org/pdf/2512.02403.pdf)  
**作者**：Hongxiang Liu, Zhifang Deng, Tong Pu, Shengli Lu  

**一句话要点**：提出ESACT，一种基于局部相似性的端到端稀疏加速器，用于计算密集型Transformer。

**关键词**：Transformer加速, 稀疏计算, 局部相似性, 硬件架构, 能效优化, 注意力机制

## 3 点简述
- 核心问题：Transformer计算成本高，现有加速器多仅利用注意力内行稀疏，忽略行间稀疏或依赖高开销全局相似性估计。
- 方法要点：通过SPLS机制，利用HLog量化预测局部注意力稀疏性，实现所有Transformer组件的端到端稀疏加速。
- 实验或效果：在26个基准测试中，SPLS减少总计算52.03%，精度损失小于1%；ESACT端到端能效达3.29 TOPS/W，注意力级能效优于SOTA。

## 摘要（原文）

> Transformers, composed of QKV generation, attention computation, and FFNs,
>   have become the dominant model across various domains due to their outstanding performance.
>   However, their high computational cost hinders efficient hardware deployment.
>   Sparsity offers a promising solution,
>   yet most existing accelerators exploit only intra-row sparsity in attention,
>   while few consider inter-row sparsity.
>   Approaches leveraging inter-row sparsity often rely on costly global similarity estimation,
>   which diminishes the acceleration benefits of sparsity,
>   and typically apply sparsity to only one or two transformer components.
>   Through careful analysis of the attention distribution and computation flow,
>   we observe that local similarity allows end-to-end sparse acceleration with lower computational overhead.
>   Motivated by this observation, we propose ESACT,
>   an end-to-end sparse accelerator for compute-intensive Transformers.
>   ESACT centers on the Sparsity Prediction with Local Similarity (SPLS) mechanism,
>   which leverages HLog quantization to accurately predict local attention sparsity prior to QK generation,
>   achieving efficient sparsity across all transformer components.
>   To support efficient hardware realization, we introduce three architectural innovations.
>   Experimental results on 26 benchmarks demonstrate that
>   SPLS reduces total computation by 52.03% with less than 1% accuracy loss.
>   ESACT achieves an end-to-end energy efficiency of 3.29 TOPS/W,
>   and improves attention-level energy efficiency by 2.95x and 2.26x over
>   SOTA attention accelerators SpAtten and Sanger, respectively.


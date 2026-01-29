---
layout: default
title: Beyond GEMM-Centric NPUs: Enabling Efficient Diffusion LLM Sampling
---

# Beyond GEMM-Centric NPUs: Enabling Efficient Diffusion LLM Sampling
**arXiv**：[2601.20706v1](https://arxiv.org/abs/2601.20706) · [PDF](https://arxiv.org/pdf/2601.20706.pdf)  
**作者**：Binglei Lou, Haoran Wu, Yao Lai, Jiayi Nie, Can Xiao, Xuan Guo, Rika Antonova, Robert Mullins, Aaron Zhao  

**一句话要点**：提出针对扩散大语言模型采样的NPU架构优化，以解决内存访问效率问题。

**关键词**：扩散大语言模型, NPU架构, 采样优化, 内存访问, 向量原语, 混合精度

## 3 点简述
- 核心问题：扩散大语言模型采样阶段内存负载高且访问不规则，占推理延迟70%。
- 方法要点：优化非GEMM向量原语、内存重用策略和混合精度内存层次。
- 实验或效果：在等效技术节点下，相比NVIDIA RTX A6000 GPU实现2.53倍加速。

## 摘要（原文）

> Diffusion Large Language Models (dLLMs) introduce iterative denoising to enable parallel token generation, but their sampling phase displays fundamentally different characteristics compared to GEMM-centric transformer layers. Profiling on modern GPUs reveals that sampling can account for up to 70% of total model inference latency-primarily due to substantial memory loads and writes from vocabulary-wide logits, reduction-based token selection, and iterative masked updates. These processes demand large on-chip SRAM and involve irregular memory accesses that conventional NPUs struggle to handle efficiently. To address this, we identify a set of critical instructions that an NPU architecture must specifically optimize for dLLM sampling. Our design employs lightweight non-GEMM vector primitives, in-place memory reuse strategies, and a decoupled mixed-precision memory hierarchy. Together, these optimizations deliver up to a 2.53x speedup over the NVIDIA RTX A6000 GPU under an equivalent nm technology node. We also open-source our cycle-accurate simulation and post-synthesis RTL verification code, confirming functional equivalence with current dLLM PyTorch implementations.


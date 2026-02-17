---
layout: default
title: WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity
---

# WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity
**arXiv**：[2602.14452v1](https://arxiv.org/abs/2602.14452) · [PDF](https://arxiv.org/pdf/2602.14452.pdf)  
**作者**：Lei Chen, Yuan Meng, Xiaoyu Zhan, Zhi Wang, Wenwu Zhu  

**一句话要点**：提出WiSparse，通过权重感知混合激活稀疏性提升LLM推理效率

**关键词**：大语言模型推理, 激活稀疏性, 权重感知, 免训练优化, 混合粒度分配

## 3 点简述
- 核心问题：现有免训练激活稀疏方法忽视权重与块间敏感性差异，导致性能不佳
- 方法要点：结合激活与权重信息，采用权重感知机制和混合粒度分配方案
- 实验或效果：在50%稀疏度下，保持Llama3.1 97%性能，推理速度提升21.4%

## 摘要（原文）

> Large Language Models (LLMs) offer strong capabilities but incur high inference costs due to dense computation and memory access. Training-free activation sparsity is a promising approach for efficient LLM inference, yet existing methods often rely solely on activation information and uniform sparsity ratios. This overlooks the critical interplay with weights and inter-block sensitivity variation, leading to suboptimal performance. We identify two key phenomena in modern LLMs: 1) less significant activations may align with highly important weights, and 2) sparsity sensitivity varies non-monotonically across model blocks. We propose Weight-aware Mixed-Granularity Training-free Activation Sparsity (WiSparse), which leverages both activation and weight information for adaptive sparsity allocation. Specifically, we introduce a weight-aware mechanism integrating activation magnitudes with precomputed weight norms to accurately identify salient channels. This is combined with a mixed-granularity allocation scheme: a global budget is distributed across blocks via evolutionary search to protect sensitive regions, then refined within blocks to minimize reconstruction error. We improve sparse kernels and demonstrate effectiveness on three representative models. Notably, at 50% sparsity, WiSparse preserves 97% of Llama3.1's dense performance, surpassing the strongest baseline by 2.23 percentage points while achieving a 21.4% acceleration in end-to-end inference speed. Our research advances the limits of training-free approaches for efficient LLM inference, pushing the boundaries of achievable speedup without training.


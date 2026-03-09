---
layout: default
title: EvoESAP: Non-Uniform Expert Pruning for Sparse MoE
---

# EvoESAP: Non-Uniform Expert Pruning for Sparse MoE
**arXiv**：[2603.06003v1](https://arxiv.org/abs/2603.06003) · [PDF](https://arxiv.org/pdf/2603.06003.pdf)  
**作者**：Zongfang Liu, Shengkun Tang, Boyang Sun, Zhiqiang Shen, Xin Yuan  

**一句话要点**：提出EvoESAP框架，通过非均匀层稀疏分配优化稀疏MoE模型剪枝，提升生成性能。

**关键词**：稀疏MoE剪枝, 非均匀稀疏分配, 进化搜索, 推测解码, 模型压缩, 专家网络

## 3 点简述
- 稀疏MoE模型部署受内存和吞吐量限制，现有剪枝方法多采用均匀层稀疏分配，影响性能。
- 引入ESAP度量，基于推测解码思想，廉价评估剪枝模型与完整模型的匹配度，无需昂贵自回归解码。
- EvoESAP在固定全局预算下，通过进化搜索优化非均匀层稀疏分配，在7B-30B模型上提升开放生成任务性能。

## 摘要（原文）

> Sparse Mixture-of-Experts (SMoE) language models achieve strong capability at low per-token compute, yet deployment remains memory- and throughput-bound because the full expert pool must be stored and served. Post-training expert pruning reduces this cost, but most methods focus on which experts to prune within each layer and default to a uniform layer-wise sparsity allocation, even though the allocation can strongly affect performance. We decouple pruning into within-layer expert ranking and across-layer budget allocation, and introduce \textbf{E}xpected \textbf{S}peculative \textbf{A}cceptance \textbf{P}roxy (\textbf{ESAP}), a speculative-decoding-inspired, teacher-forced metric that measures how well a pruned model matches the full model. ESAP is bounded and stable, enabling cheap comparison of many candidates without costly autoregressive decoding. Building on ESAP, we propose EvoESAP, an evolutionary searching framework that optimizes a non-uniform layer-wise sparsity allocation under a fixed global budget while holding the within-layer pruning order fixed, making it a plug-and-play method with criteria such as Frequency, EAN, SEER, and REAP. Across 7B--30B SMoE LLMs at 25\% and 50\% sparsity, EvoESAP consistently discovers non-uniform allocations that improve open-ended generation (up to \textbf{+19.6\%} on MATH-500 at 50\% sparsity) while preserving competitive multiple-choice accuracy compared with uniform pruning at the same sparsity.


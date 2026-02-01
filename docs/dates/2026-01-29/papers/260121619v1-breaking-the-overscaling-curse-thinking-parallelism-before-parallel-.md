---
layout: default
title: Breaking the Overscaling Curse: Thinking Parallelism Before Parallel Thinking
---

# Breaking the Overscaling Curse: Thinking Parallelism Before Parallel Thinking
**arXiv**：[2601.21619v1](https://arxiv.org/abs/2601.21619) · [PDF](https://arxiv.org/pdf/2601.21619.pdf)  
**作者**：Yiming Wang, Zhuosheng Zhang, Rui Wang  

**一句话要点**：提出T2方法以解决并行思维中的过缩放诅咒，通过样本级优化提升效率

**关键词**：并行思维, 过缩放诅咒, 样本异质性, 潜在表示, 解码优化, 成本效率

## 3 点简述
- 核心问题：系统级并行度分配导致样本异质性下的预算冗余，形成过缩放诅咒
- 方法要点：利用潜在表示在解码前估计每个样本的最优并行度，实现轻量级优化
- 实验或效果：T2显著降低成本，同时保持可比性能，提升并行思维效率

## 摘要（原文）

> Parallel thinking enhances LLM reasoning by multi-path sampling and aggregation. In system-level evaluations, a global parallelism level N is allocated to all samples, typically set large to maximize overall dataset accuracy. However, due to sample heterogeneity, some samples can achieve comparable performance with a smaller N'< N, causing budget redundancy. This incompatibility between system-level efficacy and sample-level efficiency constitutes the overscaling curse. In this paper, we formalize and quantify the overscaling curse, showing its universality and severity in practice, and analyze its trigger mechanism. We then propose a lightweight method, T2, to break the overscaling curse, which utilizes latent representations to estimate the optimal parallelism level for each sample before decoding. Experiments show that T2 significantly reduces cost while maintaining comparable performance, enabling more efficient parallel thinking.


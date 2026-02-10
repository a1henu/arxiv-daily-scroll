---
layout: default
title: Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction
---

# Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction
**arXiv**：[2602.08585v1](https://arxiv.org/abs/2602.08585) · [PDF](https://arxiv.org/pdf/2602.08585.pdf)  
**作者**：Ziyao Tang, Pengkun Jiao, Xinhang Chen, Wei Liu, Shiyong Li, Jingjing Chen  

**一句话要点**：提出LU-KV框架，通过边际效用优化KV缓存逐出以加速模型推理

**关键词**：KV缓存逐出, 注意力机制, 推理加速, 长序列建模, 边际效用优化

## 3 点简述
- 核心问题：现有KV缓存逐出方法忽视注意力头异质性，无法有效分配预算
- 方法要点：基于边际效用设计凸包松弛和贪心求解器，优化头级预算分配
- 实验或效果：在LongBench和RULER基准上，减少80%缓存大小且性能损失最小

## 摘要（原文）

> Given the quadratic complexity of attention, KV cache eviction is vital to accelerate model inference. Current KV cache eviction methods typically rely on instantaneous heuristic metrics, implicitly assuming that score magnitudes are consistent proxies for importance across all heads. However, this overlooks the heterogeneity in predictive fidelity across attention heads. While certain heads prioritize the instantaneous contribution of tokens, others are dedicated to capturing long-horizon utility. In this paper, we propose that optimal budget allocation should be governed by the marginal utility in preserving long-term semantic information. Based on this insight, we propose LU-KV, a novel framework that optimizes head-level budget allocation through a convex-hull relaxation and a marginal-utility-based greedy solver to achieve near-optimal precision. Furthermore, we implement a data-driven offline profiling protocol to facilitate the practical deployment of LU-KV. Extensive evaluations on LongBench and RULER benchmarks demonstrate that LU-KV achieves an 80% reduction in KV cache size with minimal performance degradation, while simultaneously reducing inference latency and GPU memory footprint.


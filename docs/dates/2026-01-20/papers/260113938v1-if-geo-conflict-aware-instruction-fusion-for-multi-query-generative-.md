---
layout: default
title: IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization
---

# IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization
**arXiv**：[2601.13938v1](https://arxiv.org/abs/2601.13938) · [PDF](https://arxiv.org/pdf/2601.13938.pdf)  
**作者**：Heyang Zhou, JiaJia Chen, Xiaolu Chen, Jie Bao, Zhen Chen, Yong Liao  

**一句话要点**：提出IF-GEO框架以解决多查询生成引擎优化中的冲突修订问题

**关键词**：生成引擎优化, 多查询优化, 冲突感知融合, 风险感知稳定性, 内容修订

## 3 点简述
- 核心问题：多查询优化中，异质查询的冲突修订需求在有限内容预算下难以协调
- 方法要点：采用'发散-收敛'框架，挖掘查询偏好并通过冲突感知指令融合合成全局修订蓝图
- 实验或效果：在多查询基准测试中实现显著性能提升，并保持跨检索场景的鲁棒性

## 摘要（原文）

> As Generative Engines revolutionize information retrieval by synthesizing direct answers from retrieved sources, ensuring source visibility becomes a significant challenge. Improving it through targeted content revisions is a practical strategy termed Generative Engine Optimization (GEO). However, optimizing a document for diverse queries presents a constrained optimization challenge where heterogeneous queries often impose conflicting and competing revision requirements under a limited content budget. To address this challenge, we propose IF-GEO, a "diverge-then-converge" framework comprising two phases: (i) mining distinct optimization preferences from representative latent queries; (ii) synthesizing a Global Revision Blueprint for guided editing by coordinating preferences via conflict-aware instruction fusion. To explicitly quantify IF-GEO's objective of cross-query stability, we introduce risk-aware stability metrics. Experiments on multi-query benchmarks demonstrate that IF-GEO achieves substantial performance gains while maintaining robustness across diverse retrieval scenarios.


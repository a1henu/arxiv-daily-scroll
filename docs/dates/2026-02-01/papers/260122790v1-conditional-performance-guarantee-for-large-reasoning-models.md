---
layout: default
title: Conditional Performance Guarantee for Large Reasoning Models
---

# Conditional Performance Guarantee for Large Reasoning Models
**arXiv**：[2601.22790v1](https://arxiv.org/abs/2601.22790) · [PDF](https://arxiv.org/pdf/2601.22790.pdf)  
**作者**：Jianguo Huang, Hao Zeng, Bingyi Jing, Hongxin Wei, Bo An  

**一句话要点**：提出G-PAC推理框架，通过分组实现条件性能保证以提升大型推理模型效率

**关键词**：大型推理模型, 条件性能保证, 分组推理, 风险控制, 计算效率

## 3 点简述
- 核心问题：大型推理模型计算成本高，现有PAC推理仅提供边际保证，缺乏条件覆盖
- 方法要点：基于输入空间分组，提出G-PAC和C-PAC实现组级条件风险控制
- 实验或效果：在多样推理基准上验证组条件风险控制，同时显著节省计算成本

## 摘要（原文）

> Large reasoning models have shown strong performance through extended chain-of-thought reasoning, yet their computational cost remains significant. Probably approximately correct (PAC) reasoning provides statistical guarantees for efficient reasoning by adaptively switching between thinking and non-thinking models, but the guarantee holds only in the marginal case and does not provide exact conditional coverage. We propose G-PAC reasoning, a practical framework that provides PAC-style guarantees at the group level by partitioning the input space. We develop two instantiations: Group PAC (G-PAC) reasoning for known group structures and Clustered PAC (C-PAC) reasoning for unknown groupings. We prove that both G-PAC and C-PAC achieve group-conditional risk control, and that grouping can strictly improve efficiency over marginal PAC reasoning in heterogeneous settings. Our experiments on diverse reasoning benchmarks demonstrate that G-PAC and C-PAC successfully achieve group-conditional risk control while maintaining substantial computational savings.


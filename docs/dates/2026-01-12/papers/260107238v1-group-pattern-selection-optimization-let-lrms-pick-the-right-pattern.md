---
layout: default
title: Group Pattern Selection Optimization: Let LRMs Pick the Right Pattern for Reasoning
---

# Group Pattern Selection Optimization: Let LRMs Pick the Right Pattern for Reasoning
**arXiv**：[2601.07238v1](https://arxiv.org/abs/2601.07238) · [PDF](https://arxiv.org/pdf/2601.07238.pdf)  
**作者**：Hanbin Wang, Jingwei Song, Jinpeng Li, Fei Mi, Lifeng Shang  

**一句话要点**：提出GPSO框架，通过强化学习优化大型推理模型选择最优推理模式以提升性能。

**关键词**：大型推理模型, 推理模式选择, 强化学习优化, 注意力掩码, 性能提升

## 3 点简述
- 核心问题：大型推理模型默认推理模式常非最优，导致性能方差大。
- 方法要点：GPSO结合多模式探索、验证器引导选择和注意力掩码，学习问题到最优模式的映射。
- 实验或效果：在多种模型和基准上实现一致显著性能提升，增强推理鲁棒性和适应性。

## 摘要（原文）

> Large reasoning models (LRMs) exhibit diverse high-level reasoning patterns (e.g., direct solution, reflection-and-verification, and exploring multiple solutions), yet prevailing training recipes implicitly bias models toward a limited set of dominant patterns. Through a systematic analysis, we identify substantial accuracy variance across these patterns on mathematics and science benchmarks, revealing that a model's default reasoning pattern is often sub-optimal for a given problem. To address this, we introduce Group Pattern Selection Optimization (GPSO), a reinforcement learning framework that extends GRPO by incorporating multi-pattern rollouts, verifier-guided optimal pattern selection per problem, and attention masking during optimization to prevent the leakage of explicit pattern suffixes into the learned policy. By exploring a portfolio of diverse reasoning strategies and optimizing the policy on the most effective ones, GPSO enables the model to internalize the mapping from problem characteristics to optimal reasoning patterns. Extensive experiments demonstrate that GPSO delivers consistent and substantial performance gains across various model backbones and benchmarks, effectively mitigating pattern sub-optimality and fostering more robust, adaptable reasoning. All data and codes are available at https://github.com/wanghanbinpanda/GPSO.


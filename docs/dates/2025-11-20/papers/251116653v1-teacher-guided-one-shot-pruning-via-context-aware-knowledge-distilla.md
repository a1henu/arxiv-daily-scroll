---
layout: default
title: Teacher-Guided One-Shot Pruning via Context-Aware Knowledge Distillation
---

# Teacher-Guided One-Shot Pruning via Context-Aware Knowledge Distillation
**arXiv**：[2511.16653v1](https://arxiv.org/abs/2511.16653) · [PDF](https://arxiv.org/pdf/2511.16653.pdf)  
**作者**：Md. Samiul Alim, Sharjil Khan, Amrijit Biswas, Fuad Rahman, Shafin Rahman, Nabeel Mohammed  

**一句话要点**：提出教师引导的一次性剪枝框架，通过上下文感知知识蒸馏解决高计算开销问题

**关键词**：神经网络剪枝, 知识蒸馏, 一次性剪枝, 上下文感知, 稀疏训练

## 3 点简述
- 非结构化剪枝需迭代训练-剪枝-重训练，计算开销大
- 在重要性评分中集成教师梯度，一次性剪枝保留关键参数
- 实验显示高稀疏度下性能优于基线，计算效率高

## 摘要（原文）

> Unstructured pruning remains a powerful strategy for compressing deep neural networks, yet it often demands iterative train-prune-retrain cycles, resulting in significant computational overhead. To address this challenge, we introduce a novel teacher-guided pruning framework that tightly integrates Knowledge Distillation (KD) with importance score estimation. Unlike prior approaches that apply KD as a post-pruning recovery step, our method leverages gradient signals informed by the teacher during importance score calculation to identify and retain parameters most critical for both task performance and knowledge transfer. Our method facilitates a one-shot global pruning strategy that efficiently eliminates redundant weights while preserving essential representations. After pruning, we employ sparsity-aware retraining with and without KD to recover accuracy without reactivating pruned connections. Comprehensive experiments across multiple image classification benchmarks, including CIFAR-10, CIFAR-100, and TinyImageNet, demonstrate that our method consistently achieves high sparsity levels with minimal performance degradation. Notably, our approach outperforms state-of-the-art baselines such as EPG and EPSD at high sparsity levels, while offering a more computationally efficient alternative to iterative pruning schemes like COLT. The proposed framework offers a computation-efficient, performance-preserving solution well suited for deployment in resource-constrained environments.


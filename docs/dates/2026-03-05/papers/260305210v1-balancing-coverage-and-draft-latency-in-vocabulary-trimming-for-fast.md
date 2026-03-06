---
layout: default
title: Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding
---

# Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding
**arXiv**：[2603.05210v1](https://arxiv.org/abs/2603.05210) · [PDF](https://arxiv.org/pdf/2603.05210.pdf)  
**作者**：Ofir Ben Shoham  

**一句话要点**：提出词汇表裁剪方法以平衡覆盖率和延迟，加速推测解码中的草稿模型推理。

**关键词**：推测解码, 词汇表裁剪, 延迟优化, 覆盖率约束, 草稿模型加速

## 3 点简述
- 核心问题：草稿模型词汇表大小在推测解码中存在覆盖率与延迟的权衡。
- 方法要点：将词汇表选择建模为约束优化，基于训练数据覆盖率和架构感知FLOPs估计延迟。
- 实验或效果：在领域特定任务上实现最高16%延迟降低和20%吞吐量提升。

## 摘要（原文）

> Speculative decoding accelerates inference for Large Language Models by using a lightweight draft model to propose candidate tokens that are verified in parallel by a larger target model. Prior work shows that the draft model often dominates speculative decoding latency, since it generates tokens sequentially and incurs high cost from its language modeling head as vocabulary size grows. This exposes a fundamental trade-off in draft model design: larger vocabularies improve token coverage and agreement with the target model, but incur higher draft latency, while smaller vocabularies reduce latency at the risk of missing tokens required for accurate draft generation. We address this trade-off through vocabulary trimming for draft models, motivated by the observation that domain-specific workloads use only a small fraction of the full vocabulary. We cast draft vocabulary selection as a constrained optimization problem that balances token coverage and draft latency. Coverage is computed over assistant responses in the training data, while latency is estimated using architecture-aware FLOPs that capture the cost of the language modeling head as a function of vocabulary size. We optimize a utility function with a Tree-structured Parzen Estimator to efficiently explore the coverage-latency Pareto frontier under a minimum coverage constraint. Experiments show improved speculative decoding throughput while reducing draft vocabularies by up to 97% with high coverage. On domain-specific tasks, we achieve up to 16% latency reduction and 20% throughput improvement, and up to 6.7% throughput gains on diverse out-of-distribution tasks.


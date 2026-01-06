---
layout: default
title: Placement Semantics for Distributed Deep Learning: A Systematic Framework for Analyzing Parallelism Strategies
---

# Placement Semantics for Distributed Deep Learning: A Systematic Framework for Analyzing Parallelism Strategies
**arXiv**：[2601.02311v1](https://arxiv.org/abs/2601.02311) · [PDF](https://arxiv.org/pdf/2601.02311.pdf)  
**作者**：Deep Pankajbhai Mehta  

**一句话要点**：提出放置语义框架以系统分析分布式深度学习中的并行策略

**关键词**：分布式深度学习, 并行策略, 放置语义, 内存优化, 通信分析, 训练状态管理

## 3 点简述
- 核心问题：缺乏统一框架预测并行策略行为，依赖试错选择
- 方法要点：通过放置语义指定训练状态在设备上的分布模式，推导内存和通信量
- 实验或效果：预测结果与已发表数据一致，验证框架准确性

## 摘要（原文）

> Training large language models requires distributing computation across many accelerators, yet practitioners select parallelism strategies (data, tensor, pipeline, ZeRO) through trial and error because no unified systematic framework predicts their behavior. We introduce placement semantics: each strategy is specified by how it places four training states (parameters, optimizer, gradients, activations) across devices using five modes (replicated, sharded, sharded-with-gather, materialized, offloaded). From placement alone, without implementation details, we derive memory consumption and communication volume. Our predictions match published results exactly: ZeRO-3 uses 8x less memory than data parallelism at 1.5x communication cost, as reported in the original paper. We prove two conditions (gradient integrity, state consistency) are necessary and sufficient for distributed training to match single-device results, and provide composition rules for combining strategies safely. The framework unifies ZeRO Stages 1-3, Fully Sharded Data Parallel (FSDP), tensor parallelism, and pipeline parallelism as instances with different placement choices.


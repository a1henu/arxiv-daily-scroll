---
layout: default
title: GraphAllocBench: A Flexible Benchmark for Preference-Conditioned Multi-Objective Policy Learning
---

# GraphAllocBench: A Flexible Benchmark for Preference-Conditioned Multi-Objective Policy Learning
**arXiv**：[2601.20753v1](https://arxiv.org/abs/2601.20753) · [PDF](https://arxiv.org/pdf/2601.20753.pdf)  
**作者**：Zhiheng Jiang, Yunzhe Wang, Ryan Marr, Ellen Novoseller, Benjamin T. Files, Volkan Ustun  

**一句话要点**：提出GraphAllocBench基准以解决偏好条件多目标策略学习在现实与可扩展性上的不足

**关键词**：多目标强化学习, 偏好条件策略学习, 图资源分配, 基准测试, 评估指标, 图神经网络

## 3 点简述
- 核心问题：现有偏好条件多目标策略学习基准局限于玩具任务和固定环境，缺乏现实性和可扩展性。
- 方法要点：基于图资源分配沙盒环境CityPlannerEnv构建灵活基准，支持多样目标函数、偏好条件和可扩展性。
- 实验或效果：通过实验揭示现有多目标强化学习方法的局限性，并引入新评估指标PNDS和OS以补充超体积度量。

## 摘要（原文）

> Preference-Conditioned Policy Learning (PCPL) in Multi-Objective Reinforcement Learning (MORL) aims to approximate diverse Pareto-optimal solutions by conditioning policies on user-specified preferences over objectives. This enables a single model to flexibly adapt to arbitrary trade-offs at run-time by producing a policy on or near the Pareto front. However, existing benchmarks for PCPL are largely restricted to toy tasks and fixed environments, limiting their realism and scalability. To address this gap, we introduce GraphAllocBench, a flexible benchmark built on a novel graph-based resource allocation sandbox environment inspired by city management, which we call CityPlannerEnv. GraphAllocBench provides a rich suite of problems with diverse objective functions, varying preference conditions, and high-dimensional scalability. We also propose two new evaluation metrics -- Proportion of Non-Dominated Solutions (PNDS) and Ordering Score (OS) -- that directly capture preference consistency while complementing the widely used hypervolume metric. Through experiments with Multi-Layer Perceptrons (MLPs) and graph-aware models, we show that GraphAllocBench exposes the limitations of existing MORL approaches and paves the way for using graph-based methods such as Graph Neural Networks in complex, high-dimensional combinatorial allocation tasks. Beyond its predefined problem set, GraphAllocBench enables users to flexibly vary objectives, preferences, and allocation rules, establishing it as a versatile and extensible benchmark for advancing PCPL. Code: https://anonymous.4open.science/r/GraphAllocBench


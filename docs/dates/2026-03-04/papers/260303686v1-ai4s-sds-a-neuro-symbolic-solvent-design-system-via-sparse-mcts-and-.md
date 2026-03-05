---
layout: default
title: AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment
---

# AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment
**arXiv**：[2603.03686v1](https://arxiv.org/abs/2603.03686) · [PDF](https://arxiv.org/pdf/2603.03686.pdf)  
**作者**：Jiangyu Chen  

**一句话要点**：提出AI4S-SDS神经符号框架，通过稀疏MCTS和可微物理对齐解决化学配方自动设计中的探索与物理约束问题。

**关键词**：神经符号系统, 稀疏蒙特卡洛树搜索, 可微物理引擎, 化学配方设计, 多智能体协作, 探索多样性

## 3 点简述
- 核心问题：化学配方自动设计需处理高维组合空间，现有LLM代理面临上下文窗口限制和路径依赖探索导致的模式崩溃。
- 方法要点：集成多智能体协作与稀疏状态存储机制，结合全局-局部搜索策略和可微物理引擎优化混合比例。
- 实验或效果：在HSP物理约束下实现全有效性，提升探索多样性，初步光刻实验发现性能优于商业基准的新配方。

## 摘要（原文）

> Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.


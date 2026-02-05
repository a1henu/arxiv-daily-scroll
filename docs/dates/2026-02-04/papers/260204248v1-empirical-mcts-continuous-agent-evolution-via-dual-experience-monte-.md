---
layout: default
title: Empirical-MCTS: Continuous Agent Evolution via Dual-Experience Monte Carlo Tree Search
---

# Empirical-MCTS: Continuous Agent Evolution via Dual-Experience Monte Carlo Tree Search
**arXiv**：[2602.04248v1](https://arxiv.org/abs/2602.04248) · [PDF](https://arxiv.org/pdf/2602.04248.pdf)  
**作者**：Hao Lu, Haoyuan Huang, Yulin Zhou, Chen Li, Ningxin Zhu  

**一句话要点**：提出Empirical-MCTS框架，通过双经验MCTS实现连续代理进化，以解决推理任务中状态丢失问题。

**关键词**：蒙特卡洛树搜索, 经验积累, 连续学习, 推理增强, 内存优化, 元提示进化

## 3 点简述
- 核心问题：现有MCTS方法为无状态，丢弃成功推理模式，无法模拟人类经验积累。
- 方法要点：引入双循环框架，结合PE-EMP和内存优化代理，实现本地探索与全局记忆优化。
- 实验效果：在AIME25等复杂推理基准上显著优于无状态MCTS和经验驱动代理。

## 摘要（原文）

> Inference-time scaling strategies, particularly Monte Carlo Tree Search (MCTS), have significantly enhanced the reasoning capabilities of Large Language Models (LLMs). However, current approaches remain predominantly stateless, discarding successful reasoning patterns after each problem instance and failing to mimic the empirical accumulation of wisdom characteristic of human problem-solving. To bridge this gap, we introduce Empirical-MCTS, a dual-loop framework that transforms stateless search into a continuous, non-parametric learning process. The framework unifies local exploration with global memory optimization through two novel mechanisms: Pairwise-Experience-Evolutionary Meta-Prompting (PE-EMP) and a Memory Optimization Agent. PE-EMP functions as a reflexive optimizer within the local search, utilizing pairwise feedback to dynamically synthesize adaptive criteria and evolve meta-prompts (system prompts) in real-time. Simultaneously, the Memory Optimization Agent manages a global repository as a dynamic policy prior, employing atomic operations to distill high-quality insights across problems. Extensive evaluations on complex reasoning benchmarks, including AIME25, ARC-AGI-2, and MathArena Apex, demonstrate that Empirical-MCTS significantly outperforms both stateless MCTS strategies and standalone experience-driven agents. These results underscore the critical necessity of coupling structured search with empirical accumulation for mastering complex, open-ended reasoning tasks.


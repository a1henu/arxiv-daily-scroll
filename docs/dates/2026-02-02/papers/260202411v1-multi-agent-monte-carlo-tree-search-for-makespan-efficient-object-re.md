---
layout: default
title: Multi-Agent Monte Carlo Tree Search for Makespan-Efficient Object Rearrangement in Cluttered Spaces
---

# Multi-Agent Monte Carlo Tree Search for Makespan-Efficient Object Rearrangement in Cluttered Spaces
**arXiv**：[2602.02411v1](https://arxiv.org/abs/2602.02411) · [PDF](https://arxiv.org/pdf/2602.02411.pdf)  
**作者**：Hanwen Ren, Junyong Kim, Aathman Tharmasanthiran, Ahmed H. Qureshi  

**一句话要点**：提出CAM-MCTS框架，用于杂乱环境中多智能体高效完成非单调物体重排任务

**关键词**：多智能体规划, 蒙特卡洛树搜索, 物体重排, 非单调任务, 完工时间优化, 异步执行

## 3 点简述
- 核心问题：杂乱环境中物体相互阻挡，需临时重排，传统方法多针对单调实例，效率低
- 方法要点：结合集中式任务分配与异步执行，通过前瞻成本估计减少空闲时间，优化全局规划
- 实验或效果：在单调和非单调任务中验证，相比基线持续降低完工时间，并在真实多智能体系统上展示鲁棒性

## 摘要（原文）

> Object rearrangement planning in complex, cluttered environments is a common challenge in warehouses, households, and rescue sites. Prior studies largely address monotone instances, whereas real-world tasks are often non-monotone-objects block one another and must be temporarily relocated to intermediate positions before reaching their final goals. In such settings, effective multi-agent collaboration can substantially reduce the time required to complete tasks. This paper introduces Centralized, Asynchronous, Multi-agent Monte Carlo Tree Search (CAM-MCTS), a novel framework for general-purpose makespan-efficient object rearrangement planning in challenging environments. CAM-MCTS combines centralized task assignment-where agents remain aware of each other's intended actions to facilitate globally optimized planning-with an asynchronous task execution strategy that enables agents to take on new tasks at appropriate time steps, rather than waiting for others, guided by a one-step look-ahead cost estimate. This design minimizes idle time, prevents unnecessary synchronization delays, and enhances overall system efficiency. We evaluate CAM-MCTS across a diverse set of monotone and non-monotone tasks in cluttered environments, demonstrating consistent reductions in makespan compared to strong baselines. Finally, we validate our approach on a real-world multi-agent system under different configurations, further confirming its effectiveness and robustness.


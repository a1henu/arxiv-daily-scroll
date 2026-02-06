---
layout: default
title: Learning to Share: Selective Memory for Efficient Parallel Agentic Systems
---

# Learning to Share: Selective Memory for Efficient Parallel Agentic Systems
**arXiv**：[2602.05965v1](https://arxiv.org/abs/2602.05965) · [PDF](https://arxiv.org/pdf/2602.05965.pdf)  
**作者**：Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, Song Wang, Mubarak Shah  

**一句话要点**：提出学习共享机制以解决并行智能体系统中的计算冗余问题

**关键词**：并行智能体系统, 共享记忆机制, 强化学习控制, 计算效率优化, 选择性信息复用

## 3 点简述
- 并行智能体系统存在重复计算子问题的效率瓶颈
- 引入全局记忆库与轻量控制器实现选择性跨团队信息复用
- 实验显示在保持性能的同时显著减少运行时间

## 摘要（原文）

> Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems. Project page: https://joefioresi718.github.io/LTS_webpage/


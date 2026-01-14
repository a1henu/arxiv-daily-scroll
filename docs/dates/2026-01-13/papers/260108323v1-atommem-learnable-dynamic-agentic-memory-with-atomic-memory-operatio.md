---
layout: default
title: AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation
---

# AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation
**arXiv**：[2601.08323v1](https://arxiv.org/abs/2601.08323) · [PDF](https://arxiv.org/pdf/2601.08323.pdf)  
**作者**：Yupeng Huo, Yaxi Lu, Zhong Zhang, Haotian Chen, Yankai Lin  

**一句话要点**：提出AtomMem，通过原子CRUD操作将记忆管理重构为动态决策问题，以解决长视野任务中静态记忆工作流的局限性。

**关键词**：代理记忆, 动态决策, 原子操作, 强化学习, 长上下文任务

## 3 点简述
- 核心问题：现有代理记忆机制依赖静态手工工作流，限制了性能和泛化能力。
- 方法要点：将高级记忆过程分解为原子CRUD操作，结合监督微调和强化学习训练自主策略。
- 实验或效果：在3个长上下文基准测试中，AtomMem-8B优于静态工作流方法，训练动态显示任务对齐策略。

## 摘要（原文）

> Equipping agents with memory is essential for solving real-world long-horizon problems. However, most existing agent memory mechanisms rely on static and hand-crafted workflows. This limits the performance and generalization ability of these memory designs, which highlights the need for a more flexible, learning-based memory framework. In this paper, we propose AtomMem, which reframes memory management as a dynamic decision-making problem. We deconstruct high-level memory processes into fundamental atomic CRUD (Create, Read, Update, Delete) operations, transforming the memory workflow into a learnable decision process. By combining supervised fine-tuning with reinforcement learning, AtomMem learns an autonomous, task-aligned policy to orchestrate memory behaviors tailored to specific task demands. Experimental results across 3 long-context benchmarks demonstrate that the trained AtomMem-8B consistently outperforms prior static-workflow memory methods. Further analysis of training dynamics shows that our learning-based formulation enables the agent to discover structured, task-aligned memory management strategies, highlighting a key advantage over predefined routines.


---
layout: default
title: FutureWeaver: Planning Test-Time Compute for Multi-Agent Systems with Modularized Collaboration
---

# FutureWeaver: Planning Test-Time Compute for Multi-Agent Systems with Modularized Collaboration
**arXiv**：[2512.11213v1](https://arxiv.org/abs/2512.11213) · [PDF](https://arxiv.org/pdf/2512.11213.pdf)  
**作者**：Dongwon Jung, Peng Shi, Yi Zhang  

**一句话要点**：提出FutureWeaver框架以优化多智能体系统在固定预算下的测试时计算分配

**关键词**：多智能体系统, 测试时计算, 模块化协作, 计算分配优化, 自玩反思, 双级规划

## 3 点简述
- 核心问题：多智能体系统中缺乏原则性机制来分配计算以促进协作，或扩展测试时计算到交互中
- 方法要点：引入模块化协作，通过自玩反思抽象可重用工作流，并采用双级规划架构优化计算分配
- 实验或效果：在复杂智能体基准测试中，FutureWeaver在不同预算设置下均优于基线，验证其有效性

## 摘要（原文）

> Scaling test-time computation improves large language model performance without additional training. Recent work demonstrates that techniques such as repeated sampling, self-verification, and self-reflection can significantly enhance task success by allocating more inference-time compute. However, applying these techniques across multiple agents in a multi-agent system is difficult: there does not exist principled mechanisms to allocate compute to foster collaboration among agents, to extend test-time scaling to collaborative interactions, or to distribute compute across agents under explicit budget constraints. To address this gap, we propose FutureWeaver, a framework for planning and optimizing test-time compute allocation in multi-agent systems under fixed budgets. FutureWeaver introduces modularized collaboration, formalized as callable functions that encapsulate reusable multi-agent workflows. These modules are automatically derived through self-play reflection by abstracting recurring interaction patterns from past trajectories. Building on these modules, FutureWeaver employs a dual-level planning architecture that optimizes compute allocation by reasoning over the current task state while also speculating on future steps. Experiments on complex agent benchmarks demonstrate that FutureWeaver consistently outperforms baselines across diverse budget settings, validating its effectiveness for multi-agent collaboration in inference-time optimization.


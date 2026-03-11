---
layout: default
title: AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents
---

# AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents
**arXiv**：[2603.09716v1](https://arxiv.org/abs/2603.09716) · [PDF](https://arxiv.org/pdf/2603.09716.pdf)  
**作者**：Xiaoxing Wang, Ning Liao, Shikun Wei, Chen Tang, Feiyu Xiong  

**一句话要点**：提出AutoAgent框架，通过认知进化与弹性记忆编排解决自适应智能体在动态环境中的决策与学习问题。

**关键词**：自适应智能体, 认知进化, 弹性记忆编排, 上下文决策, 多智能体框架, 经验学习

## 3 点简述
- 核心问题：现有自主智能体框架存在静态认知、工作流依赖和上下文利用低效，限制在开放非平稳环境中的适应性。
- 方法要点：结合演化认知、实时上下文决策和弹性记忆编排，实现闭环认知进化，无需外部重训练。
- 实验或效果：在检索增强推理、工具增强基准和具身任务中，提升任务成功率、工具使用效率和协作鲁棒性。

## 摘要（原文）

> Autonomous agent frameworks still struggle to reconcile long-term experiential learning with real-time, context-sensitive decision-making. In practice, this gap appears as static cognition, rigid workflow dependence, and inefficient context usage, which jointly limit adaptability in open-ended and non-stationary environments. To address these limitations, we present AutoAgent, a self-evolving multi-agent framework built on three tightly coupled components: evolving cognition, on-the-fly contextual decision-making, and elastic memory orchestration. At the core of AutoAgent, each agent maintains structured prompt-level cognition over tools, self-capabilities, peer expertise, and task knowledge. During execution, this cognition is combined with live task context to select actions from a unified space that includes tool calls, LLM-based generation, and inter-agent requests. To support efficient long-horizon reasoning, an Elastic Memory Orchestrator dynamically organizes interaction history by preserving raw records, compressing redundant trajectories, and constructing reusable episodic abstractions, thereby reducing token overhead while retaining decision-critical evidence. These components are integrated through a closed-loop cognitive evolution process that aligns intended actions with observed outcomes to continuously update cognition and expand reusable skills, without external retraining. Empirical results across retrieval-augmented reasoning, tool-augmented agent benchmarks, and embodied task environments show that AutoAgent consistently improves task success, tool-use efficiency, and collaborative robustness over static and memory-augmented baselines. Overall, AutoAgent provides a unified and practical foundation for adaptive autonomous agents that must learn from experience while making reliable context-aware decisions in dynamic environments.


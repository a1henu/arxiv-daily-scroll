---
layout: default
title: Optimistic Transfer under Task Shift via Bellman Alignment
---

# Optimistic Transfer under Task Shift via Bellman Alignment
**arXiv**：[2601.21924v1](https://arxiv.org/abs/2601.21924) · [PDF](https://arxiv.org/pdf/2601.21924.pdf)  
**作者**：Jinhang Chai, Enpei Zhang, Elynn Chen, Yujun Yan  

**一句话要点**：提出基于贝尔曼对齐的乐观转移强化学习框架，解决任务转移中的在线学习偏差问题。

**关键词**：在线强化学习, 任务转移, 贝尔曼对齐, 遗憾界分析, 函数逼近, 数据重用

## 3 点简述
- 核心问题：在线转移强化学习中，源任务与目标任务的贝尔曼回归目标不匹配导致系统偏差和遗憾保证失效。
- 方法要点：引入一步贝尔曼对齐作为抽象，提出重加权目标操作，通过测度变换校正转移不匹配，实现统计上可靠的源数据重用。
- 实验或效果：在表格和神经网络设置中，相比单任务学习和朴素池化，该框架展现出持续改进，验证了贝尔曼对齐作为模型无关转移原则的有效性。

## 摘要（原文）

> We study online transfer reinforcement learning (RL) in episodic Markov decision processes, where experience from related source tasks is available during learning on a target task. A fundamental difficulty is that task similarity is typically defined in terms of rewards or transitions, whereas online RL algorithms operate on Bellman regression targets. As a result, naively reusing source Bellman updates introduces systematic bias and invalidates regret guarantees.
>   We identify one-step Bellman alignment as the correct abstraction for transfer in online RL and propose re-weighted targeting (RWT), an operator-level correction that retargets continuation values and compensates for transition mismatch via a change of measure. RWT reduces task mismatch to a fixed one-step correction and enables statistically sound reuse of source data.
>   This alignment yields a two-stage RWT $Q$-learning framework that separates variance reduction from bias correction. Under RKHS function approximation, we establish regret bounds that scale with the complexity of the task shift rather than the target MDP. Empirical results in both tabular and neural network settings demonstrate consistent improvements over single-task learning and naïve pooling, highlighting Bellman alignment as a model-agnostic transfer principle for online RL.


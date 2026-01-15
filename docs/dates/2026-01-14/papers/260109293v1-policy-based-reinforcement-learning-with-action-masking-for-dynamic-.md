---
layout: default
title: Policy-Based Reinforcement Learning with Action Masking for Dynamic Job Shop Scheduling under Uncertainty: Handling Random Arrivals and Machine Failures
---

# Policy-Based Reinforcement Learning with Action Masking for Dynamic Job Shop Scheduling under Uncertainty: Handling Random Arrivals and Machine Failures
**arXiv**：[2601.09293v1](https://arxiv.org/abs/2601.09293) · [PDF](https://arxiv.org/pdf/2601.09293.pdf)  
**作者**：Sofiene Lassoued, Stefan Lier, Andreas Schwung  

**一句话要点**：提出基于策略强化学习与动作掩码的框架，以解决不确定动态作业车间调度问题。

**关键词**：动态作业车间调度, 强化学习, 动作掩码, Petri网建模, 不确定性处理

## 3 点简述
- 核心问题：处理随机作业到达和机器故障的动态作业车间调度不确定性。
- 方法要点：使用着色时间Petri网建模环境，结合Maskable PPO进行动态决策。
- 实验或效果：在动态JSSP基准上优于传统启发式方法，实现完工时间最小化。

## 摘要（原文）

> We present a novel framework for solving Dynamic Job Shop Scheduling Problems under uncertainty, addressing the challenges introduced by stochastic job arrivals and unexpected machine breakdowns. Our approach follows a model-based paradigm, using Coloured Timed Petri Nets to represent the scheduling environment, and Maskable Proximal Policy Optimization to enable dynamic decision-making while restricting the agent to feasible actions at each decision point. To simulate realistic industrial conditions, dynamic job arrivals are modeled using a Gamma distribution, which captures complex temporal patterns such as bursts, clustering, and fluctuating workloads. Machine failures are modeled using a Weibull distribution to represent age-dependent degradation and wear-out dynamics. These stochastic models enable the framework to reflect real-world manufacturing scenarios better. In addition, we study two action-masking strategies: a non-gradient approach that overrides the probabilities of invalid actions, and a gradient-based approach that assigns negative gradients to invalid actions within the policy network. We conduct extensive experiments on dynamic JSSP benchmarks, demonstrating that our method consistently outperforms traditional heuristic and rule-based approaches in terms of makespan minimization. The results highlight the strength of combining interpretable Petri-net-based models with adaptive reinforcement learning policies, yielding a resilient, scalable, and explainable framework for real-time scheduling in dynamic and uncertain manufacturing environments.


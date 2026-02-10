---
layout: default
title: Dialogue Model Optimization via Agent Game and Adaptive Tree-based GRPO
---

# Dialogue Model Optimization via Agent Game and Adaptive Tree-based GRPO
**arXiv**：[2602.08533v1](https://arxiv.org/abs/2602.08533) · [PDF](https://arxiv.org/pdf/2602.08533.pdf)  
**作者**：Kun Peng, Conghui Tan, Yu Liu, Guohua Tang, Zhongqian Sun, Wei Yang, Zining Zhu, Lei Jiang, Yanbing Liu, Hao Peng  

**一句话要点**：提出基于双智能体博弈与自适应树状GRPO的长时对话优化框架，以解决数据依赖与短视偏差问题。

**关键词**：对话智能体, 长时强化学习, 自适应树状优化, 双智能体博弈, 在线个性化

## 3 点简述
- 核心问题：现有方法依赖预收集用户数据，强化学习存在短视偏差，忽视长时对话价值。
- 方法要点：采用双智能体博弈，用户智能体通过风格模仿和主动终止构建动态环境；引入自适应树状GRPO，将对话轨迹视为树，自适应调整观察范围以平衡探索与维护。
- 实验或效果：实验显示框架在性能、样本效率和鲁棒性方面表现优越，将计算开销从指数级降至多项式级。

## 摘要（原文）

> Open-ended dialogue agents aim to deliver engaging, personalized interactions by adapting to users' traits, but existing methods face critical limitations: over-reliance on pre-collected user data, and short-horizon biases in reinforcement learning (RL) that neglect long-term dialogue value. To address these, we propose a novel long-horizon RL framework integrating online personalization with Adaptive Tree-based Group Relative Policy Optimization (AT-GRPO). Adopting a two-agent game paradigm, a user agent constructs dynamic environments via style mimicry (learning user-specific conversational traits) and active termination (predicting turn-level termination probabilities as immediate rewards), forming an iterative cycle that drives the dialogue agent to deepen interest exploration. AT-GRPO reinterprets dialogue trajectories as trees and introduces adaptive observation ranges. Unlike full tree expansion that incurs exponential overhead, it limits each node to aggregate rewards from a stage-aware range: larger ranges support early-stage topic exploration, while smaller ranges facilitate late-stage dialogue maintenance. This design reduces rollout budgets from exponential to polynomial in the dialogue length, while preserving long-term reward capture. Extensive experiments show our framework's superior performance, sample efficiency, and robustness.


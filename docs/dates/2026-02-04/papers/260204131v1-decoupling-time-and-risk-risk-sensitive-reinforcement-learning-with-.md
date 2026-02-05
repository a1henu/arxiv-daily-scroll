---
layout: default
title: Decoupling Time and Risk: Risk-Sensitive Reinforcement Learning with General Discounting
---

# Decoupling Time and Risk: Risk-Sensitive Reinforcement Learning with General Discounting
**arXiv**：[2602.04131v1](https://arxiv.org/abs/2602.04131) · [PDF](https://arxiv.org/pdf/2602.04131.pdf)  
**作者**：Mehrdad Moghimi, Anthony Coache, Hyejin Ku  

**一句话要点**：提出支持灵活折扣和风险度量的分布强化学习框架，以优化安全关键应用中的决策偏好。

**关键词**：分布强化学习, 风险敏感优化, 灵活折扣, 决策偏好, 安全关键应用

## 3 点简述
- 核心问题：传统强化学习中折扣因子固定，无法充分表达时间偏好和风险敏感目标。
- 方法要点：引入灵活折扣函数，结合分布强化学习优化风险度量，提供算法最优性分析。
- 实验或效果：通过多视野扩展解决现有方法问题，实验验证方法鲁棒性，适用于安全关键场景。

## 摘要（原文）

> Distributional reinforcement learning (RL) is a powerful framework increasingly adopted in safety-critical domains for its ability to optimize risk-sensitive objectives. However, the role of the discount factor is often overlooked, as it is typically treated as a fixed parameter of the Markov decision process or tunable hyperparameter, with little consideration of its effect on the learned policy. In the literature, it is well-known that the discounting function plays a major role in characterizing time preferences of an agent, which an exponential discount factor cannot fully capture. Building on this insight, we propose a novel framework that supports flexible discounting of future rewards and optimization of risk measures in distributional RL. We provide a technical analysis of the optimality of our algorithms, show that our multi-horizon extension fixes issues raised with existing methodologies, and validate the robustness of our methods through extensive experiments. Our results highlight that discounting is a cornerstone in decision-making problems for capturing more expressive temporal and risk preferences profiles, with potential implications for real-world safety-critical applications.


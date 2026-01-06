---
layout: default
title: Moments Matter:Stabilizing Policy Optimization using Return Distributions
---

# Moments Matter:Stabilizing Policy Optimization using Return Distributions
**arXiv**：[2601.01803v1](https://arxiv.org/abs/2601.01803) · [PDF](https://arxiv.org/pdf/2601.01803.pdf)  
**作者**：Dennis Jabs, Aditya Mohan, Marius Lindauer  

**一句话要点**：提出基于分布评论家高阶矩的PPO修正方法，以提升连续控制任务中策略优化的稳定性。

**关键词**：强化学习, 策略优化, 分布评论家, 高阶矩, 稳定性提升, 连续控制

## 3 点简述
- 核心问题：深度强化学习策略因环境和算法噪声导致不稳定，影响算法比较和实际应用。
- 方法要点：通过分布评论家建模状态-动作回报分布，利用偏度和峰度修正PPO的优势函数，惩罚极端尾部行为。
- 实验或效果：在Walker2D环境中，稳定性提升高达75%，同时保持可比的评估回报。

## 摘要（原文）

> Deep Reinforcement Learning (RL) agents often learn policies that achieve the same episodic return yet behave very differently, due to a combination of environmental (random transitions, initial conditions, reward noise) and algorithmic (minibatch selection, exploration noise) factors. In continuous control tasks, even small parameter shifts can produce unstable gaits, complicating both algorithm comparison and real-world transfer. Previous work has shown that such instability arises when policy updates traverse noisy neighborhoods and that the spread of post-update return distribution $R(θ)$, obtained by repeatedly sampling minibatches, updating $θ$, and measuring final returns, is a useful indicator of this noise. Although explicitly constraining the policy to maintain a narrow $R(θ)$ can improve stability, directly estimating $R(θ)$ is computationally expensive in high-dimensional settings. We propose an alternative that takes advantage of environmental stochasticity to mitigate update-induced variability. Specifically, we model state-action return distribution through a distributional critic and then bias the advantage function of PPO using higher-order moments (skewness and kurtosis) of this distribution. By penalizing extreme tail behaviors, our method discourages policies from entering parameter regimes prone to instability. We hypothesize that in environments where post-update critic values align poorly with post-update returns, standard PPO struggles to produce a narrow $R(θ)$. In such cases, our moment-based correction narrows $R(θ)$, improving stability by up to 75% in Walker2D, while preserving comparable evaluation returns.


---
layout: default
title: Almost Sure Convergence of Differential Temporal Difference Learning for Average Reward Markov Decision Processes
---

# Almost Sure Convergence of Differential Temporal Difference Learning for Average Reward Markov Decision Processes
**arXiv**：[2602.16629v1](https://arxiv.org/abs/2602.16629) · [PDF](https://arxiv.org/pdf/2602.16629.pdf)  
**作者**：Ethan Blaser, Jiuqi Wang, Shangtong Zhang  

**一句话要点**：证明无局部时钟的差分时序差分学习在平均奖励马尔可夫决策过程中的几乎必然收敛

**关键词**：平均奖励强化学习, 差分时序差分学习, 几乎必然收敛, 无局部时钟, 理论分析

## 3 点简述
- 核心问题：现有差分TD收敛保证依赖局部时钟学习率，不实用且限于表格设置。
- 方法要点：证明在标准递减学习率下，on-policy n步差分TD几乎必然收敛，无需局部时钟。
- 实验或效果：推导三个充分条件，确保off-policy n步差分TD也能无局部时钟收敛，强化理论基础。

## 摘要（原文）

> The average reward is a fundamental performance metric in reinforcement learning (RL) focusing on the long-run performance of an agent. Differential temporal difference (TD) learning algorithms are a major advance for average reward RL as they provide an efficient online method to learn the value functions associated with the average reward in both on-policy and off-policy settings. However, existing convergence guarantees require a local clock in learning rates tied to state visit counts, which practitioners do not use and does not extend beyond tabular settings. We address this limitation by proving the almost sure convergence of on-policy $n$-step differential TD for any $n$ using standard diminishing learning rates without a local clock. We then derive three sufficient conditions under which off-policy $n$-step differential TD also converges without a local clock. These results strengthen the theoretical foundations of differential TD and bring its convergence analysis closer to practical implementations.


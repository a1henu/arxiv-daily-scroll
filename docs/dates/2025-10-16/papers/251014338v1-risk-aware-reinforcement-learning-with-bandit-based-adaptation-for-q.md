---
layout: default
title: Risk-Aware Reinforcement Learning with Bandit-Based Adaptation for Quadrupedal Locomotion
---

# Risk-Aware Reinforcement Learning with Bandit-Based Adaptation for Quadrupedal Locomotion
**arXiv**：[2510.14338v1](https://arxiv.org/abs/2510.14338) · [PDF](https://arxiv.org/pdf/2510.14338.pdf)  
**作者**：Yuanhong Zeng, Anushri Dixit  

**一句话要点**：提出风险感知强化学习与多臂老虎机自适应方法，以提升四足机器人在未知环境中的运动性能。

**关键词**：风险感知强化学习, 四足机器人运动, CVaR约束优化, 多臂老虎机, 策略自适应, 未知环境适应

## 3 点简述
- 核心问题：四足机器人在未知环境中运动时，面临稳定性与性能下降的风险。
- 方法要点：使用CVaR约束策略优化训练风险条件策略族，并通过多臂老虎机在线自适应选择最优策略。
- 实验或效果：在仿真和真实机器人测试中，性能优于基线，自适应选择在未知地形中快速生效。

## 摘要（原文）

> In this work, we study risk-aware reinforcement learning for quadrupedal
> locomotion. Our approach trains a family of risk-conditioned policies using a
> Conditional Value-at-Risk (CVaR) constrained policy optimization technique that
> provides improved stability and sample efficiency. At deployment, we adaptively
> select the best performing policy from the family of policies using a
> multi-armed bandit framework that uses only observed episodic returns, without
> any privileged environment information, and adapts to unknown conditions on the
> fly. Hence, we train quadrupedal locomotion policies at various levels of
> robustness using CVaR and adaptively select the desired level of robustness
> online to ensure performance in unknown environments. We evaluate our method in
> simulation across eight unseen settings (by changing dynamics, contacts,
> sensing noise, and terrain) and on a Unitree Go2 robot in previously unseen
> terrains. Our risk-aware policy attains nearly twice the mean and tail
> performance in unseen environments compared to other baselines and our
> bandit-based adaptation selects the best-performing risk-aware policy in
> unknown terrain within two minutes of operation.


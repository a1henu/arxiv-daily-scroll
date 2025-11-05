---
layout: default
title: A Quantitative Comparison of Centralised and Distributed Reinforcement Learning-Based Control for Soft Robotic Arms
---

# A Quantitative Comparison of Centralised and Distributed Reinforcement Learning-Based Control for Soft Robotic Arms
**arXiv**：[2511.02192v1](https://arxiv.org/abs/2511.02192) · [PDF](https://arxiv.org/pdf/2511.02192.pdf)  
**作者**：Linxin Hou, Qirui Wu, Zhihang Qin, Neil Banerjee, Yongxin Guo, Cecilia Laschi  

**一句话要点**：比较集中与分布式强化学习在软体机械臂控制中的性能，基于Cosserat模型仿真。

**关键词**：软体机器人控制, 多智能体强化学习, Cosserat模型仿真, 策略优化比较, 样本效率分析

## 3 点简述
- 核心问题：集中与分布式MARL在软体机械臂控制中的性能差异，随控制段数变化。
- 方法要点：使用PPO和MAPPO，在PyElastica和OpenAI Gym中训练，评估多种场景。
- 实验效果：分布式策略在高控制段数时样本效率高，集中策略训练时间更短。

## 摘要（原文）

> This paper presents a quantitative comparison between centralised and
> distributed multi-agent reinforcement learning (MARL) architectures for
> controlling a soft robotic arm modelled as a Cosserat rod in simulation. Using
> PyElastica and the OpenAI Gym interface, we train both a global Proximal Policy
> Optimisation (PPO) controller and a Multi-Agent PPO (MAPPO) under identical
> budgets. Both approaches are based on the arm having $n$ number of controlled
> sections. The study systematically varies $n$ and evaluates the performance of
> the arm to reach a fixed target in three scenarios: default baseline condition,
> recovery from external disturbance, and adaptation to actuator failure.
> Quantitative metrics used for the evaluation are mean action magnitude, mean
> final distance, mean episode length, and success rate. The results show that
> there are no significant benefits of the distributed policy when the number of
> controlled sections $n\le4$. In very simple systems, when $n\le2$, the
> centralised policy outperforms the distributed one. When $n$ increases to $4<
> n\le 12$, the distributed policy shows a high sample efficiency. In these
> systems, distributed policy promotes a stronger success rate, resilience, and
> robustness under local observability and yields faster convergence given the
> same sample size. However, centralised policies achieve much higher time
> efficiency during training as it takes much less time to train the same size of
> samples. These findings highlight the trade-offs between centralised and
> distributed policy in reinforcement learning-based control for soft robotic
> systems and provide actionable design guidance for future sim-to-real transfer
> in soft rod-like manipulators.


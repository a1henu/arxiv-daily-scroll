---
layout: default
title: Safe Exploration via Policy Priors
---

# Safe Exploration via Policy Priors
**arXiv**：[2601.19612v1](https://arxiv.org/abs/2601.19612) · [PDF](https://arxiv.org/pdf/2601.19612.pdf)  
**作者**：Manuel Wendl, Yarden As, Manish Prajapat, Anton Pollak, Stelian Coros, Andreas Krause  

**一句话要点**：提出SOOPER方法，利用策略先验实现强化学习的安全探索

**关键词**：安全强化学习, 策略先验, 概率动力学模型, 安全探索, 离线数据, 收敛保证

## 3 点简述
- 核心问题：强化学习在真实环境中需安全探索，避免危险行为。
- 方法要点：使用次优保守策略作为先验，结合概率动力学模型进行乐观探索与悲观回退。
- 实验或效果：在安全RL基准和真实硬件上验证，优于现有方法，理论保证安全与收敛。

## 摘要（原文）

> Safe exploration is a key requirement for reinforcement learning (RL) agents to learn and adapt online, beyond controlled (e.g. simulated) environments. In this work, we tackle this challenge by utilizing suboptimal yet conservative policies (e.g., obtained from offline data or simulators) as priors. Our approach, SOOPER, uses probabilistic dynamics models to optimistically explore, yet pessimistically fall back to the conservative policy prior if needed. We prove that SOOPER guarantees safety throughout learning, and establish convergence to an optimal policy by bounding its cumulative regret. Extensive experiments on key safe RL benchmarks and real-world hardware demonstrate that SOOPER is scalable, outperforms the state-of-the-art and validate our theoretical guarantees in practice.


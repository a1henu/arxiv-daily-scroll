---
layout: default
title: Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings
---

# Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings
**arXiv**：[2602.12520v1](https://arxiv.org/abs/2602.12520) · [PDF](https://arxiv.org/pdf/2602.12520.pdf)  
**作者**：Zhizun Wang, David Meger  

**一句话要点**：提出基于模型的多智能体强化学习框架，结合联合状态-动作学习嵌入以提升部分可观测动态环境中的协调效率。

**关键词**：多智能体强化学习, 模型基强化学习, 状态-动作嵌入, 变分自编码器, 想象模块, 联合动作值估计

## 3 点简述
- 核心问题：在部分可观测、高度动态的多智能体环境中，如何高效学习协调策略并减少真实环境交互需求。
- 方法要点：设计世界模型，通过变分自编码器训练，并注入状态-动作学习嵌入（SALE）到想象模块和联合智能体网络中，以增强未来轨迹预测和联合动作值估计。
- 实验或效果：在StarCraft II微操、Multi-Agent MuJoCo和Level-Based Foraging基准测试中，方法优于基线算法，验证了联合状态-动作学习嵌入的有效性。

## 摘要（原文）

> Learning to coordinate many agents in partially observable and highly dynamic environments requires both informative representations and data-efficient training. To address this challenge, we present a novel model-based multi-agent reinforcement learning framework that unifies joint state-action representation learning with imaginative roll-outs. We design a world model trained with variational auto-encoders and augment the model using the state-action learned embedding (SALE). SALE is injected into both the imagination module that forecasts plausible future roll-outs and the joint agent network whose individual action values are combined through a mixing network to estimate the joint action-value function. By coupling imagined trajectories with SALE-based action values, the agents acquire a richer understanding of how their choices influence collective outcomes, leading to improved long-term planning and optimization under limited real-environment interactions. Empirical studies on well-established multi-agent benchmarks, including StarCraft II Micro-Management, Multi-Agent MuJoCo, and Level-Based Foraging challenges, demonstrate consistent gains of our method over baseline algorithms and highlight the effectiveness of joint state-action learned embeddings within a multi-agent model-based paradigm.


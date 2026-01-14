---
layout: default
title: Model-Agnostic Solutions for Deep Reinforcement Learning in Non-Ergodic Contexts
---

# Model-Agnostic Solutions for Deep Reinforcement Learning in Non-Ergodic Contexts
**arXiv**：[2601.08726v1](https://arxiv.org/abs/2601.08726) · [PDF](https://arxiv.org/pdf/2601.08726.pdf)  
**作者**：Bert Verbruggen, Arne Vanhoyweghen, Vincent Ginis  

**一句话要点**：提出模型无关的深度强化学习方法，通过引入时间依赖性解决非遍历环境中的策略次优问题。

**关键词**：非遍历环境, 深度强化学习, 时间依赖性, 贝尔曼方程, 策略优化, 模型无关方法

## 3 点简述
- 核心问题：非遍历环境中，传统强化学习基于期望值的贝尔曼方程导致策略次优，因长期结果依赖具体轨迹而非整体平均。
- 方法要点：在深度强化学习中引入显式时间依赖性，使网络函数近似能纳入时间信息，估计与过程内在增长率一致的价值函数。
- 实验或效果：扩展分析至深度强化学习实现，展示其在非遍历动态下同样产生次优策略，而时间依赖性改进无需改变环境反馈即可自然提升。

## 摘要（原文）

> Reinforcement Learning (RL) remains a central optimisation framework in machine learning. Although RL agents can converge to optimal solutions, the definition of ``optimality'' depends on the environment's statistical properties. The Bellman equation, central to most RL algorithms, is formulated in terms of expected values of future rewards. However, when ergodicity is broken, long-term outcomes depend on the specific trajectory rather than on the ensemble average. In such settings, the ensemble average diverges from the time-average growth experienced by individual agents, with expected-value formulations yielding systematically suboptimal policies. Prior studies demonstrated that traditional RL architectures fail to recover the true optimum in non-ergodic environments. We extend this analysis to deep RL implementations and show that these, too, produce suboptimal policies under non-ergodic dynamics. Introducing explicit time dependence into the learning process can correct this limitation. By allowing the network's function approximation to incorporate temporal information, the agent can estimate value functions consistent with the process's intrinsic growth rate. This improvement does not require altering the environmental feedback, such as reward transformations or modified objective functions, but arises naturally from the agent's exposure to temporal trajectories. Our results contribute to the growing body of research on reinforcement learning methods for non-ergodic systems.


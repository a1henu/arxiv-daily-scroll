---
layout: default
title: Mean-Field Reinforcement Learning without Synchrony
---

# Mean-Field Reinforcement Learning without Synchrony
**arXiv**：[2602.18026v1](https://arxiv.org/abs/2602.18026) · [PDF](https://arxiv.org/pdf/2602.18026.pdf)  
**作者**：Shan Yang  

**一句话要点**：提出基于种群分布的TMF框架，解决异步多智能体强化学习中的均值动作未定义问题。

**关键词**：均值场强化学习, 异步多智能体, 种群分布, TMF框架, 策略梯度算法, 有限种群近似

## 3 点简述
- 核心问题：传统均值场强化学习依赖同步动作，异步时均值动作未定义，限制应用。
- 方法要点：构建TMF框架，使用种群分布作为统计量，覆盖从同步到顺序决策的完整谱系。
- 实验或效果：在资源选择和动态排队游戏中，TMF-PG算法性能稳定，近似误差以O(1/√N)速率衰减。

## 摘要（原文）

> Mean-field reinforcement learning (MF-RL) scales multi-agent RL to large populations by reducing each agent's dependence on others to a single summary statistic -- the mean action. However, this reduction requires every agent to act at every time step; when some agents are idle, the mean action is simply undefined. Addressing asynchrony therefore requires a different summary statistic -- one that remains defined regardless of which agents act. The population distribution $μ\in Δ(\mathcal{O})$ -- the fraction of agents at each observation -- satisfies this requirement: its dimension is independent of $N$, and under exchangeability it fully determines each agent's reward and transition. Existing MF-RL theory, however, is built on the mean action and does not extend to $μ$. We therefore construct the Temporal Mean Field (TMF) framework around the population distribution $μ$ from scratch, covering the full spectrum from fully synchronous to purely sequential decision-making within a single theory. We prove existence and uniqueness of TMF equilibria, establish an $O(1/\sqrt{N})$ finite-population approximation bound that holds regardless of how many agents act per step, and prove convergence of a policy gradient algorithm (TMF-PG) to the unique equilibrium. Experiments on a resource selection game and a dynamic queueing game confirm that TMF-PG achieves near-identical performance whether one agent or all $N$ act per step, with approximation error decaying at the predicted $O(1/\sqrt{N})$ rate.


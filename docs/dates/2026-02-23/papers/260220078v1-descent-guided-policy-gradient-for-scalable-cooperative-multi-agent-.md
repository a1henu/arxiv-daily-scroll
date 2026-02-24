---
layout: default
title: Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning
---

# Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning
**arXiv**：[2602.20078v1](https://arxiv.org/abs/2602.20078) · [PDF](https://arxiv.org/pdf/2602.20078.pdf)  
**作者**：Shan Yang, Yang Liu  

**一句话要点**：提出基于下降引导的策略梯度框架，以解决多智能体强化学习中的跨智能体噪声扩展问题。

**关键词**：多智能体强化学习, 策略梯度, 梯度方差, 可微模型, 云调度, 样本复杂度

## 3 点简述
- 核心问题：多智能体强化学习中，跨智能体噪声随智能体数量线性增长，导致梯度估计方差高和样本复杂度高。
- 方法要点：利用可微分析模型构建无噪声的个体引导梯度，解耦智能体间的梯度依赖，降低方差至常数级。
- 实验或效果：在异构云调度任务中，DG-PG在5至200智能体规模下快速收敛，验证了规模不变的样本复杂度。

## 摘要（原文）

> Scaling cooperative multi-agent reinforcement learning (MARL) is fundamentally limited by cross-agent noise: when agents share a common reward, the actions of all $N$ agents jointly determine each agent's learning signal, so cross-agent noise grows with $N$. In the policy gradient setting, per-agent gradient estimate variance scales as $Θ(N)$, yielding sample complexity $\mathcal{O}(N/ε)$. We observe that many domains -- cloud computing, transportation, power systems -- have differentiable analytical models that prescribe efficient system states. In this work, we propose Descent-Guided Policy Gradient (DG-PG), a framework that constructs noise-free per-agent guidance gradients from these analytical models, decoupling each agent's gradient from the actions of all others. We prove that DG-PG reduces gradient variance from $Θ(N)$ to $\mathcal{O}(1)$, preserves the equilibria of the cooperative game, and achieves agent-independent sample complexity $\mathcal{O}(1/ε)$. On a heterogeneous cloud scheduling task with up to 200 agents, DG-PG converges within 10 episodes at every tested scale -- from $N=5$ to $N=200$ -- directly confirming the predicted scale-invariant complexity, while MAPPO and IPPO fail to converge under identical architectures.


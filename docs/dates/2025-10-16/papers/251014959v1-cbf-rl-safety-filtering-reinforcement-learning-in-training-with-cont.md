---
layout: default
title: CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions
---

# CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions
**arXiv**：[2510.14959v1](https://arxiv.org/abs/2510.14959) · [PDF](https://arxiv.org/pdf/2510.14959.pdf)  
**作者**：Lizhi Yang, Blake Werner, Massimiliano de Sa Aaron D. Ames  

**一句话要点**：提出CBF-RL框架，在强化学习训练中集成控制屏障函数以提升安全性

**关键词**：强化学习, 控制屏障函数, 安全过滤, 机器人控制, 训练安全, 实时部署

## 3 点简述
- 强化学习常牺牲安全性追求性能，导致实际部署风险
- CBF-RL在训练中编码安全约束，无需在线安全过滤器
- 实验验证在导航和人形机器人任务中实现安全探索和鲁棒性能

## 摘要（原文）

> Reinforcement learning (RL), while powerful and expressive, can often
> prioritize performance at the expense of safety. Yet safety violations can lead
> to catastrophic outcomes in real-world deployments. Control Barrier Functions
> (CBFs) offer a principled method to enforce dynamic safety -- traditionally
> deployed \emph{online} via safety filters. While the result is safe behavior,
> the fact that the RL policy does not have knowledge of the CBF can lead to
> conservative behaviors. This paper proposes CBF-RL, a framework for generating
> safe behaviors with RL by enforcing CBFs \emph{in training}. CBF-RL has two key
> attributes: (1) minimally modifying a nominal RL policy to encode safety
> constraints via a CBF term, (2) and safety filtering of the policy rollouts in
> training. Theoretically, we prove that continuous-time safety filters can be
> deployed via closed-form expressions on discrete-time roll-outs. Practically,
> we demonstrate that CBF-RL internalizes the safety constraints in the learned
> policy -- both enforcing safer actions and biasing towards safer rewards --
> enabling safe deployment without the need for an online safety filter. We
> validate our framework through ablation studies on navigation tasks and on the
> Unitree G1 humanoid robot, where CBF-RL enables safer exploration, faster
> convergence, and robust performance under uncertainty, enabling the humanoid
> robot to avoid obstacles and climb stairs safely in real-world settings without
> a runtime safety filter.


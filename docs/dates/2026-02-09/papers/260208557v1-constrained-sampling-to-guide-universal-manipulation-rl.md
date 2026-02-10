---
layout: default
title: Constrained Sampling to Guide Universal Manipulation RL
---

# Constrained Sampling to Guide Universal Manipulation RL
**arXiv**：[2602.08557v1](https://arxiv.org/abs/2602.08557) · [PDF](https://arxiv.org/pdf/2602.08557.pdf)  
**作者**：Marc Toussaint, Cornelius V. Braun, Eckart Cobo-Briesewitz, Sayantan Auddy, Armand Jordana, Justin Carpentier  

**一句话要点**：提出Sample-Guided RL，利用模型求解器采样可行状态以引导通用操作强化学习

**关键词**：强化学习, 接触操作, 状态采样, 模型引导, 通用策略

## 3 点简述
- 核心问题：稀疏奖励下RL难以探索复杂接触操作策略
- 方法要点：基于可行状态流形采样，结合约束求解器引导策略训练
- 实验或效果：在双球和panda臂场景中实现高成功率，发现复杂全身接触策略

## 摘要（原文）

> We consider how model-based solvers can be leveraged to guide training of a universal policy to control from any feasible start state to any feasible goal in a contact-rich manipulation setting. While Reinforcement Learning (RL) has demonstrated its strength in such settings, it may struggle to sufficiently explore and discover complex manipulation strategies, especially in sparse-reward settings. Our approach is based on the idea of a lower-dimensional manifold of feasible, likely-visited states during such manipulation and to guide RL with a sampler from this manifold. We propose Sample-Guided RL, which uses model-based constraint solvers to efficiently sample feasible configurations (satisfying differentiable collision, contact, and force constraints) and leverage them to guide RL for universal (goal-conditioned) manipulation policies. We study using this data directly to bias state visitation, as well as using black-box optimization of open-loop trajectories between random configurations to impose a state bias and optionally add a behavior cloning loss. In a minimalistic double sphere manipulation setting, Sample-Guided RL discovers complex manipulation strategies and achieves high success rates in reaching any statically stable state. In a more challenging panda arm setting, our approach achieves a significant success rate over a near-zero baseline, and demonstrates a breadth of complex whole-body-contact manipulation strategies.


---
layout: default
title: Stochastic Decision Horizons for Constrained Reinforcement Learning
---

# Stochastic Decision Horizons for Constrained Reinforcement Learning
**arXiv**：[2602.04599v1](https://arxiv.org/abs/2602.04599) · [PDF](https://arxiv.org/pdf/2602.04599.pdf)  
**作者**：Nikola Milosevic, Leonard Franz, Daniel Haeufle, Georg Martius, Nico Scherf, Pavel Kolev  

**一句话要点**：提出基于随机决策视野的控制即推理方法，以提升约束强化学习的离策略可扩展性。

**关键词**：约束强化学习, 随机决策视野, 控制即推理, 离策略学习, 生存加权目标, 虚拟终止

## 3 点简述
- 核心问题：约束马尔可夫决策过程（CMDPs）中，传统加性成本约束和双变量方法常阻碍离策略学习的可扩展性。
- 方法要点：引入随机决策视野，通过状态-动作依赖的延续机制，使约束违规衰减奖励贡献并缩短规划视野，形成生存加权目标。
- 实验或效果：在标准基准测试中展示改进的样本效率和有利的回报-违规权衡，虚拟终止MPO（VT-MPO）能扩展到高维肌肉骨骼设置。

## 摘要（原文）

> Constrained Markov decision processes (CMDPs) provide a principled model for handling constraints, such as safety and other auxiliary objectives, in reinforcement learning. The common approach of using additive-cost constraints and dual variables often hinders off-policy scalability. We propose a Control as Inference formulation based on stochastic decision horizons, where constraint violations attenuate reward contributions and shorten the effective planning horizon via state-action-dependent continuation. This yields survival-weighted objectives that remain replay-compatible for off-policy actor-critic learning. We propose two violation semantics, absorbing and virtual termination, that share the same survival-weighted return but result in distinct optimization structures that lead to SAC/MPO-style policy improvement. Experiments demonstrate improved sample efficiency and favorable return-violation trade-offs on standard benchmarks. Moreover, MPO with virtual termination (VT-MPO) scales effectively to our high-dimensional musculoskeletal Hyfydy setup.


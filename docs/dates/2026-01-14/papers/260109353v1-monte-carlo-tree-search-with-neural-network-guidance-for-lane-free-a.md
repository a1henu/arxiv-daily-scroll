---
layout: default
title: Monte-Carlo Tree Search with Neural Network Guidance for Lane-Free Autonomous Driving
---

# Monte-Carlo Tree Search with Neural Network Guidance for Lane-Free Autonomous Driving
**arXiv**：[2601.09353v1](https://arxiv.org/abs/2601.09353) · [PDF](https://arxiv.org/pdf/2601.09353.pdf)  
**作者**：Ioannis Peridis, Dimitrios Troullinos, Georgios Chalkiadakis, Pantelis Giankoulidis, Ioannis Papamichail, Markos Papageorgiou  

**一句话要点**：提出神经网络引导的蒙特卡洛树搜索方法，用于无车道自动驾驶规划。

**关键词**：自动驾驶规划, 蒙特卡洛树搜索, 神经网络引导, 无车道交通, 强化学习框架, 计算效率

## 3 点简述
- 核心问题：无车道交通环境增加自动驾驶规划复杂度，需平衡安全与效率。
- 方法要点：结合预训练神经网络指导蒙特卡洛树搜索，提升决策效率。
- 实验效果：评估碰撞率和速度，分析各向同性状态信息、性能加速及计算资源权衡。

## 摘要（原文）

> Lane-free traffic environments allow vehicles to better harness the lateral capacity of the road without being restricted to lane-keeping, thereby increasing the traffic flow rates. As such, we have a distinct and more challenging setting for autonomous driving. In this work, we consider a Monte-Carlo Tree Search (MCTS) planning approach for single-agent autonomous driving in lane-free traffic, where the associated Markov Decision Process we formulate is influenced from existing approaches tied to reinforcement learning frameworks. In addition, MCTS is equipped with a pre-trained neural network (NN) that guides the selection phase. This procedure incorporates the predictive capabilities of NNs for a more informed tree search process under computational constraints. In our experimental evaluation, we consider metrics that address both safety (through collision rates) and efficacy (through measured speed). Then, we examine: (a) the influence of isotropic state information for vehicles in a lane-free environment, resulting in nudging behaviour--vehicles' policy reacts due to the presence of faster tailing ones, (b) the acceleration of performance for the NN-guided variant of MCTS, and (c) the trade-off between computational resources and solution quality.


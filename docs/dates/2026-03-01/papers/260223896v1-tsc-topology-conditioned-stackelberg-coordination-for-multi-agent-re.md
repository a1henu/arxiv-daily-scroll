---
layout: default
title: TSC: Topology-Conditioned Stackelberg Coordination for Multi-Agent Reinforcement Learning in Interactive Driving
---

# TSC: Topology-Conditioned Stackelberg Coordination for Multi-Agent Reinforcement Learning in Interactive Driving
**arXiv**：[2602.23896v1](https://arxiv.org/abs/2602.23896) · [PDF](https://arxiv.org/pdf/2602.23896.pdf)  
**作者**：Xiaotong Zhang, Gang Xiong, Yuanjing Wang, Siyu Teng, Alois Knoll, Long Chen  

**一句话要点**：提出拓扑条件Stackelberg协调框架，以解决密集交通中多智能体强化学习的交互驾驶问题

**关键词**：多智能体强化学习, 交互驾驶, Stackelberg博弈, 拓扑条件协调, 密集交通, 分散执行

## 3 点简述
- 核心问题：密集交通中多智能体交互驾驶存在部分可观测性下的不稳定行为，如振荡让行或不安全承诺，现有方法同步决策加剧非平稳性或集中排序扩展性差
- 方法要点：从轨迹编织关系中提取时变有向优先级图，定义局部领导者-跟随者依赖，通过图局部Stackelberg子游戏分解密集交互，在集中训练分散执行下学习顺序协调策略
- 实验或效果：在四个密集交通场景中，相比代表性多智能体强化学习基线，TSC在关键指标上表现更优，显著减少碰撞，同时保持竞争性交通效率和控制平滑度

## 摘要（原文）

> Safe and efficient autonomous driving in dense traffic is fundamentally a decentralized multi-agent coordination problem, where interactions at conflict points such as merging and weaving must be resolved reliably under partial observability. With only local and incomplete cues, interaction patterns can change rapidly, often causing unstable behaviors such as oscillatory yielding or unsafe commitments. Existing multi-agent reinforcement learning (MARL) approaches either adopt synchronous decision-making, which exacerbate non-stationarity, or depend on centralized sequencing mechanisms that scale poorly as traffic density increases. To address these limitations, we propose Topology-conditioned Stackelberg Coordination (TSC), a learning framework for decentralized interactive driving under communication-free execution, which extracts a time-varying directed priority graph from braid-inspired weaving relations between trajectories, thereby defining local leader-follower dependencies without constructing a global order of play. Conditioned on this graph, TSC endogenously factorizes dense interactions into graph-local Stackelberg subgames and, under centralized training and decentralized execution (CTDE), learns a sequential coordination policy that anticipates leaders via action prediction and trains followers through action-conditioned value learning to approximate local best responses, improving training stability and safety in dense traffic. Experiments across four dense traffic scenarios show that TSC achieves superior performance over representative MARL baselines across key metrics, most notably reducing collisions while maintaining competitive traffic efficiency and control smoothness.


---
layout: default
title: A Curriculum-Based Deep Reinforcement Learning Framework for the Electric Vehicle Routing Problem
---

# A Curriculum-Based Deep Reinforcement Learning Framework for the Electric Vehicle Routing Problem
**arXiv**：[2601.15038v1](https://arxiv.org/abs/2601.15038) · [PDF](https://arxiv.org/pdf/2601.15038.pdf)  
**作者**：Mertcan Daysalilar, Fuat Uyguroglu, Gabriel Nicolosi, Adam Meyers  

**一句话要点**：提出基于课程学习的深度强化学习框架，以解决电动汽车路径规划中的训练不稳定问题。

**关键词**：电动汽车路径规划, 深度强化学习, 课程学习, 异构图注意力, 训练稳定性, 泛化能力

## 3 点简述
- 核心问题：深度强化学习在电动汽车带时间窗路径规划中面临训练不稳定，难以收敛或泛化。
- 方法要点：采用三阶段课程学习，逐步增加问题复杂度，结合改进的近端策略优化和异构图注意力编码器。
- 实验或效果：在小规模实例上训练，能泛化到未见的中大规模实例，在可行性率和解质量上优于基线方法。

## 摘要（原文）

> The electric vehicle routing problem with time windows (EVRPTW) is a complex optimization problem in sustainable logistics, where routing decisions must minimize total travel distance, fleet size, and battery usage while satisfying strict customer time constraints. Although deep reinforcement learning (DRL) has shown great potential as an alternative to classical heuristics and exact solvers, existing DRL models often struggle to maintain training stability-failing to converge or generalize when constraints are dense. In this study, we propose a curriculum-based deep reinforcement learning (CB-DRL) framework designed to resolve this instability. The framework utilizes a structured three-phase curriculum that gradually increases problem complexity: the agent first learns distance and fleet optimization (Phase A), then battery management (Phase B), and finally the full EVRPTW (Phase C). To ensure stable learning across phases, the framework employs a modified proximal policy optimization algorithm with phase-specific hyperparameters, value and advantage clipping, and adaptive learning-rate scheduling. The policy network is built upon a heterogeneous graph attention encoder enhanced by global-local attention and feature-wise linear modulation. This specialized architecture explicitly captures the distinct properties of depots, customers, and charging stations. Trained exclusively on small instances with N=10 customers, the model demonstrates robust generalization to unseen instances ranging from N=5 to N=100, significantly outperforming standard baselines on medium-scale problems. Experimental results confirm that this curriculum-guided approach achieves high feasibility rates and competitive solution quality on out-of-distribution instances where standard DRL baselines fail, effectively bridging the gap between neural speed and operational reliability.


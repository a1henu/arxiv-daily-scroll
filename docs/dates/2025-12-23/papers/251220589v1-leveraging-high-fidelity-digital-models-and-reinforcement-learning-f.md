---
layout: default
title: Leveraging High-Fidelity Digital Models and Reinforcement Learning for Mission Engineering: A Case Study of Aerial Firefighting Under Perfect Information
---

# Leveraging High-Fidelity Digital Models and Reinforcement Learning for Mission Engineering: A Case Study of Aerial Firefighting Under Perfect Information
**arXiv**：[2512.20589v1](https://arxiv.org/abs/2512.20589) · [PDF](https://arxiv.org/pdf/2512.20589.pdf)  
**作者**：İbrahim Oğuz Çetinkaya, Sajad Khodadadian, Taylan G. Topçu  

**一句话要点**：提出基于高保真数字模型与强化学习的智能任务协调方法，以空中灭火为例提升任务工程性能

**关键词**：任务工程, 强化学习, 数字模型, 马尔可夫决策过程, 自适应协调, 空中灭火

## 3 点简述
- 核心问题：任务环境不确定动态，静态架构脆弱，需自适应任务分配与重构
- 方法要点：结合数字工程基础设施，将任务战术管理建模为MDP，使用PPO训练强化学习代理
- 实验或效果：空中灭火案例中，智能协调器超越基线，显著降低任务性能变异性

## 摘要（原文）

> As systems engineering (SE) objectives evolve from design and operation of monolithic systems to complex System of Systems (SoS), the discipline of Mission Engineering (ME) has emerged which is increasingly being accepted as a new line of thinking for the SE community. Moreover, mission environments are uncertain, dynamic, and mission outcomes are a direct function of how the mission assets will interact with this environment. This proves static architectures brittle and calls for analytically rigorous approaches for ME. To that end, this paper proposes an intelligent mission coordination methodology that integrates digital mission models with Reinforcement Learning (RL), that specifically addresses the need for adaptive task allocation and reconfiguration. More specifically, we are leveraging a Digital Engineering (DE) based infrastructure that is composed of a high-fidelity digital mission model and agent-based simulation; and then we formulate the mission tactics management problem as a Markov Decision Process (MDP), and employ an RL agent trained via Proximal Policy Optimization. By leveraging the simulation as a sandbox, we map the system states to actions, refining the policy based on realized mission outcomes. The utility of the RL-based intelligent mission coordinator is demonstrated through an aerial firefighting case study. Our findings indicate that the RL-based intelligent mission coordinator not only surpasses baseline performance but also significantly reduces the variability in mission performance. Thus, this study serves as a proof of concept demonstrating that DE-enabled mission simulations combined with advanced analytical tools offer a mission-agnostic framework for improving ME practice; which can be extended to more complicated fleet design and selection problems in the future from a mission-first perspective.


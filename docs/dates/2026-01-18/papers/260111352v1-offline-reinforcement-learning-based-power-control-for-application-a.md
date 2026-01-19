---
layout: default
title: Offline Reinforcement-Learning-Based Power Control for Application-Agnostic Energy Efficiency
---

# Offline Reinforcement-Learning-Based Power Control for Application-Agnostic Energy Efficiency
**arXiv**：[2601.11352v1](https://arxiv.org/abs/2601.11352) · [PDF](https://arxiv.org/pdf/2601.11352.pdf)  
**作者**：Akhilesh Raj, Swann Perarnau, Aniruddha Gokhale, Solomon Bekele Abera  

**一句话要点**：提出基于离线强化学习的CPU功率控制方法，以提升并行应用的运行时能效

**关键词**：离线强化学习, CPU功率控制, 能效优化, 并行应用, 灰盒方法, 硬件性能计数器

## 3 点简述
- 核心问题：在线强化学习训练在能效控制中面临模型缺失、噪声和可靠性挑战
- 方法要点：利用离线强化学习，结合灰盒方法整合应用无关性能数据和硬件计数器
- 实验或效果：在多种基准测试中，通过Intel RAPL控制功率，显著降低能耗且性能损失可接受

## 摘要（原文）

> Energy efficiency has become an integral aspect of modern computing infrastructure design, impacting the performance, cost, scalability, and durability of production systems. The incorporation of power actuation and sensing capabilities in CPU designs is indicative of this, enabling the deployment of system software that can actively monitor and adjust energy consumption and performance at runtime. While reinforcement learning (RL) would seem ideal for the design of such energy efficiency control systems, online training presents challenges ranging from the lack of proper models for setting up an adequate simulated environment, to perturbation (noise) and reliability issues, if training is deployed on a live system.
>   In this paper we discuss the use of offline reinforcement learning as an alternative approach for the design of an autonomous CPU power controller, with the goal of improving the energy efficiency of parallel applications at runtime without unduly impacting their performance. Offline RL sidesteps the issues incurred by online RL training by leveraging a dataset of state transitions collected from arbitrary policies prior to training.
>   Our methodology applies offline RL to a gray-box approach to energy efficiency, combining online application-agnostic performance data (e.g., heartbeats) and hardware performance counters to ensure that the scientific objectives are met with limited performance degradation. Evaluating our method on a variety of compute-bound and memory-bound benchmarks and controlling power on a live system through Intel's Running Average Power Limit, we demonstrate that such an offline-trained agent can substantially reduce energy consumption at a tolerable performance degradation cost.


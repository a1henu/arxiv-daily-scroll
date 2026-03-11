---
layout: default
title: On the Cost of Evolving Task Specialization in Multi-Robot Systems
---

# On the Cost of Evolving Task Specialization in Multi-Robot Systems
**arXiv**：[2603.09552v1](https://arxiv.org/abs/2603.09552) · [PDF](https://arxiv.org/pdf/2603.09552.pdf)  
**作者**：Paolo Leopardi, Heiko Hamann, Jonas Kuckling, Tanja Katharina Kaiser  

**一句话要点**：分析多机器人系统中任务专业化的成本效益，揭示有限优化预算下通用行为优于专业化

**关键词**：多机器人系统, 任务专业化, 进化优化, 人工神经网络, 成本效益分析, 觅食场景

## 3 点简述
- 核心问题：任务专业化在多机器人系统中是否总能提高效率，尤其在有限优化预算下
- 方法要点：在觅食场景中，进化人工神经网络作为通用行为和任务专业化行为
- 实验或效果：通用行为优化成功，而专业化控制器合作效率低，性能更差

## 摘要（原文）

> Task specialization can lead to simpler robot behaviors and higher efficiency in multi-robot systems. Previous works have shown the emergence of task specialization during evolutionary optimization, focusing on feasibility rather than costs. In this study, we take first steps toward a cost-benefit analysis of task specialization in robot swarms using a foraging scenario. We evolve artificial neural networks as generalist behaviors for the entire task and as task-specialist behaviors for subtasks within a limited evaluation budget. We show that generalist behaviors can be successfully optimized while the evolved task-specialist controllers fail to cooperate efficiently, resulting in worse performance than the generalists. Consequently, task specialization does not necessarily improve efficiency when optimization budget is limited.


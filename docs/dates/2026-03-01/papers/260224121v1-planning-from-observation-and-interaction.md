---
layout: default
title: Planning from Observation and Interaction
---

# Planning from Observation and Interaction
**arXiv**：[2602.24121v1](https://arxiv.org/abs/2602.24121) · [PDF](https://arxiv.org/pdf/2602.24121.pdf)  
**作者**：Tyler Han, Siyang Shen, Rohan Baijal, Harine Ravichandiran, Bat Nemekhbold, Kevin Huang, Sanghun Jung, Byron Boots  

**一句话要点**：提出基于规划的逆强化学习算法，仅通过观察与交互实现机器人世界建模与任务学习。

**关键词**：逆强化学习, 机器人学习, 世界建模, 观察学习, 规划算法, 样本效率

## 3 点简述
- 核心问题：在无奖励函数和演示者动作的约束下，仅通过任务观察学习机器人操作任务。
- 方法要点：采用规划式逆强化学习，从观察和交互中构建世界模型，无需先验知识或预训练。
- 实验或效果：真实世界实验显示，算法能在1小时内从零学习图像操作任务，样本效率和成功率优于现有方法。

## 摘要（原文）

> Observational learning requires an agent to learn to perform a task by referencing only observations of the performed task. This work investigates the equivalent setting in real-world robot learning where access to hand-designed rewards and demonstrator actions are not assumed. To address this data-constrained setting, this work presents a planning-based Inverse Reinforcement Learning (IRL) algorithm for world modeling from observation and interaction alone. Experiments conducted entirely in the real-world demonstrate that this paradigm is effective for learning image-based manipulation tasks from scratch in under an hour, without assuming prior knowledge, pre-training, or data of any kind beyond task observations. Moreover, this work demonstrates that the learned world model representation is capable of online transfer learning in the real-world from scratch. In comparison to existing approaches, including IRL, RL, and Behavior Cloning (BC), which have more restrictive assumptions, the proposed approach demonstrates significantly greater sample efficiency and success rates, enabling a practical path forward for online world modeling and planning from observation and interaction. Videos and more at: https://uwrobotlearning.github.io/mpail2/.


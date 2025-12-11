---
layout: default
title: Dynamic one-time delivery of critical data by small and sparse UAV swarms: a model problem for MARL scaling studies
---

# Dynamic one-time delivery of critical data by small and sparse UAV swarms: a model problem for MARL scaling studies
**arXiv**：[2512.09682v1](https://arxiv.org/abs/2512.09682) · [PDF](https://arxiv.org/pdf/2512.09682.pdf)  
**作者**：Mika Persson, Jonas Lidman, Jacob Ljungberg, Samuel Sandelius, Adam Andersson  

**一句话要点**：提出基于多智能体强化学习的无人机群分散控制模型，用于关键数据一次性传递

**关键词**：多智能体强化学习, 无人机群控制, 分散控制, 扩展性研究, 确定性游戏

## 3 点简述
- 研究多智能体强化学习在无人机群分散控制中的应用，以传递关键数据包至已知位置
- 引入确定性游戏家族，设计用于多智能体强化学习的扩展性研究
- 实验显示，现有多智能体强化学习算法在小规模智能体下表现良好，但扩展性随智能体数量增加而受限

## 摘要（原文）

> This work presents a conceptual study on the application of Multi-Agent Reinforcement Learning (MARL) for decentralized control of unmanned aerial vehicles to relay a critical data package to a known position. For this purpose, a family of deterministic games is introduced, designed for scaling studies for MARL. A robust baseline policy is proposed, which is based on restricting agent motion envelopes and applying Dijkstra's algorithm. Experimental results show that two off-the-shelf MARL algorithms perform competitively with the baseline for a small number of agents, but scalability issues arise as the number of agents increase.


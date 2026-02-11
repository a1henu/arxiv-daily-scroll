---
layout: default
title: A Collaborative Safety Shield for Safe and Efficient CAV Lane Changes in Congested On-Ramp Merging
---

# A Collaborative Safety Shield for Safe and Efficient CAV Lane Changes in Congested On-Ramp Merging
**arXiv**：[2602.10007v1](https://arxiv.org/abs/2602.10007) · [PDF](https://arxiv.org/pdf/2602.10007.pdf)  
**作者**：Bharathkumar Hegde, Melanie Bouroche  

**一句话要点**：提出MARL-MASS控制器，以安全高效地解决拥堵匝道汇入中的CAV换道问题

**关键词**：自动驾驶换道, 多智能体强化学习, 控制屏障函数, 匝道汇入, 交通效率优化, 安全约束

## 3 点简述
- 核心问题：现有换道控制器难以同时保证安全与提升交通效率，尤其在拥堵匝道汇入场景中
- 方法要点：设计多智能体安全护盾MASS，基于控制屏障函数确保安全，并集成MARL与定制奖励函数优化效率
- 实验或效果：在仿真中验证MARL-MASS能平衡安全与效率，实现协作换道并提升策略稳定性

## 摘要（原文）

> Lane changing in dense traffic is a significant challenge for Connected and Autonomous Vehicles (CAVs). Existing lane change controllers primarily either ensure safety or collaboratively improve traffic efficiency, but do not consider these conflicting objectives together. To address this, we propose the Multi-Agent Safety Shield (MASS), designed using Control Barrier Functions (CBFs) to enable safe and collaborative lane changes. The MASS enables collaboration by capturing multi-agent interactions among CAVs through interaction topologies constructed as a graph using a simple algorithm. Further, a state-of-the-art Multi-Agent Reinforcement Learning (MARL) lane change controller is extended by integrating MASS to ensure safety and defining a customised reward function to prioritise efficiency improvements. As a result, we propose a lane change controller, known as MARL-MASS, and evaluate it in a congested on-ramp merging simulation. The results demonstrate that MASS enables collaborative lane changes with safety guarantees by strictly respecting the safety constraints. Moreover, the proposed custom reward function improves the stability of MARL policies trained with a safety shield. Overall, by encouraging the exploration of a collaborative lane change policy while respecting safety constraints, MARL-MASS effectively balances the trade-off between ensuring safety and improving traffic efficiency in congested traffic. The code for MARL-MASS is available with an open-source licence at https://github.com/hkbharath/MARL-MASS


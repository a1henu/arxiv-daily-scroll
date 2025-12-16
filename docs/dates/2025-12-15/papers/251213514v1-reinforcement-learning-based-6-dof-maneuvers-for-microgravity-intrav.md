---
layout: default
title: Reinforcement Learning based 6-DoF Maneuvers for Microgravity Intravehicular Docking: A Simulation Study with Int-Ball2 in ISS-JEM
---

# Reinforcement Learning based 6-DoF Maneuvers for Microgravity Intravehicular Docking: A Simulation Study with Int-Ball2 in ISS-JEM
**arXiv**：[2512.13514v1](https://arxiv.org/abs/2512.13514) · [PDF](https://arxiv.org/pdf/2512.13514.pdf)  
**作者**：Aman Arora, Matteo El-Hariry, Miguel Olivares-Mendez  

**一句话要点**：提出基于强化学习的6自由度对接框架，用于国际空间站内微重力环境下Int-Ball2机器人的精确对接。

**关键词**：强化学习, 6自由度对接, 微重力环境, 国际空间站, 近端策略优化, 仿真研究

## 3 点简述
- 核心问题：国际空间站内自主飞行器在传感噪声、执行器失配和环境变化下的精确对接挑战。
- 方法要点：使用近端策略优化在Isaac Sim高保真模型中训练控制器，建模推进器拖曳扭矩和极性结构。
- 实验或效果：在域随机化和有界观测噪声下实现稳定可靠对接，为未来扩展奠定基础。

## 摘要（原文）

> Autonomous free-flyers play a critical role in intravehicular tasks aboard the International Space Station (ISS), where their precise docking under sensing noise, small actuation mismatches, and environmental variability remains a nontrivial challenge. This work presents a reinforcement learning (RL) framework for six-degree-of-freedom (6-DoF) docking of JAXA's Int-Ball2 robot inside a high-fidelity Isaac Sim model of the Japanese Experiment Module (JEM). Using Proximal Policy Optimization (PPO), we train and evaluate controllers under domain-randomized dynamics and bounded observation noise, while explicitly modeling propeller drag-torque effects and polarity structure. This enables a controlled study of how Int-Ball2's propulsion physics influence RL-based docking performance in constrained microgravity interiors. The learned policy achieves stable and reliable docking across varied conditions and lays the groundwork for future extensions pertaining to Int-Ball2 in collision-aware navigation, safe RL, propulsion-accurate sim-to-real transfer, and vision-based end-to-end docking.


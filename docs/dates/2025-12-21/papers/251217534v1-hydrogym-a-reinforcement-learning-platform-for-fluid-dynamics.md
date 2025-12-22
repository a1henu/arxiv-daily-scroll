---
layout: default
title: HydroGym: A Reinforcement Learning Platform for Fluid Dynamics
---

# HydroGym: A Reinforcement Learning Platform for Fluid Dynamics
**arXiv**：[2512.17534v1](https://arxiv.org/abs/2512.17534) · [PDF](https://arxiv.org/pdf/2512.17534.pdf)  
**作者**：Christian Lagemann, Sajeda Mokbel, Miro Gondrum, Mario Rüttgers, Jared Callaham, Ludger Paehler, Samuel Ahnert, Nicholas Zolman, Kai Lagemann, Nikolaus Adams, Matthias Meinke, Wolfgang Schröder, Jean-Christophe Loiseau, Esther Lagemann, Steven L. Brunton  

**一句话要点**：提出HydroGym强化学习平台以解决流体控制中缺乏标准化基准和计算需求高的问题

**关键词**：流体动力学, 强化学习平台, 流控制基准, 可微求解器, 迁移学习, 计算流体力学

## 3 点简述
- 流体控制面临高维非线性挑战，缺乏标准化平台阻碍强化学习应用
- HydroGym集成42个验证环境，提供不可微和可微求解器以提升样本效率
- 实验显示控制器能发现鲁棒控制原则，迁移学习减少约50%训练回合

## 摘要（原文）

> Modeling and controlling fluid flows is critical for several fields of science and engineering, including transportation, energy, and medicine. Effective flow control can lead to, e.g., lift increase, drag reduction, mixing enhancement, and noise reduction. However, controlling a fluid faces several significant challenges, including high-dimensional, nonlinear, and multiscale interactions in space and time. Reinforcement learning (RL) has recently shown great success in complex domains, such as robotics and protein folding, but its application to flow control is hindered by a lack of standardized benchmark platforms and the computational demands of fluid simulations. To address these challenges, we introduce HydroGym, a solver-independent RL platform for flow control research. HydroGym integrates sophisticated flow control benchmarks, scalable runtime infrastructure, and state-of-the-art RL algorithms. Our platform includes 42 validated environments spanning from canonical laminar flows to complex three-dimensional turbulent scenarios, validated over a wide range of Reynolds numbers. We provide non-differentiable solvers for traditional RL and differentiable solvers that dramatically improve sample efficiency through gradient-enhanced optimization. Comprehensive evaluation reveals that RL agents consistently discover robust control principles across configurations, such as boundary layer manipulation, acoustic feedback disruption, and wake reorganization. Transfer learning studies demonstrate that controllers learned at one Reynolds number or geometry adapt efficiently to new conditions, requiring approximately 50% fewer training episodes. The HydroGym platform is highly extensible and scalable, providing a framework for researchers in fluid dynamics, machine learning, and control to add environments, surrogate models, and control algorithms to advance science and technology.


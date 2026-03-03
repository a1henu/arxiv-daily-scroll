---
layout: default
title: Towards Robot Skill Learning and Adaptation with Gaussian Processes
---

# Towards Robot Skill Learning and Adaptation with Gaussian Processes
**arXiv**：[2603.01480v1](https://arxiv.org/abs/2603.01480) · [PDF](https://arxiv.org/pdf/2603.01480.pdf)  
**作者**：A K M Nadimul Haque, Fouad Sukkar, Sheila Sujipto, Cedric Le Gentil, Marc G. Carmichael, Teresa Vidal-Calleja  

**一句话要点**：提出基于高斯过程的机器人技能学习与适应框架，以应对任务配置的大幅变化。

**关键词**：机器人技能学习, 高斯过程建模, 技能适应, 稀疏路径点, 运动学保持, 强化学习

## 3 点简述
- 核心问题：现有技能模型表达能力不足，难以适应环境的大幅变化。
- 方法要点：利用高斯过程稀疏路径点建模，结合优化、行为克隆和强化学习进行技能适应。
- 实验或效果：在模拟和硬件任务中，成功率超越基准，保持运动学特征。

## 摘要（原文）

> General robot skill adaptation requires expressive representations robust to varying task configurations. While recent learning-based skill adaptation methods refined via Reinforcement Learning (RL), have shown success, existing skill models often lack sufficient representational capacity for anything beyond minor environmental changes. In contrast, Gaussian Process (GP)-based skill modelling provides an expressive representation with useful analytical properties; however, adaptation of GP-based skills remains underexplored. This paper proposes a novel, robust skill adaptation framework that utilises GPs with sparse via-points for compact and expressive modelling. The model considers the trajectory's poses and leverages its first and second analytical derivatives to preserve the skill's kinematic profile. We present three adaptation methods to cater for the variability between initial and observed configurations. Firstly, an optimisation agent that adjusts the path's via-points while preserving the demonstration velocity. Second, a behaviour cloning agent trained to replicate output trajectories from the optimisation agent. Lastly, an RL agent that has learnt to modify via-points whilst maintaining the kinematic profile and enabling online capabilities. Evaluated across three tasks (drawer opening, cube-pushing and bar manipulation) in both simulation and hardware, our proposed methods outperform every benchmark in success rates. Furthermore, the results demonstrate that the GP-based representation enables all three methods to attain high cosine similarity and low velocity magnitude errors, indicating strong preservation of the kinematic profile. Overall, our formulation provides a compact representation capable of adapting to large deviations from a single demonstrated skill.


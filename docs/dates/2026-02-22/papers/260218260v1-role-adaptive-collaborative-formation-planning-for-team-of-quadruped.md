---
layout: default
title: Role-Adaptive Collaborative Formation Planning for Team of Quadruped Robots in Cluttered Environments
---

# Role-Adaptive Collaborative Formation Planning for Team of Quadruped Robots in Cluttered Environments
**arXiv**：[2602.18260v1](https://arxiv.org/abs/2602.18260) · [PDF](https://arxiv.org/pdf/2602.18260.pdf)  
**作者**：Magnus Norén, Marios-Nektarios Stamatopoulos, Avijit Banerjee, George Nikolakopoulos  

**一句话要点**：提出角色自适应协作编队规划框架，解决四足机器人团队在杂乱环境中的灵活导航问题。

**关键词**：四足机器人编队, 动态角色分配, 避障规划, 虚拟弹簧阻尼系统, Fast Marching Square算法, 杂乱环境导航

## 3 点简述
- 核心问题：传统方法在杂乱环境中固定领导或角色，导致编队僵化、避障困难。
- 方法要点：集成动态角色分配、部分目标规划和虚拟弹簧阻尼系统，结合FM2算法进行路径规划。
- 实验或效果：通过仿真和实物实验验证，展示平滑协调、自适应角色切换和鲁棒编队维护。

## 摘要（原文）

> This paper presents a role-adaptive Leader-Follower-based formation planning and control framework for teams of quadruped robots operating in cluttered environments. Unlike conventional methods with fixed leaders or rigid formation roles, the proposed approach integrates dynamic role assignment and partial goal planning, enabling flexible, collision-free navigation in complex scenarios. Formation stability and inter-robot safety are ensured through a virtual spring-damper system coupled with a novel obstacle avoidance layer that adaptively adjusts each agent's velocity. A dynamic look-ahead reference generator further enhances flexibility, allowing temporary formation deformation to maneuver around obstacles while maintaining goal-directed motion. The Fast Marching Square (FM2) algorithm provides the global path for the leader and local paths for the followers as the planning backbone. The framework is validated through extensive simulations and real-world experiments with teams of quadruped robots. Results demonstrate smooth coordination, adaptive role switching, and robust formation maintenance in complex, unstructured environments. A video featuring the simulation and physical experiments along with their associated visualizations can be found at https://youtu.be/scq37Tua9W4.


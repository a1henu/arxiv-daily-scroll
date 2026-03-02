---
layout: default
title: Learning to Build: Autonomous Robotic Assembly of Stable Structures Without Predefined Plans
---

# Learning to Build: Autonomous Robotic Assembly of Stable Structures Without Predefined Plans
**arXiv**：[2602.23934v1](https://arxiv.org/abs/2602.23934) · [PDF](https://arxiv.org/pdf/2602.23934.pdf)  
**作者**：Jingwen Wang, Johannes Kirschner, Paul Rolland, Luis Salamanca, Stefana Parascho  

**一句话要点**：提出基于强化学习的自主机器人装配框架，无需预定义蓝图即可构建稳定结构。

**关键词**：自主机器人装配, 强化学习, 后继特征, 无蓝图建造, 环境适应性, 闭环控制

## 3 点简述
- 核心问题：传统机器人装配依赖固定蓝图，难以适应环境不确定性和建造过程中的变化。
- 方法要点：使用深度Q学习和后继特征的强化学习策略，通过目标和障碍定义任务，实现灵活决策。
- 实验或效果：在15个2D离散块装配任务上评估，真实闭环机器人实验验证了方法的可行性和抗噪声能力。

## 摘要（原文）

> This paper presents a novel autonomous robotic assembly framework for constructing stable structures without relying on predefined architectural blueprints. Instead of following fixed plans, construction tasks are defined through targets and obstacles, allowing the system to adapt more flexibly to environmental uncertainty and variations during the building process. A reinforcement learning (RL) policy, trained using deep Q-learning with successor features, serves as the decision-making component. As a proof of concept, we evaluate the approach on a benchmark of 15 2D robotic assembly tasks of discrete block construction. Experiments using a real-world closed-loop robotic setup demonstrate the feasibility of the method and its ability to handle construction noise. The results suggest that our framework offers a promising direction for more adaptable and robust robotic construction in real-world environments.


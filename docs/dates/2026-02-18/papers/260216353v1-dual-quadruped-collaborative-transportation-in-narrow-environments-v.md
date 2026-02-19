---
layout: default
title: Dual-Quadruped Collaborative Transportation in Narrow Environments via Safe Reinforcement Learning
---

# Dual-Quadruped Collaborative Transportation in Narrow Environments via Safe Reinforcement Learning
**arXiv**：[2602.16353v1](https://arxiv.org/abs/2602.16353) · [PDF](https://arxiv.org/pdf/2602.16353.pdf)  
**作者**：Zhezhi Lei, Zhihai Bi, Wenxin Wang, Jun Ma  

**一句话要点**：提出基于安全强化学习的双四足机器人协作运输方法，以解决狭窄环境中的安全与性能挑战。

**关键词**：协作运输, 安全强化学习, 约束马尔可夫博弈, 四足机器人, 狭窄环境

## 3 点简述
- 核心问题：狭窄环境中多机器人协作运输的安全与性能难以保证，可行区域受限。
- 方法要点：建模为约束马尔可夫博弈，引入成本优势分解和约束分配方法，确保安全并优化任务奖励。
- 实验或效果：仿真与实时实验显示，相比现有方法，该方法性能更优且成功率更高。

## 摘要（原文）

> Collaborative transportation, where multiple robots collaboratively transport a payload, has garnered significant attention in recent years. While ensuring safe and high-performance inter-robot collaboration is critical for effective task execution, it is difficult to pursue in narrow environments where the feasible region is extremely limited. To address this challenge, we propose a novel approach for dual-quadruped collaborative transportation via safe reinforcement learning (RL). Specifically, we model the task as a fully cooperative constrained Markov game, where collision avoidance is formulated as constraints. We introduce a cost-advantage decomposition method that enforces the sum of team constraints to remain below an upper bound, thereby guaranteeing task safety within an RL framework. Furthermore, we propose a constraint allocation method that assigns shared constraints to individual robots to maximize the overall task reward, encouraging autonomous task-assignment among robots, thereby improving collaborative task performance. Simulation and real-time experimental results demonstrate that the proposed approach achieves superior performance and a higher success rate in dual-quadruped collaborative transportation compared to existing methods.


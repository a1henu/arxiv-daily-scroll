---
layout: default
title: TWISTED-RL: Hierarchical Skilled Agents for Knot-Tying without Human Demonstrations
---

# TWISTED-RL: Hierarchical Skilled Agents for Knot-Tying without Human Demonstrations
**arXiv**：[2602.14526v1](https://arxiv.org/abs/2602.14526) · [PDF](https://arxiv.org/pdf/2602.14526.pdf)  
**作者**：Guy Freund, Tom Jurgenson, Matan Sudry, Erez Karpas  

**一句话要点**：提出TWISTED-RL框架，通过分层强化学习实现无演示机器人打结

**关键词**：机器人打结, 分层强化学习, 无演示学习, 拓扑动作, 可变形物体操作

## 3 点简述
- 核心问题：机器人打结面临可变形物体交互和拓扑约束的复杂性挑战。
- 方法要点：用多步强化学习策略替代单步逆模型，基于抽象拓扑动作进行条件控制。
- 实验效果：成功解决更高复杂度结，如八字结和单结，提升成功率并减少规划时间。

## 摘要（原文）

> Robotic knot-tying represents a fundamental challenge in robotics due to the complex interactions between deformable objects and strict topological constraints. We present TWISTED-RL, a framework that improves upon the previous state-of-the-art in demonstration-free knot-tying (TWISTED), which smartly decomposed a single knot-tying problem into manageable subproblems, each addressed by a specialized agent. Our approach replaces TWISTED's single-step inverse model that was learned via supervised learning with a multi-step Reinforcement Learning policy conditioned on abstract topological actions rather than goal states. This change allows more delicate topological state transitions while avoiding costly and ineffective data collection protocols, thus enabling better generalization across diverse knot configurations. Experimental results demonstrate that TWISTED-RL manages to solve previously unattainable knots of higher complexity, including commonly used knots such as the Figure-8 and the Overhand. Furthermore, the increase in success rates and drop in planning time establishes TWISTED-RL as the new state-of-the-art in robotic knot-tying without human demonstrations.


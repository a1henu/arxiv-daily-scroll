---
layout: default
title: Accelerating Robotic Reinforcement Learning with Agent Guidance
---

# Accelerating Robotic Reinforcement Learning with Agent Guidance
**arXiv**：[2602.11978v1](https://arxiv.org/abs/2602.11978) · [PDF](https://arxiv.org/pdf/2602.11978.pdf)  
**作者**：Haojun Chen, Zili Zou, Chengdong Ma, Yaoxiang Pu, Haotong Zhang, Yuanpei Chen, Yaodong Yang  

**一句话要点**：提出AGPS框架，用多模态智能体替代人类监督，以加速机器人强化学习。

**关键词**：机器人强化学习, 样本效率, 智能体指导, 多模态智能体, 语义世界模型, 探索剪枝

## 3 点简述
- 核心问题：强化学习在机器人应用中样本效率低，人类监督方法存在可扩展性障碍。
- 方法要点：将智能体视为语义世界模型，通过工具提供精确指导，结构化物理探索。
- 实验或效果：在精度插入和可变形物体操作任务中，AGPS在样本效率上优于人类监督方法。

## 摘要（原文）

> Reinforcement Learning (RL) offers a powerful paradigm for autonomous robots to master generalist manipulation skills through trial-and-error. However, its real-world application is stifled by severe sample inefficiency. Recent Human-in-the-Loop (HIL) methods accelerate training by using human corrections, yet this approach faces a scalability barrier. Reliance on human supervisors imposes a 1:1 supervision ratio that limits fleet expansion, suffers from operator fatigue over extended sessions, and introduces high variance due to inconsistent human proficiency. We present Agent-guided Policy Search (AGPS), a framework that automates the training pipeline by replacing human supervisors with a multimodal agent. Our key insight is that the agent can be viewed as a semantic world model, injecting intrinsic value priors to structure physical exploration. By using executable tools, the agent provides precise guidance via corrective waypoints and spatial constraints for exploration pruning. We validate our approach on two tasks, ranging from precision insertion to deformable object manipulation. Results demonstrate that AGPS outperforms HIL methods in sample efficiency. This automates the supervision pipeline, unlocking the path to labor-free and scalable robot learning. Project website: https://agps-rl.github.io/agps.


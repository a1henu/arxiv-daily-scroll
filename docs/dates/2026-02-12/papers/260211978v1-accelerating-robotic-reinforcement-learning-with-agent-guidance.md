---
layout: default
title: Accelerating Robotic Reinforcement Learning with Agent Guidance
---

# Accelerating Robotic Reinforcement Learning with Agent Guidance
**arXiv**：[2602.11978v1](https://arxiv.org/abs/2602.11978) · [PDF](https://arxiv.org/pdf/2602.11978.pdf)  
**作者**：Haojun Chen, Zili Zou, Chengdong Ma, Yaoxiang Pu, Haotong Zhang, Yuanpei Chen, Yaodong Yang  

**一句话要点**：提出Agent-guided Policy Search以自动化机器人强化学习监督，提升样本效率。

**关键词**：机器人强化学习, 样本效率, 智能体指导, 多模态智能体, 语义世界模型

## 3 点简述
- 核心问题：强化学习在机器人操作中样本效率低，人机协同方法存在可扩展性限制。
- 方法要点：用多模态智能体替代人类监督，通过语义世界模型提供内在价值先验和空间约束指导。
- 实验或效果：在精度插入和可变形物体操作任务中，AGPS在样本效率上优于人机协同方法。

## 摘要（原文）

> Reinforcement Learning (RL) offers a powerful paradigm for autonomous robots to master generalist manipulation skills through trial-and-error. However, its real-world application is stifled by severe sample inefficiency. Recent Human-in-the-Loop (HIL) methods accelerate training by using human corrections, yet this approach faces a scalability barrier. Reliance on human supervisors imposes a 1:1 supervision ratio that limits fleet expansion, suffers from operator fatigue over extended sessions, and introduces high variance due to inconsistent human proficiency. We present Agent-guided Policy Search (AGPS), a framework that automates the training pipeline by replacing human supervisors with a multimodal agent. Our key insight is that the agent can be viewed as a semantic world model, injecting intrinsic value priors to structure physical exploration. By using executable tools, the agent provides precise guidance via corrective waypoints and spatial constraints for exploration pruning. We validate our approach on two tasks, ranging from precision insertion to deformable object manipulation. Results demonstrate that AGPS outperforms HIL methods in sample efficiency. This automates the supervision pipeline, unlocking the path to labor-free and scalable robot learning. Project website: https://agps-rl.github.io/agps.


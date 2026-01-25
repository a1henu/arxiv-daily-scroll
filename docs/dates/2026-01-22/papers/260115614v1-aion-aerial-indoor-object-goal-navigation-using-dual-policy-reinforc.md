---
layout: default
title: AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning
---

# AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning
**arXiv**：[2601.15614v1](https://arxiv.org/abs/2601.15614) · [PDF](https://arxiv.org/pdf/2601.15614.pdf)  
**作者**：Zichen Yan, Yuchen Hou, Shenao Wang, Yichao Gao, Rui Huang, Lin Zhao  

**一句话要点**：提出AION双策略强化学习框架，实现基于视觉的空中室内物体目标导航。

**关键词**：物体目标导航, 空中机器人, 强化学习, 双策略框架, 视觉导航

## 3 点简述
- 核心问题：扩展物体目标导航至空中平台，面临3D运动、感知与控制挑战。
- 方法要点：采用端到端双策略强化学习，分离探索与目标到达行为。
- 实验或效果：在AI2-THOR和IsaacSim中评估，展示优越的探索、导航效率与安全性。

## 摘要（原文）

> Object-Goal Navigation (ObjectNav) requires an agent to autonomously explore an unknown environment and navigate toward target objects specified by a semantic label. While prior work has primarily studied zero-shot ObjectNav under 2D locomotion, extending it to aerial platforms with 3D locomotion capability remains underexplored. Aerial robots offer superior maneuverability and search efficiency, but they also introduce new challenges in spatial perception, dynamic control, and safety assurance. In this paper, we propose AION for vision-based aerial ObjectNav without relying on external localization or global maps. AION is an end-to-end dual-policy reinforcement learning (RL) framework that decouples exploration and goal-reaching behaviors into two specialized policies. We evaluate AION on the AI2-THOR benchmark and further assess its real-time performance in IsaacSim using high-fidelity drone models. Experimental results show that AION achieves superior performance across comprehensive evaluation metrics in exploration, navigation efficiency, and safety. The video can be found at https://youtu.be/TgsUm6bb7zg.


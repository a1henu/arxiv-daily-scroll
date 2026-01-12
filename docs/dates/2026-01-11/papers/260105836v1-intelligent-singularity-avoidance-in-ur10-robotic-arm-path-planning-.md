---
layout: default
title: Intelligent Singularity Avoidance in UR10 Robotic Arm Path Planning Using Hybrid Fuzzy Logic and Reinforcement Learning
---

# Intelligent Singularity Avoidance in UR10 Robotic Arm Path Planning Using Hybrid Fuzzy Logic and Reinforcement Learning
**arXiv**：[2601.05836v1](https://arxiv.org/abs/2601.05836) · [PDF](https://arxiv.org/pdf/2601.05836.pdf)  
**作者**：Sheng-Kai Chen, Jyh-Horng Wu  

**一句话要点**：提出混合模糊逻辑与强化学习方法，以解决UR10机械臂路径规划中的奇异性规避问题。

**关键词**：机械臂路径规划, 奇异性规避, 模糊逻辑, 强化学习, 实时检测, 自适应控制

## 3 点简述
- 核心问题：机械臂奇异性导致控制失效和设备损坏，需实时检测与规避。
- 方法要点：结合模糊逻辑决策和强化学习框架，利用可操作性度量和条件数分析进行自适应路径规划。
- 实验或效果：实验显示90%成功率到达目标位置，同时保持与奇异配置的安全距离。

## 摘要（原文）

> This paper presents a comprehensive approach to singularity detection and avoidance in UR10 robotic arm path planning through the integration of fuzzy logic safety systems and reinforcement learning algorithms. The proposed system addresses critical challenges in robotic manipulation where singularities can cause loss of control and potential equipment damage. Our hybrid approach combines real-time singularity detection using manipulability measures, condition number analysis, and fuzzy logic decision-making with a stable reinforcement learning framework for adaptive path planning. Experimental results demonstrate a 90% success rate in reaching target positions while maintaining safe distances from singular configurations. The system integrates PyBullet simulation for training data collection and URSim connectivity for real-world deployment.


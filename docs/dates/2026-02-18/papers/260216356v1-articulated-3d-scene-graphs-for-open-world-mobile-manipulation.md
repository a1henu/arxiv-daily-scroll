---
layout: default
title: Articulated 3D Scene Graphs for Open-World Mobile Manipulation
---

# Articulated 3D Scene Graphs for Open-World Mobile Manipulation
**arXiv**：[2602.16356v1](https://arxiv.org/abs/2602.16356) · [PDF](https://arxiv.org/pdf/2602.16356.pdf)  
**作者**：Martin Büchner, Adrian Röfer, Tim Engelbracht, Tim Welschehold, Zuria Bauer, Hermann Blum, Marc Pollefeys, Abhinav Valada  

**一句话要点**：提出MoMa-SG框架以构建语义-运动学3D场景图，支持开放世界移动操作

**关键词**：3D场景图, 关节物体操作, 语义-运动学建模, RGB-D序列分析, 移动机器人

## 3 点简述
- 核心问题：机器人无法预测物体运动，需弥合语义、几何与运动学间的差距
- 方法要点：通过点跟踪和统一扭转估计，从RGB-D序列中推断物体关节参数
- 实验或效果：在真实数据集和机器人上验证，实现日常环境中对关节物体的稳健操作

## 摘要（原文）

> Semantics has enabled 3D scene understanding and affordance-driven object interaction. However, robots operating in real-world environments face a critical limitation: they cannot anticipate how objects move. Long-horizon mobile manipulation requires closing the gap between semantics, geometry, and kinematics. In this work, we present MoMa-SG, a novel framework for building semantic-kinematic 3D scene graphs of articulated scenes containing a myriad of interactable objects. Given RGB-D sequences containing multiple object articulations, we temporally segment object interactions and infer object motion using occlusion-robust point tracking. We then lift point trajectories into 3D and estimate articulation models using a novel unified twist estimation formulation that robustly estimates revolute and prismatic joint parameters in a single optimization pass. Next, we associate objects with estimated articulations and detect contained objects by reasoning over parent-child relations at identified opening states. We also introduce the novel Arti4D-Semantic dataset, which uniquely combines hierarchical object semantics including parent-child relation labels with object axis annotations across 62 in-the-wild RGB-D sequences containing 600 object interactions and three distinct observation paradigms. We extensively evaluate the performance of MoMa-SG on two datasets and ablate key design choices of our approach. In addition, real-world experiments on both a quadruped and a mobile manipulator demonstrate that our semantic-kinematic scene graphs enable robust manipulation of articulated objects in everyday home environments. We provide code and data at: https://momasg.cs.uni-freiburg.de.


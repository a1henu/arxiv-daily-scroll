---
layout: default
title: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
---

# Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
**arXiv**：[2602.16705v1](https://arxiv.org/abs/2602.16705) · [PDF](https://arxiv.org/pdf/2602.16705.pdf)  
**作者**：Runpei Dong, Ziyan Li, Xialin He, Saurabh Gupta  

**一句话要点**：提出HERO范式，结合大视觉模型与模拟训练，实现人形机器人开放词汇视觉移动操作

**关键词**：人形机器人控制, 视觉移动操作, 开放词汇理解, 末端执行器跟踪, 模拟训练, 大视觉模型

## 3 点简述
- 核心问题：现有基于真实世界模仿学习的方法泛化能力有限，因大规模数据集收集困难。
- 方法要点：设计残差感知末端执行器跟踪策略，结合逆运动学、学习前向模型、目标调整和重规划，降低跟踪误差3.2倍。
- 实验或效果：系统在办公室、咖啡店等多样真实环境中可靠操作日常物体，高度范围43cm至92cm。

## 摘要（原文）

> Visual loco-manipulation of arbitrary objects in the wild with humanoid robots requires accurate end-effector (EE) control and a generalizable understanding of the scene via visual inputs (e.g., RGB-D images). Existing approaches are based on real-world imitation learning and exhibit limited generalization due to the difficulty in collecting large-scale training datasets. This paper presents a new paradigm, HERO, for object loco-manipulation with humanoid robots that combines the strong generalization and open-vocabulary understanding of large vision models with strong control performance from simulated training. We achieve this by designing an accurate residual-aware EE tracking policy. This EE tracking policy combines classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, c) goal adjustment, and d) replanning. Together, these innovations help us cut down the end-effector tracking error by 3.2x. We use this accurate end-effector tracker to build a modular system for loco-manipulation, where we use open-vocabulary large vision models for strong visual generalization. Our system is able to operate in diverse real-world environments, from offices to coffee shops, where the robot is able to reliably manipulate various everyday objects (e.g., mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests in simulation and the real world demonstrate the effectiveness of our proposed design. We believe the advances in this paper can open up new ways of training humanoid robots to interact with daily objects.


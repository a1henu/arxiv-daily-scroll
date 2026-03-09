---
layout: default
title: Terrain characterization and locomotion adaptation in a small-scale lizard-inspired robot
---

# Terrain characterization and locomotion adaptation in a small-scale lizard-inspired robot
**arXiv**：[2603.05837v1](https://arxiv.org/abs/2603.05837) · [PDF](https://arxiv.org/pdf/2603.05837.pdf)  
**作者**：Duncan Andrews, Landon Zimmerman, Evan Martin, Joe DiGennaro, Baxi Chong  

**一句话要点**：提出小型蜥蜴机器人SILA Bot，通过本体感知与线性反馈控制实现复杂地形自适应运动。

**关键词**：小型机器人, 地形自适应, 本体感知, 颗粒介质, 线性控制, 运动模式优化

## 3 点简述
- 核心问题：小型机器人缺乏在复杂自然地形中感知与响应的系统理解。
- 方法要点：使用颗粒介质模拟地形，基于关节扭矩估计深度并参数化最优运动模式。
- 实验或效果：线性控制器显著提升未知深度地形上的运动性能，计算复杂度低。

## 摘要（原文）

> Unlike their large-scale counterparts, small-scale robots are largely confined to laboratory environments and are rarely deployed in real-world settings. As robot size decreases, robot-terrain interactions fundamentally change; however, there remains a lack of systematic understanding of what sensory information small-scale robots should acquire and how they should respond when traversing complex natural terrains. To address these challenges, we develop a Small-scale, Intelligent, Lizard-inspired, Adaptive Robot (SILA Bot) capable of adapting to diverse substrates. We use granular media of varying depths as a controlled yet representative terrain paradigm. We show that the optimal body movement pattern (ranging from standing-wave bending that assists limb retraction on flat ground to traveling-wave undulation that generates thrust in deep granular media) can be parameterized and approximated as a linear function of granular depth. Furthermore, proprioceptive signals, such as joint torque, provide sufficient information to estimate granular depth via a K-Nearest Neighbors classifier, achieving 95% accuracy. Leveraging these relationships, we design a simple linear feedback controller that modulates body phase and substantially improves locomotion performance on terrains with unknown depth. Together, these results establish a principled framework for perception and control in small-scale locomotion and enable effective terrain-adaptive locomotion while maintaining low computational complexity.


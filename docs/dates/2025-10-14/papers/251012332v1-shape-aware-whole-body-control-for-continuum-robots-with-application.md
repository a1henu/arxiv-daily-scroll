---
layout: default
title: Shape-Aware Whole-Body Control for Continuum Robots with Application in Endoluminal Surgical Robotics
---

# Shape-Aware Whole-Body Control for Continuum Robots with Application in Endoluminal Surgical Robotics
**arXiv**：[2510.12332v1](https://arxiv.org/abs/2510.12332) · [PDF](https://arxiv.org/pdf/2510.12332.pdf)  
**作者**：Mohammadreza Kasaei, Mostafa Ghobadi, Mohsen Khadem  

**一句话要点**：提出形状感知全身控制框架以解决内腔手术中连续机器人的精确导航问题

**关键词**：连续机器人控制, 内腔手术导航, 形状感知估计, 模型预测控制, 增强神经ODE, 避障优化

## 3 点简述
- 核心问题：内腔手术中传统仅尖端控制易导致壁接触和组织损伤，难以到达远端目标。
- 方法要点：结合物理模型与增强神经ODE，实现形状估计和高效雅可比计算，并采用MPPI控制器优化跟踪与避障。
- 实验或效果：仿真和真实机器人实验显示毫米级精度，减少壁接触，提高适应性。

## 摘要（原文）

> This paper presents a shape-aware whole-body control framework for
> tendon-driven continuum robots with direct application to endoluminal surgical
> navigation. Endoluminal procedures, such as bronchoscopy, demand precise and
> safe navigation through tortuous, patient-specific anatomy where conventional
> tip-only control often leads to wall contact, tissue trauma, or failure to
> reach distal targets. To address these challenges, our approach combines a
> physics-informed backbone model with residual learning through an Augmented
> Neural ODE, enabling accurate shape estimation and efficient Jacobian
> computation. A sampling-based Model Predictive Path Integral (MPPI) controller
> leverages this representation to jointly optimize tip tracking, backbone
> conformance, and obstacle avoidance under actuation constraints. A task manager
> further enhances adaptability by allowing real-time adjustment of objectives,
> such as wall clearance or direct advancement, during tele-operation. Extensive
> simulation studies demonstrate millimeter-level accuracy across diverse
> scenarios, including trajectory tracking, dynamic obstacle avoidance, and
> shape-constrained reaching. Real-robot experiments on a bronchoscopy phantom
> validate the framework, showing improved lumen-following accuracy, reduced wall
> contacts, and enhanced adaptability compared to joystick-only navigation and
> existing baselines. These results highlight the potential of the proposed
> framework to increase safety, reliability, and operator efficiency in minimally
> invasive endoluminal surgery, with broader applicability to other confined and
> safety-critical environments.


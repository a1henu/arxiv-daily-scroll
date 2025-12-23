---
layout: default
title: LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller
---

# LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller
**arXiv**：[2512.19576v1](https://arxiv.org/abs/2512.19576) · [PDF](https://arxiv.org/pdf/2512.19576.pdf)  
**作者**：Kirill Djebko, Tom Baumann, Erik Dilger, Frank Puppe, Sergio Montenegro  

**一句话要点**：提出LeLaR，首次在轨演示基于AI的卫星姿态控制器，用于惯性指向机动。

**关键词**：卫星姿态控制, 深度强化学习, Sim2Real, 在轨演示, 自适应控制, 纳米卫星

## 3 点简述
- 核心问题：传统控制器设计耗时且对模型不确定性和操作条件变化敏感，Sim2Real差距是部署挑战。
- 方法要点：使用深度强化学习在仿真中训练自适应控制策略，并部署到InnoCube纳米卫星进行在轨验证。
- 实验或效果：在轨演示成功，稳态指标确认AI控制器在重复机动中表现稳健，优于传统PD控制器。

## 摘要（原文）

> Attitude control is essential for many satellite missions. Classical controllers, however, are time-consuming to design and sensitive to model uncertainties and variations in operational boundary conditions. Deep Reinforcement Learning (DRL) offers a promising alternative by learning adaptive control strategies through autonomous interaction with a simulation environment. Overcoming the Sim2Real gap, which involves deploying an agent trained in simulation onto the real physical satellite, remains a significant challenge. In this work, we present the first successful in-orbit demonstration of an AI-based attitude controller for inertial pointing maneuvers. The controller was trained entirely in simulation and deployed to the InnoCube 3U nanosatellite, which was developed by the Julius-Maximilians-Universität Würzburg in cooperation with the Technische Universität Berlin, and launched in January 2025. We present the AI agent design, the methodology of the training procedure, the discrepancies between the simulation and the observed behavior of the real satellite, and a comparison of the AI-based attitude controller with the classical PD controller of InnoCube. Steady-state metrics confirm the robust performance of the AI-based controller during repeated in-orbit maneuvers.


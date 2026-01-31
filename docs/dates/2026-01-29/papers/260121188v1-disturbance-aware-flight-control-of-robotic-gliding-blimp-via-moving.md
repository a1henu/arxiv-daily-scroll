---
layout: default
title: Disturbance-Aware Flight Control of Robotic Gliding Blimp via Moving Mass Actuation
---

# Disturbance-Aware Flight Control of Robotic Gliding Blimp via Moving Mass Actuation
**arXiv**：[2601.21188v1](https://arxiv.org/abs/2601.21188) · [PDF](https://arxiv.org/pdf/2601.21188.pdf)  
**作者**：Hao Cheng, Feitian Zhang  

**一句话要点**：提出基于移动质量驱动的扰动感知飞行控制框架，以增强机器人滑翔飞艇在风扰环境下的稳定性。

**关键词**：机器人飞艇控制, 扰动感知, 移动质量驱动, 模型预测控制, 风扰补偿, 飞行稳定性

## 3 点简述
- 核心问题：机器人飞艇作为轻于空气平台，易受风扰动影响，缺乏扰动感知控制框架。
- 方法要点：结合移动水平估计器实时推断风扰，并集成模型预测控制器进行补偿，利用二自由度移动质量机制生成惯性及气动力矩。
- 实验或效果：在迎风和侧风条件下进行飞行实验，显示MHE-MPC框架显著优于基准PID控制，验证了扰动感知飞行的有效性。

## 摘要（原文）

> Robotic blimps, as lighter-than-air (LTA) aerial systems, offer long endurance and inherently safe operation but remain highly susceptible to wind disturbances. Building on recent advances in moving mass actuation, this paper addresses the lack of disturbance-aware control frameworks for LTA platforms by explicitly modeling and compensating for wind-induced effects. A moving horizon estimator (MHE) infers real-time wind perturbations and provides these estimates to a model predictive controller (MPC), enabling robust trajectory and heading regulation under varying wind conditions. The proposed approach leverages a two-degree-of-freedom (2-DoF) moving-mass mechanism to generate both inertial and aerodynamic moments for attitude and heading control, thereby enhancing flight stability in disturbance-prone environments. Extensive flight experiments under headwind and crosswind conditions show that the integrated MHE-MPC framework significantly outperforms baseline PID control, demonstrating its effectiveness for disturbance-aware LTA flight.


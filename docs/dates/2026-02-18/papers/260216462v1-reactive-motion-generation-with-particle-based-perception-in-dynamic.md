---
layout: default
title: Reactive Motion Generation With Particle-Based Perception in Dynamic Environments
---

# Reactive Motion Generation With Particle-Based Perception in Dynamic Environments
**arXiv**：[2602.16462v1](https://arxiv.org/abs/2602.16462) · [PDF](https://arxiv.org/pdf/2602.16462.pdf)  
**作者**：Xiyuan Zhao, Huijun Li, Lifeng Zhu, Zhikai Wei, Xianyi Zhu, Aiguo Song  

**一句话要点**：提出基于张量化粒子感知与MPPI的机器人反应式运动生成方法，以提升动态环境中的安全性与反应性。

**关键词**：反应式运动生成, 动态环境感知, 粒子滤波, 模型预测控制, 机器人避障, MPPI规划

## 3 点简述
- 核心问题：动态非结构化场景中，静态感知与系统动力学限制反应式运动生成，难以可靠建模动态障碍物并优化无碰撞轨迹。
- 方法要点：采用张量化粒子权重更新方案，显式维护障碍物速度与协方差，构建动态表示；提出障碍物感知的MPPI规划，联合传播机器人-障碍物动力学，预测与评估不确定性下的未来运动。
- 实验或效果：在模拟和嘈杂真实环境中验证，显式建模机器人-障碍物动力学显著提升性能，优于现有MPPI感知规划基线，有效避障。

## 摘要（原文）

> Reactive motion generation in dynamic and unstructured scenarios is typically subject to essentially static perception and system dynamics. Reliably modeling dynamic obstacles and optimizing collision-free trajectories under perceptive and control uncertainty are challenging. This article focuses on revealing tight connection between reactive planning and dynamic mapping for manipulators from a model-based perspective. To enable efficient particle-based perception with expressively dynamic property, we present a tensorized particle weight update scheme that explicitly maintains obstacle velocities and covariance meanwhile. Building upon this dynamic representation, we propose an obstacle-aware MPPI-based planning formulation that jointly propagates robot-obstacle dynamics, allowing future system motion to be predicted and evaluated under uncertainty. The model predictive method is shown to significantly improve safety and reactivity with dynamic surroundings. By applying our complete framework in simulated and noisy real-world environments, we demonstrate that explicit modeling of robot-obstacle dynamics consistently enhances performance over state-of-the-art MPPI-based perception-planning baselines avoiding multiple static and dynamic obstacles.


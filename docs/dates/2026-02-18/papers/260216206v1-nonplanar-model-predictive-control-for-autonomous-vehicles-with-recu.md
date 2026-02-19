---
layout: default
title: Nonplanar Model Predictive Control for Autonomous Vehicles with Recursive Sparse Gaussian Process Dynamics
---

# Nonplanar Model Predictive Control for Autonomous Vehicles with Recursive Sparse Gaussian Process Dynamics
**arXiv**：[2602.16206v1](https://arxiv.org/abs/2602.16206) · [PDF](https://arxiv.org/pdf/2602.16206.pdf)  
**作者**：Ahmad Amine, Kabir Puri, Viet-Anh Le, Rahul Mangharam  

**一句话要点**：提出非平面模型预测控制框架，结合递归稀疏高斯过程动力学，用于自动驾驶车辆在非平面地形中的实时适应。

**关键词**：非平面模型预测控制, 递归稀疏高斯过程, 自动驾驶车辆动力学, 几何感知建模, 实时适应, 参考跟踪

## 3 点简述
- 核心问题：自动驾驶车辆在非平面地形中面临复杂动力学建模挑战，传统平面模型难以准确描述。
- 方法要点：采用几何感知建模方法，学习残差高斯过程，并利用递归稀疏高斯过程实现实时动力学适应。
- 实验或效果：在自定义Isaac Sim环境中验证，通过模型预测路径积分控制器实现高跟踪精度于挑战性3D表面。

## 摘要（原文）

> This paper proposes a nonplanar model predictive control (MPC) framework for autonomous vehicles operating on nonplanar terrain. To approximate complex vehicle dynamics in such environments, we develop a geometry-aware modeling approach that learns a residual Gaussian Process (GP). By utilizing a recursive sparse GP, the framework enables real-time adaptation to varying terrain geometry. The effectiveness of the learned model is demonstrated in a reference-tracking task using a Model Predictive Path Integral (MPPI) controller. Validation within a custom Isaac Sim environment confirms the framework's capability to maintain high tracking accuracy on challenging 3D surfaces.


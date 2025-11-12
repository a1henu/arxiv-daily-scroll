---
layout: default
title: Dual-MPC Footstep Planning for Robust Quadruped Locomotion
---

# Dual-MPC Footstep Planning for Robust Quadruped Locomotion
**arXiv**：[2511.07921v1](https://arxiv.org/abs/2511.07921) · [PDF](https://arxiv.org/pdf/2511.07921.pdf)  
**作者**：Byeong-Il Ham, Hyun-Bin Kim, Jeonguk Kang, Keun Ha Choi, Kyung-Soo Kim  

**一句话要点**：提出双MPC脚步规划方法，以增强四足机器人对不期望身体旋转的鲁棒性。

**关键词**：脚步规划, 模型预测控制, 四足机器人, 角动量控制, 鲁棒运动

## 3 点简述
- 核心问题：传统方法忽略角速度，仅依赖地面反作用力控制角动量，导致性能不足。
- 方法要点：结合模型预测控制优化脚步位置和地面反作用力，形成双输入协调控制。
- 实验或效果：在四足机器人上验证，减少振荡，延长支撑和摆动相，适应多种地形。

## 摘要（原文）

> In this paper, we propose a footstep planning strategy based on model predictive control (MPC) that enables robust regulation of body orientation against undesired body rotations by optimizing footstep placement. Model-based locomotion approaches typically adopt heuristic methods or planning based on the linear inverted pendulum model. These methods account for linear velocity in footstep planning, while excluding angular velocity, which leads to angular momentum being handled exclusively via ground reaction force (GRF). Footstep planning based on MPC that takes angular velocity into account recasts the angular momentum control problem as a dual-input approach that coordinates GRFs and footstep placement, instead of optimizing GRFs alone, thereby improving tracking performance. A mutual-feedback loop couples the footstep planner and the GRF MPC, with each using the other's solution to iteratively update footsteps and GRFs. The use of optimal solutions reduces body oscillation and enables extended stance and swing phases. The method is validated on a quadruped robot, demonstrating robust locomotion with reduced oscillations, longer stance and swing phases across various terrains.


---
layout: default
title: Tendon-based modelling, estimation and control for a simulated high-DoF anthropomorphic hand model
---

# Tendon-based modelling, estimation and control for a simulated high-DoF anthropomorphic hand model
**arXiv**：[2601.20682v1](https://arxiv.org/abs/2601.20682) · [PDF](https://arxiv.org/pdf/2601.20682.pdf)  
**作者**：Péter Polcz, Katalin Schäffer, Miklós Koller  

**一句话要点**：提出基于肌腱位移和张力估计关节位置的计算方法，用于无关节编码器的仿人手机器人控制。

**关键词**：肌腱驱动控制, 关节位置估计, 非线性优化, 仿人手模型, MuJoCo模拟

## 3 点简述
- 核心问题：肌腱驱动仿人手机器人缺乏直接关节角度传感，影响机械紧凑性和灵巧性。
- 方法要点：基于Denavit-Hartenberg约定建立运动学模型，通过非线性优化从肌腱状态估计关节位置。
- 实验或效果：在MuJoCo模拟环境中使用高自由度手模型验证估计与控制框架的有效性和局限性。

## 摘要（原文）

> Tendon-driven anthropomorphic robotic hands often lack direct joint angle sensing, as the integration of joint encoders can compromise mechanical compactness and dexterity. This paper presents a computational method for estimating joint positions from measured tendon displacements and tensions. An efficient kinematic modeling framework for anthropomorphic hands is first introduced based on the Denavit-Hartenberg convention. Using a simplified tendon model, a system of nonlinear equations relating tendon states to joint positions is derived and solved via a nonlinear optimization approach. The estimated joint angles are then employed for closed-loop control through a Jacobian-based proportional-integral (PI) controller augmented with a feedforward term, enabling gesture tracking without direct joint sensing. The effectiveness and limitations of the proposed estimation and control framework are demonstrated in the MuJoCo simulation environment using the Anatomically Correct Biomechatronic Hand, featuring five degrees of freedom for each long finger and six degrees of freedom for the thumb.


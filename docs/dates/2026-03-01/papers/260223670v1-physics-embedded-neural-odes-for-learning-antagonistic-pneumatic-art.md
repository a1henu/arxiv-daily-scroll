---
layout: default
title: Physics-Embedded Neural ODEs for Learning Antagonistic Pneumatic Artificial Muscle Dynamics
---

# Physics-Embedded Neural ODEs for Learning Antagonistic Pneumatic Artificial Muscle Dynamics
**arXiv**：[2602.23670v1](https://arxiv.org/abs/2602.23670) · [PDF](https://arxiv.org/pdf/2602.23670.pdf)  
**作者**：Xinyao Wang, Jonathan Realmuto  

**一句话要点**：提出物理嵌入神经常微分方程框架，以学习拮抗式气动人工肌肉的非线性动态

**关键词**：神经常微分方程, 气动人工肌肉, 物理嵌入模型, 非线性动态, 刚度控制

## 3 点简述
- 拮抗式气动人工肌肉具有耦合、非线性和迟滞动态，建模与控制困难
- 结合参数化关节力学与神经网络力分量，嵌入物理结构于神经常微分方程
- 实验验证模型预测精度高，实现可靠刚度控制和一致阻抗行为

## 摘要（原文）

> Pneumatic artificial muscles (PAMs) enable compliant actuation for soft wearable, assistive, and interactive robots. When arranged antagonistically, PAMs can provide variable impedance through co-contraction but exhibit coupled, nonlinear, and hysteretic dynamics that challenge modeling and control. This paper presents a hybrid neural ordinary differential equation (Neural ODE) framework that embeds physical structure into a learned model of antagonistic PAM dynamics. The formulation combines parametric joint mechanics and pneumatic state dynamics with a neural network force component that captures antagonistic coupling and rate-dependent hysteresis. The forward model predicts joint motion and chamber pressures with a mean R$^2$ of 0.88 across 225 co-contraction conditions. An inverse formulation, derived from the learned dynamics, computes pressure commands offline for desired motion and stiffness profiles, tracked in closed loop during execution. Experimental validation demonstrates reliable stiffness control across 126-176 N/mm and consistent impedance behavior across operating velocities, in contrast to a static model, which shows degraded stiffness consistency at higher velocities.


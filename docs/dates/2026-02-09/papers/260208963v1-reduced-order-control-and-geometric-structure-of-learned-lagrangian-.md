---
layout: default
title: Reduced-order Control and Geometric Structure of Learned Lagrangian Latent Dynamics
---

# Reduced-order Control and Geometric Structure of Learned Lagrangian Latent Dynamics
**arXiv**：[2602.08963v1](https://arxiv.org/abs/2602.08963) · [PDF](https://arxiv.org/pdf/2602.08963.pdf)  
**作者**：Katharina Friedl, Noémie Jaquier, Seungyeon Kim, Jens Lundell, Danica Kragic  

**一句话要点**：提出基于学习拉格朗日隐空间动力学的降阶控制框架，用于高维机械系统。

**关键词**：降阶控制, 拉格朗日动力学, 隐空间学习, 结构保持模型, 稳定性分析, 高维系统

## 3 点简述
- 核心问题：高维机械系统缺乏精确物理模型，神经网络控制缺乏物理结构保证。
- 方法要点：学习结构保持的降阶动力学，推导跟踪控制律并分析稳定性条件。
- 实验或效果：在仿真和真实系统上验证理论分析和控制器准确性。

## 摘要（原文）

> Model-based controllers can offer strong guarantees on stability and convergence by relying on physically accurate dynamic models. However, these are rarely available for high-dimensional mechanical systems such as deformable objects or soft robots. While neural architectures can learn to approximate complex dynamics, they are either limited to low-dimensional systems or provide only limited formal control guarantees due to a lack of embedded physical structure. This paper introduces a latent control framework based on learned structure-preserving reduced-order dynamics for high-dimensional Lagrangian systems. We derive a reduced tracking law for fully actuated systems and adopt a Riemannian perspective on projection-based model-order reduction to study the resulting latent and projected closed-loop dynamics. By quantifying the sources of modeling error, we derive interpretable conditions for stability and convergence. We extend the proposed controller and analysis to underactuated systems by introducing learned actuation patterns. Experimental results on simulated and real-world systems validate our theoretical investigation and the accuracy of our controllers.


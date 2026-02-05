---
layout: default
title: Jacobian Regularization Stabilizes Long-Term Integration of Neural Differential Equations
---

# Jacobian Regularization Stabilizes Long-Term Integration of Neural Differential Equations
**arXiv**：[2602.04608v1](https://arxiv.org/abs/2602.04608) · [PDF](https://arxiv.org/pdf/2602.04608.pdf)  
**作者**：Maya Janvier, Julien Salomon, Etienne Meunier  

**一句话要点**：提出雅可比正则化以稳定短训练展开下神经微分方程的长时积分

**关键词**：神经微分方程, 雅可比正则化, 长时积分, 稳定性优化, 方向导数, 短训练展开

## 3 点简述
- 核心问题：神经微分方程在长时积分中易出现稳定性和精度问题，长展开训练成本高
- 方法要点：通过方向导数正则化雅可比矩阵，设计已知和未知动态的两种正则化方法
- 实验或效果：在常微分和偏微分方程中，以低成本显著提升长时模拟的稳定性

## 摘要（原文）

> Hybrid models and Neural Differential Equations (NDE) are getting increasingly important for the modeling of physical systems, however they often encounter stability and accuracy issues during long-term integration. Training on unrolled trajectories is known to limit these divergences but quickly becomes too expensive due to the need for computing gradients over an iterative process. In this paper, we demonstrate that regularizing the Jacobian of the NDE model via its directional derivatives during training stabilizes long-term integration in the challenging context of short training rollouts. We design two regularizations, one for the case of known dynamics where we can directly derive the directional derivatives of the dynamic and one for the case of unknown dynamics where they are approximated using finite differences. Both methods, while having a far lower cost compared to long rollouts during training, are successful in improving the stability of long-term simulations for several ordinary and partial differential equations, opening up the door to training NDE methods for long-term integration of large scale systems.


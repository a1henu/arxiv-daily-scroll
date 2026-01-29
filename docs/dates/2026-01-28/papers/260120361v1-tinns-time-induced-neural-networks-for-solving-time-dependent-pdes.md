---
layout: default
title: TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs
---

# TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs
**arXiv**：[2601.20361v1](https://arxiv.org/abs/2601.20361) · [PDF](https://arxiv.org/pdf/2601.20361.pdf)  
**作者**：Chen-Yang Dai, Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai, Chieh-Hsin Lai  

**一句话要点**：提出时间诱导神经网络以解决时间依赖偏微分方程中标准PINNs的精度与训练稳定性问题

**关键词**：时间依赖偏微分方程, 物理信息神经网络, 权重参数化, 非线性最小二乘优化, Levenberg-Marquardt方法, 网格无关求解

## 3 点简述
- 标准PINNs在时间依赖PDE中因共享权重导致特征耦合，影响精度和训练稳定性
- TINNs通过参数化网络权重为时间函数，使空间表示随时间演化，保持共享结构
- 实验显示TINNs在多种时间依赖PDE上精度提升达4倍，收敛速度加快10倍

## 摘要（原文）

> Physics-informed neural networks (PINNs) solve time-dependent partial differential equations (PDEs) by learning a mesh-free, differentiable solution that can be evaluated anywhere in space and time. However, standard space--time PINNs take time as an input but reuse a single network with shared weights across all times, forcing the same features to represent markedly different dynamics. This coupling degrades accuracy and can destabilize training when enforcing PDE, boundary, and initial constraints jointly. We propose Time-Induced Neural Networks (TINNs), a novel architecture that parameterizes the network weights as a learned function of time, allowing the effective spatial representation to evolve over time while maintaining shared structure. The resulting formulation naturally yields a nonlinear least-squares problem, which we optimize efficiently using a Levenberg--Marquardt method. Experiments on various time-dependent PDEs show up to $4\times$ improved accuracy and $10\times$ faster convergence compared to PINNs and strong baselines.


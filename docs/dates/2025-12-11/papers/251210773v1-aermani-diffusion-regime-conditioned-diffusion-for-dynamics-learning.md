---
layout: default
title: AERMANI-Diffusion: Regime-Conditioned Diffusion for Dynamics Learning in Aerial Manipulators
---

# AERMANI-Diffusion: Regime-Conditioned Diffusion for Dynamics Learning in Aerial Manipulators
**arXiv**：[2512.10773v1](https://arxiv.org/abs/2512.10773) · [PDF](https://arxiv.org/pdf/2512.10773.pdf)  
**作者**：Samaksh Ujjawal, Shivansh Pratap Singh, Naveen Sudheer Nair, Rishabh Dev Yadav, Wei Pan, Spandan Roy  

**一句话要点**：提出基于状态条件扩散的框架，以解决空中机械臂动力学建模中的非线性非平稳效应问题。

**关键词**：空中机械臂, 扩散模型, 动力学建模, 自适应控制, 残差学习

## 3 点简述
- 核心问题：空中机械臂因惯性耦合和空气动力快速变化，导致传统模型在非线性非平稳效应下精度不足。
- 方法要点：采用条件扩散过程建模残差力分布，结合轻量时间编码器提取运动配置摘要，提升预测一致性。
- 实验或效果：结合自适应控制器实现不确定性补偿，在真实测试中显著提高跟踪精度。

## 摘要（原文）

> Aerial manipulators undergo rapid, configuration-dependent changes in inertial coupling forces and aerodynamic forces, making accurate dynamics modeling a core challenge for reliable control. Analytical models lose fidelity under these nonlinear and nonstationary effects, while standard data-driven methods such as deep neural networks and Gaussian processes cannot represent the diverse residual behaviors that arise across different operating conditions. We propose a regime-conditioned diffusion framework that models the full distribution of residual forces using a conditional diffusion process and a lightweight temporal encoder. The encoder extracts a compact summary of recent motion and configuration, enabling consistent residual predictions even through abrupt transitions or unseen payloads. When combined with an adaptive controller, the framework enables dynamics uncertainty compensation and yields markedly improved tracking accuracy in real-world tests.


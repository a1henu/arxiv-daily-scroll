---
layout: default
title: Model Predictive Control via Probabilistic Inference: A Tutorial
---

# Model Predictive Control via Probabilistic Inference: A Tutorial
**arXiv**：[2511.08019v1](https://arxiv.org/abs/2511.08019) · [PDF](https://arxiv.org/pdf/2511.08019.pdf)  
**作者**：Kohei Honda  

**一句话要点**：提出基于概率推理的模型预测控制教程，以处理机器人中的非线性系统优化问题

**关键词**：模型预测控制, 概率推理, 最优控制, 机器人行为优化, 采样方法

## 3 点简述
- 核心问题：传统优化方法在非线性或不可微机器人系统中难以处理
- 方法要点：将最优控制重新解释为概率推理，使用采样技术估计控制分布
- 实验或效果：未知，但提供MPPI算法推导和调优原则作为实用指南

## 摘要（原文）

> Model Predictive Control (MPC) is a fundamental framework for optimizing robot behavior over a finite future horizon. While conventional numerical optimization methods can efficiently handle simple dynamics and cost structures, they often become intractable for the nonlinear or non-differentiable systems commonly encountered in robotics. This article provides a tutorial on probabilistic inference-based MPC, presenting a unified theoretical foundation and a comprehensive overview of representative methods. Probabilistic inference-based MPC approaches, such as Model Predictive Path Integral (MPPI) control, have gained significant attention by reinterpreting optimal control as a problem of probabilistic inference. Rather than relying on gradient-based numerical optimization, these methods estimate optimal control distributions through sampling-based techniques, accommodating arbitrary cost functions and dynamics. We first derive the optimal control distribution from the standard optimal control problem, elucidating its probabilistic interpretation and key characteristics. The widely used MPPI algorithm is then derived as a practical example, followed by discussions on prior and variational distribution design, tuning principles, and theoretical aspects. This article aims to serve as a systematic guide for researchers and practitioners seeking to understand, implement, and extend these methods in robotics and beyond.


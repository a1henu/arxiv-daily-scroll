---
layout: default
title: Optimal Derivative Feedback Control for an Active Magnetic Levitation System: An Experimental Study on Data-Driven Approaches
---

# Optimal Derivative Feedback Control for an Active Magnetic Levitation System: An Experimental Study on Data-Driven Approaches
**arXiv**：[2602.06944v1](https://arxiv.org/abs/2602.06944) · [PDF](https://arxiv.org/pdf/2602.06944.pdf)  
**作者**：Saber Omidi, Rene Akupan Ebunle, Se Young Yoon  

**一句话要点**：提出基于强化学习的无模型最优导数反馈控制，用于主动磁悬浮系统，并通过实验验证其优于基于辨识模型的间接方法。

**关键词**：主动磁悬浮系统, 最优导数反馈控制, 强化学习, 无模型控制, 系统辨识, 策略迭代

## 3 点简述
- 核心问题：设计主动磁悬浮系统的最优导数反馈控制器，比较无模型与基于辨识模型的方法。
- 方法要点：直接方法采用强化学习策略迭代，引入epoch循环收集多组数据以减少学习偏差；间接方法基于DMDc和PEM辨识的数学模型。
- 实验或效果：实验表明，当允许多epoch迭代时，直接无模型方法在稳定性和性能上优于间接方法，后者依赖单组数据。

## 摘要（原文）

> This paper presents the design and implementation of data-driven optimal derivative feedback controllers for an active magnetic levitation system. A direct, model-free control design method based on the reinforcement learning framework is compared with an indirect optimal control design derived from a numerically identified mathematical model of the system. For the direct model-free approach, a policy iteration procedure is proposed, which adds an iteration layer called the epoch loop to gather multiple sets of process data, providing a more diverse dataset and helping reduce learning biases. This direct control design method is evaluated against a comparable optimal control solution designed from a plant model obtained through the combined Dynamic Mode Decomposition with Control (DMDc) and Prediction Error Minimization (PEM) system identification. Results show that while both controllers can stabilize and improve the performance of the magnetic levitation system when compared to controllers designed from a nominal model, the direct model-free approach consistently outperforms the indirect solution when multiple epochs are allowed. The iterative refinement of the optimal control law over the epoch loop provides the direct approach a clear advantage over the indirect method, which relies on a single set of system data to determine the identified model and control.


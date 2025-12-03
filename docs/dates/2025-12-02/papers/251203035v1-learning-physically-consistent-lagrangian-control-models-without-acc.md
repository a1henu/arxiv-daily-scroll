---
layout: default
title: Learning Physically Consistent Lagrangian Control Models Without Acceleration Measurements
---

# Learning Physically Consistent Lagrangian Control Models Without Acceleration Measurements
**arXiv**：[2512.03035v1](https://arxiv.org/abs/2512.03035) · [PDF](https://arxiv.org/pdf/2512.03035.pdf)  
**作者**：Ibrahim Laiche, Mokrane Boudaoud, Patrick Gallinari, Pascal Morin  

**一句话要点**：提出基于损失函数的算法以提升拉格朗日系统物理一致性，无需加速度测量

**关键词**：拉格朗日系统, 物理一致性, 神经网络, 模型学习, 非线性控制, 损失函数

## 3 点简述
- 核心问题：拉格朗日或哈密顿神经网络在有限、部分和噪声数据下易产生物理不一致模型
- 方法要点：设计原始损失函数，改进模型物理一致性，支持基于模型的非线性控制
- 实验或效果：在仿真和实验系统中，相比其他学习方法，物理一致性显著提升

## 摘要（原文）

> This article investigates the modeling and control of Lagrangian systems involving non-conservative forces using a hybrid method that does not require acceleration calculations. It focuses in particular on the derivation and identification of physically consistent models, which are essential for model-based control synthesis. Lagrangian or Hamiltonian neural networks provide useful structural guarantees but the learning of such models often leads to inconsistent models, especially on real physical systems where training data are limited, partial and noisy. Motivated by this observation and the objective to exploit these models for model-based nonlinear control, a learning algorithm relying on an original loss function is proposed to improve the physical consistency of Lagrangian systems. A comparative analysis of different learning-based modeling approaches with the proposed solution shows significant improvements in terms of physical consistency of the learned models, on both simulated and experimental systems. The model's consistency is then exploited to demonstrate, on an experimental benchmark, the practical relevance of the proposed methodology for feedback linearization and energy-based control techniques.


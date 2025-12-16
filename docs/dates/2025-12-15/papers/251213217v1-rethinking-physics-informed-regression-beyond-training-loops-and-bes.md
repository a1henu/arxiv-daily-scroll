---
layout: default
title: Rethinking Physics-Informed Regression Beyond Training Loops and Bespoke Architectures
---

# Rethinking Physics-Informed Regression Beyond Training Loops and Bespoke Architectures
**arXiv**：[2512.13217v1](https://arxiv.org/abs/2512.13217) · [PDF](https://arxiv.org/pdf/2512.13217.pdf)  
**作者**：Lorenzo Sabug, Eric Kerrigan  

**一句话要点**：提出基于约束优化的物理信息回归方法，直接计算预测点状态，无需训练循环。

**关键词**：物理信息回归, 约束优化, 多元泰勒展开, 反应-扩散系统, 无训练预测

## 3 点简述
- 核心问题：传统物理信息回归依赖全局函数逼近器如神经网络，需长训练循环且对采样布局敏感。
- 方法要点：将每个预测建模为约束优化问题，利用多元泰勒展开并显式强制物理定律，实现低计算成本查询。
- 实验或效果：在反应-扩散系统上，与神经网络方法相比，预测精度竞争，同时消除训练需求并保持对采样布局的鲁棒性。

## 摘要（原文）

> We revisit the problem of physics-informed regression, and propose a method that directly computes the state at the prediction point, simultaneously with the derivative and curvature information of the existing samples. We frame each prediction as a constrained optimisation problem, leveraging multivariate Taylor series expansions and explicitly enforcing physical laws. Each individual query can be processed with low computational cost without any pre- or re-training, in contrast to global function approximator-based solutions such as neural networks. Our comparative benchmarks on a reaction-diffusion system show competitive predictive accuracy relative to a neural network-based solution, while completely eliminating the need for long training loops, and remaining robust to changes in the sampling layout.


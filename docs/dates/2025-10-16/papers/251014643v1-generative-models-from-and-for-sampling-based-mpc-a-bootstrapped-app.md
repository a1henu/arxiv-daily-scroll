---
layout: default
title: Generative Models From and For Sampling-Based MPC: A Bootstrapped Approach For Adaptive Contact-Rich Manipulation
---

# Generative Models From and For Sampling-Based MPC: A Bootstrapped Approach For Adaptive Contact-Rich Manipulation
**arXiv**：[2510.14643v1](https://arxiv.org/abs/2510.14643) · [PDF](https://arxiv.org/pdf/2510.14643.pdf)  
**作者**：Lara Brudermüller, Brandon Hung, Xinghao Zhu, Jiuguang Wang, Nick Hawes, Preston Culbertson, Simon Le Cleac'h  

**一句话要点**：提出生成预测控制框架，通过条件流匹配模型摊销采样MPC，用于接触丰富的机器人操作。

**关键词**：生成预测控制, 采样模型预测控制, 条件流匹配, 机器人操作, 接触丰富任务, 样本效率

## 3 点简述
- 核心问题：采样模型预测控制在线规划效率低，难以适应接触丰富的机器人任务。
- 方法要点：利用模拟数据训练条件流匹配模型，学习有意义的提议分布以指导采样。
- 实验或效果：在仿真和硬件实验中提高样本效率，减少规划视野，并展示任务泛化能力。

## 摘要（原文）

> We present a generative predictive control (GPC) framework that amortizes
> sampling-based Model Predictive Control (SPC) by bootstrapping it with
> conditional flow-matching models trained on SPC control sequences collected in
> simulation. Unlike prior work relying on iterative refinement or gradient-based
> solvers, we show that meaningful proposal distributions can be learned directly
> from noisy SPC data, enabling more efficient and informed sampling during
> online planning. We further demonstrate, for the first time, the application of
> this approach to real-world contact-rich loco-manipulation with a quadruped
> robot. Extensive experiments in simulation and on hardware show that our method
> improves sample efficiency, reduces planning horizon requirements, and
> generalizes robustly across task variations.


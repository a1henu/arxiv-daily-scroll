---
layout: default
title: Iterative Tuning of Nonlinear Model Predictive Control for Robotic Manufacturing Tasks
---

# Iterative Tuning of Nonlinear Model Predictive Control for Robotic Manufacturing Tasks
**arXiv**：[2512.13170v1](https://arxiv.org/abs/2512.13170) · [PDF](https://arxiv.org/pdf/2512.13170.pdf)  
**作者**：Deepak Ingole, Valentin Bhend, Shiva Ganesh Murali, Oliver Dobrich, Alisa Rupenayan  

**一句话要点**：提出基于任务级反馈的迭代学习框架，用于自动调优非线性模型预测控制权重，以应对机器人制造任务中的环境漂移和系统磨损。

**关键词**：非线性模型预测控制, 迭代学习控制, 机器人制造, 自适应调优, 经验灵敏度矩阵

## 3 点简述
- 核心问题：制造过程常受环境漂移和系统磨损扰动，需在重复操作中重新调优控制参数。
- 方法要点：采用迭代学习控制思想，通过经验灵敏度矩阵自适应调整NMPC权重，避免解析导数计算。
- 实验或效果：在UR10e机器人碳纤维缠绕仿真中，仅4次在线重复即达到接近离线贝叶斯优化的跟踪性能。

## 摘要（原文）

> Manufacturing processes are often perturbed by drifts in the environment and wear in the system, requiring control re-tuning even in the presence of repetitive operations. This paper presents an iterative learning framework for automatic tuning of Nonlinear Model Predictive Control (NMPC) weighting matrices based on task-level performance feedback. Inspired by norm-optimal Iterative Learning Control (ILC), the proposed method adaptively adjusts NMPC weights Q and R across task repetitions to minimize key performance indicators (KPIs) related to tracking accuracy, control effort, and saturation. Unlike gradient-based approaches that require differentiating through the NMPC solver, we construct an empirical sensitivity matrix, enabling structured weight updates without analytic derivatives. The framework is validated through simulation on a UR10e robot performing carbon fiber winding on a tetrahedral core. Results demonstrate that the proposed approach converges to near-optimal tracking performance (RMSE within 0.3% of offline Bayesian Optimization (BO)) in just 4 online repetitions, compared to 100 offline evaluations required by BO algorithm. The method offers a practical solution for adaptive NMPC tuning in repetitive robotic tasks, combining the precision of carefully optimized controllers with the flexibility of online adaptation.


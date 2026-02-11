---
layout: default
title: Adaptive recurrent flow map operator learning for reaction diffusion dynamics
---

# Adaptive recurrent flow map operator learning for reaction diffusion dynamics
**arXiv**：[2602.09487v1](https://arxiv.org/abs/2602.09487) · [PDF](https://arxiv.org/pdf/2602.09487.pdf)  
**作者**：Huseyin Tunc  

**一句话要点**：提出自适应循环训练的数据驱动算子学习器，以稳定预测反应扩散动力学的长期动态。

**关键词**：反应扩散动力学, 算子学习, 自适应训练, 零样本泛化, 长期预测, 数据驱动方法

## 3 点简述
- 核心问题：反应扩散方程的长时动态预测中，自回归算子易因误差累积漂移，且分布外初始条件降低准确性。
- 方法要点：采用自适应循环训练策略，通过轻量验证里程碑提前退出无效展开段并重定向优化，无需物理残差。
- 实验或效果：在FitzHugh-Nagumo等系统上，仅用短时分布内数据训练，实现零样本泛化，比基于物理损失的算子学习器快数倍。

## 摘要（原文）

> Reaction-diffusion (RD) equations underpin pattern formation across chemistry, biology, and physics, yet learning stable operators that forecast their long-term dynamics from data remains challenging. Neural-operator surrogates provide resolution-robust prediction, but autoregressive rollouts can drift due to the accumulation of error, and out-of-distribution (OOD) initial conditions often degrade accuracy. Physics-based numerical residual objectives can regularize operator learning, although they introduce additional assumptions, sensitivity to discretization and loss design, and higher training cost. Here we develop a purely data-driven operator learner with adaptive recurrent training (DDOL-ART) using a robust recurrent strategy with lightweight validation milestones that early-exit unproductive rollout segments and redirect optimization. Trained only on a single in-distribution toroidal Gaussian family over short horizons, DDOL-ART learns one-step operators that remain stable under long rollouts and generalize zero-shot to strong morphology shifts across FitzHugh-Nagumo (FN), Gray-Scott (GS), and Lambda-Omega (LO) systems. Across these benchmarks, DDOL-ART delivers a strong accuracy and cost trade-off. It is several-fold faster than a physics-based numerical-loss operator learner (NLOL) under matched settings, and it remains competitive on both in-distribution stability and OOD robustness. Training-dynamics diagnostics show that adaptivity strengthens the correlation between validation error and OOD test error performance, acting as a feedback controller that limits optimization drift. Our results indicate that feedback-controlled recurrent training of DDOL-ART generates robust flow-map surrogates without PDE residuals, while simultaneously maintaining competitiveness with NLOL at significantly reduced training costs.


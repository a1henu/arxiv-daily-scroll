---
layout: default
title: Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations
---

# Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations
**arXiv**：[2602.12706v1](https://arxiv.org/abs/2602.12706) · [PDF](https://arxiv.org/pdf/2602.12706.pdf)  
**作者**：Heechang Kim, Qianying Cao, Hyomin Shin, Seungchul Lee, George Em Karniadakis, Minseok Choi  

**一句话要点**：提出物理信息拉普拉斯神经算子以解决小数据和分布外泛化问题

**关键词**：神经算子, 物理信息学习, 偏微分方程求解, 小数据泛化, 分布外泛化

## 3 点简述
- 核心问题：数据驱动神经算子在小数据和分布外输入时泛化能力差
- 方法要点：嵌入物理残差，引入虚拟输入和时间因果加权增强训练
- 实验或效果：在四个基准测试中提升小数据准确性，减少变异性，增强泛化

## 摘要（原文）

> Neural operators have emerged as fast surrogate solvers for parametric partial differential equations (PDEs). However, purely data-driven models often require extensive training data and can generalize poorly, especially in small-data regimes and under unseen (out-of-distribution) input functions that are not represented in the training data. To address these limitations, we propose the Physics-Informed Laplace Neural Operator (PILNO), which enhances the Laplace Neural Operator (LNO) by embedding governing physics into training through PDE, boundary condition, and initial condition residuals. To improve expressivity, we first introduce an Advanced LNO (ALNO) backbone that retains a pole-residue transient representation while replacing the steady-state branch with an FNO-style Fourier multiplier. To make physics-informed training both data-efficient and robust, PILNO further leverages (i) virtual inputs: an unlabeled ensemble of input functions spanning a broad spectral range that provides abundant physics-only supervision and explicitly targets out-of-distribution (OOD) regimes; and (ii) temporal-causality weighting: a time-decaying reweighting of the physics residual that prioritizes early-time dynamics and stabilizes optimization for time-dependent PDEs. Across four representative benchmarks -- Burgers' equation, Darcy flow, a reaction-diffusion system, and a forced KdV equation -- PILNO consistently improves accuracy in small-data settings (e.g., N_train <= 27), reduces run-to-run variability across random seeds, and achieves stronger OOD generalization than purely data-driven baselines.


---
layout: default
title: Safe and Robust Domains of Attraction for Discrete-Time Systems: A Set-Based Characterization and Certifiable Neural Network Estimation
---

# Safe and Robust Domains of Attraction for Discrete-Time Systems: A Set-Based Characterization and Certifiable Neural Network Estimation
**arXiv**：[2603.03082v1](https://arxiv.org/abs/2603.03082) · [PDF](https://arxiv.org/pdf/2603.03082.pdf)  
**作者**：Mohamed Serry, Maxwell Fitzsimmons, Jun Liu  

**一句话要点**：提出基于集合表征与神经网络估计的框架，以解决离散时间非线性不确定系统安全鲁棒吸引域估计问题。

**关键词**：吸引域估计, 非线性系统, 物理信息神经网络, 鲁棒不变集, 形式验证, 离散时间系统

## 3 点简述
- 核心问题：非线性不确定系统在状态约束下吸引域估计的理论与计算挑战。
- 方法要点：引入度量空间上的值函数表征吸引域，并嵌入Bellman型方程训练物理信息神经网络。
- 实验或效果：通过四个数值示例验证方法有效性，并与现有方法比较性能。

## 摘要（原文）

> Analyzing nonlinear systems with attracting robust invariant sets (RISs) requires estimating their domains of attraction (DOAs). Despite extensive research, accurately characterizing DOAs for general nonlinear systems remains challenging due to both theoretical and computational limitations, particularly in the presence of uncertainties and state constraints. In this paper, we propose a novel framework for the accurate estimation of safe (state-constrained) and robust DOAs for discrete-time nonlinear uncertain systems with continuous dynamics, open safe sets, compact disturbance sets, and uniformly locally $\ell_p$-stable compact RISs. The notion of uniform $\ell_p$ stability is quite general and encompasses, as special cases, uniform exponential and polynomial stability. The DOAs are characterized via newly introduced value functions defined on metric spaces of compact sets. We establish their fundamental mathematical properties and derive the associated Bellman-type (Zubov-type) functional equations. Building on this characterization, we develop a physics-informed neural network (NN) framework to learn the corresponding value functions by embedding the derived Bellman-type equations directly into the training process. To obtain certifiable estimates of the safe robust DOAs from the learned neural approximations, we further introduce a verification procedure that leverages existing formal verification tools. The effectiveness and applicability of the proposed methodology are demonstrated through four numerical examples involving nonlinear uncertain systems subject to state constraints, and its performance is compared with existing methods from the literature.


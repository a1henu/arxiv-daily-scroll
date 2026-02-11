---
layout: default
title: Differentiable Modeling for Low-Inertia Grids: Benchmarking PINNs, NODEs, and DP for Identification and Control of SMIB System
---

# Differentiable Modeling for Low-Inertia Grids: Benchmarking PINNs, NODEs, and DP for Identification and Control of SMIB System
**arXiv**：[2602.09667v1](https://arxiv.org/abs/2602.09667) · [PDF](https://arxiv.org/pdf/2602.09667.pdf)  
**作者**：Shinhoo Kang, Sangwook Kim, Sehyun Yun  

**一句话要点**：比较PINNs、NODEs和DP在低惯性电网SMIB系统建模与控制中的性能

**关键词**：低惯性电网建模, 可微分编程, 物理信息神经网络, 神经常微分方程, SMIB系统控制, 参数识别

## 3 点简述
- 核心问题：低惯性电网需精确状态预测和物理一致灵敏度以支持控制，不同可微分建模范式控制影响未知
- 方法要点：以SMIB为基准，评估PINNs、NODEs和DP在轨迹外推、参数估计和LQR控制中的表现
- 实验或效果：NODE外推优，PINN泛化有限；DP参数识别收敛快；DP控制稳定性接近理论最优，NODE可作为无方程数据驱动替代

## 摘要（原文）

> The transition toward low-inertia power systems demands modeling frameworks that provide not only accurate state predictions but also physically consistent sensitivities for control. While scientific machine learning offers powerful nonlinear modeling tools, the control-oriented implications of different differentiable paradigms remain insufficiently understood. This paper presents a comparative study of Physics-Informed Neural Networks (PINNs), Neural Ordinary Differential Equations (NODEs), and Differentiable Programming (DP) for modeling, identification, and control of power system dynamics. Using the Single Machine Infinite Bus (SMIB) system as a benchmark, we evaluate their performance in trajectory extrapolation, parameter estimation, and Linear Quadratic Regulator (LQR) synthesis.
>   Our results highlight a fundamental trade-off between data-driven flexibility and physical structure. NODE exhibits superior extrapolation by capturing the underlying vector field, whereas PINN shows limited generalization due to its reliance on a time-dependent solution map. In the inverse problem of parameter identification, while both DP and PINN successfully recover the unknown parameters, DP achieves significantly faster convergence by enforcing governing equations as hard constraints. Most importantly, for control synthesis, the DP framework yields closed-loop stability comparable to the theoretical optimum. Furthermore, we demonstrate that NODE serves as a viable data-driven surrogate when governing equations are unavailable.


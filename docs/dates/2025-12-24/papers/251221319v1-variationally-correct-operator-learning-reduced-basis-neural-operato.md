---
layout: default
title: Variationally correct operator learning: Reduced basis neural operator with a posteriori error estimation
---

# Variationally correct operator learning: Reduced basis neural operator with a posteriori error estimation
**arXiv**：[2512.21319v1](https://arxiv.org/abs/2512.21319) · [PDF](https://arxiv.org/pdf/2512.21319.pdf)  
**作者**：Yuan Qiu, Wolfgang Dahmen, Peng Chen  

**一句话要点**：提出变分正确算子学习框架，通过FOSLS损失和降基神经算子解决PDE残差损失缺乏变分正确性问题。

**关键词**：算子学习, 变分正确性, 一阶系统最小二乘, 降基神经算子, 后验误差估计, 偏微分方程

## 3 点简述
- 核心问题：标准PDE残差损失因使用非合规范数或边界条件惩罚项，导致小残差不保证小解误差。
- 方法要点：构建一阶系统最小二乘目标，其值在PDE诱导范数下等价于解误差，并设计降基神经算子确保函数空间合规性。
- 实验或效果：数值基准测试验证理论误差界，在PDE合规范数下实现优于基线的精度，残差损失作为可靠后验误差估计器。

## 摘要（原文）

> Minimizing PDE-residual losses is a common strategy to promote physical consistency in neural operators. However, standard formulations often lack variational correctness, meaning that small residuals do not guarantee small solution errors due to the use of non-compliant norms or ad hoc penalty terms for boundary conditions. This work develops a variationally correct operator learning framework by constructing first-order system least-squares (FOSLS) objectives whose values are provably equivalent to the solution error in PDE-induced norms. We demonstrate this framework on stationary diffusion and linear elasticity, incorporating mixed Dirichlet-Neumann boundary conditions via variational lifts to preserve norm equivalence without inconsistent penalties. To ensure the function space conformity required by the FOSLS loss, we propose a Reduced Basis Neural Operator (RBNO). The RBNO predicts coefficients for a pre-computed, conforming reduced basis, thereby ensuring variational stability by design while enabling efficient training. We provide a rigorous convergence analysis that bounds the total error by the sum of finite element discretization bias, reduced basis truncation error, neural network approximation error, and statistical estimation errors arising from finite sampling and optimization. Numerical benchmarks validate these theoretical bounds and demonstrate that the proposed approach achieves superior accuracy in PDE-compliant norms compared to standard baselines, while the residual loss serves as a reliable, computable a posteriori error estimator.


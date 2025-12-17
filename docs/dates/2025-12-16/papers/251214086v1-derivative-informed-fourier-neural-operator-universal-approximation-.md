---
layout: default
title: Derivative-Informed Fourier Neural Operator: Universal Approximation and Applications to PDE-Constrained Optimization
---

# Derivative-Informed Fourier Neural Operator: Universal Approximation and Applications to PDE-Constrained Optimization
**arXiv**：[2512.14086v1](https://arxiv.org/abs/2512.14086) · [PDF](https://arxiv.org/pdf/2512.14086.pdf)  
**作者**：Boyuan Yao, Dingcheng Luo, Lianghao Cao, Nikola Kovachki, Thomas O'Leary-Roseberry, Omar Ghattas  

**一句话要点**：提出导数信息傅里叶神经算子以解决偏微分方程约束优化中的高精度代理建模问题

**关键词**：傅里叶神经算子, 偏微分方程约束优化, 导数信息学习, 代理建模, 无限维优化

## 3 点简述
- 核心问题：传统傅里叶神经算子作为代理模型在偏微分方程约束优化中导数精度不足，影响优化效果
- 方法要点：通过联合最小化输出和Fréchet导数误差训练导数信息傅里叶神经算子，提升敏感度模拟能力
- 实验或效果：在非线性扩散-反应、Helmholtz和Navier-Stokes方程上验证了样本效率高和低训练样本下的高精度

## 摘要（原文）

> We present approximation theories and efficient training methods for derivative-informed Fourier neural operators (DIFNOs) with applications to PDE-constrained optimization. A DIFNO is an FNO trained by minimizing its prediction error jointly on output and Fréchet derivative samples of a high-fidelity operator (e.g., a parametric PDE solution operator). As a result, a DIFNO can closely emulate not only the high-fidelity operator's response but also its sensitivities. To motivate the use of DIFNOs instead of conventional FNOs as surrogate models, we show that accurate surrogate-driven PDE-constrained optimization requires accurate surrogate Fréchet derivatives. Then, for continuously differentiable operators, we establish (i) simultaneous universal approximation of FNOs and their Fréchet derivatives on compact sets, and (ii) universal approximation of FNOs in weighted Sobolev spaces with input measures that have unbounded supports. Our theoretical results certify the capability of FNOs for accurate derivative-informed operator learning and accurate solution of PDE-constrained optimization. Furthermore, we develop efficient training schemes using dimension reduction and multi-resolution techniques that significantly reduce memory and computational costs for Fréchet derivative learning. Numerical examples on nonlinear diffusion--reaction, Helmholtz, and Navier--Stokes equations demonstrate that DIFNOs are superior in sample complexity for operator learning and solving infinite-dimensional PDE-constrained inverse problems, achieving high accuracy at low training sample sizes.


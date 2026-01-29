---
layout: default
title: Neural Quantum States in Mixed Precision
---

# Neural Quantum States in Mixed Precision
**arXiv**：[2601.20782v1](https://arxiv.org/abs/2601.20782) · [PDF](https://arxiv.org/pdf/2601.20782.pdf)  
**作者**：Massimo Solinas, Agnes Valenti, Nawaf Bou-Rabee, Roeland Wiersema  

**一句话要点**：提出混合精度算术框架，以提升基于神经网络的变分蒙特卡洛方法在量子多体系统模拟中的可扩展性与能效。

**关键词**：混合精度计算, 变分蒙特卡洛, 量子多体系统, 神经网络, 误差分析, 能效优化

## 3 点简述
- 核心问题：传统双精度算术在量子多体系统模拟中计算成本高，限制了硬件加速器的性能优势。
- 方法要点：推导混合精度在Metropolis-Hastings MCMC中的误差分析框架，并应用于变分蒙特卡洛方法。
- 实验或效果：实证表明量子态采样可在半精度下执行而不损失精度，实现更高效模拟。

## 摘要（原文）

> Scientific computing has long relied on double precision (64-bit floating point) arithmetic to guarantee accuracy in simulations of real-world phenomena. However, the growing availability of hardware accelerators such as Graphics Processing Units (GPUs) has made low-precision formats attractive due to their superior performance, reduced memory footprint, and improved energy efficiency. In this work, we investigate the role of mixed-precision arithmetic in neural-network based Variational Monte Carlo (VMC), a widely used method for solving computationally otherwise intractable quantum many-body systems. We first derive general analytical bounds on the error introduced by reduced precision on Metropolis-Hastings MCMC, and then empirically validate these bounds on the use-case of VMC. We demonstrate that significant portions of the algorithm, in particular, sampling the quantum state, can be executed in half precision without loss of accuracy. More broadly, this work provides a theoretical framework to assess the applicability of mixed-precision arithmetic in machine-learning approaches that rely on MCMC sampling. In the context of VMC, we additionally demonstrate the practical effectiveness of mixed-precision strategies, enabling more scalable and energy-efficient simulations of quantum many-body systems.


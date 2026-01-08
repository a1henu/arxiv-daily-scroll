---
layout: default
title: Robust Physics Discovery from Highly Corrupted Data: A PINN Framework Applied to the Nonlinear Schrödinger Equation
---

# Robust Physics Discovery from Highly Corrupted Data: A PINN Framework Applied to the Nonlinear Schrödinger Equation
**arXiv**：[2601.04176v1](https://arxiv.org/abs/2601.04176) · [PDF](https://arxiv.org/pdf/2601.04176.pdf)  
**作者**：Pietro de Oliveira Esteves  

**一句话要点**：提出基于PINN的框架，从高噪声数据中稳健发现非线性薛定谔方程物理参数

**关键词**：物理信息神经网络, 非线性薛定谔方程, 参数反演, 噪声鲁棒性, 自动微分, 稀疏数据

## 3 点简述
- 核心问题：从严重噪声数据中恢复非线性薛定谔方程参数，传统方法因噪声放大而失效
- 方法要点：结合物理信息神经网络与自动微分，利用物理正则化过滤噪声
- 实验或效果：在20%高斯噪声下，使用500稀疏点实现β系数误差小于0.2%，泛化能力强

## 摘要（原文）

> We demonstrate a deep learning framework capable of recovering physical parameters from the Nonlinear Schrodinger Equation (NLSE) under severe noise conditions. By integrating Physics-Informed Neural Networks (PINNs) with automatic differentiation, we achieve reconstruction of the nonlinear coefficient beta with less than 0.2 percent relative error using only 500 sparse, randomly sampled data points corrupted by 20 percent additive Gaussian noise, a regime where traditional finite difference methods typically fail due to noise amplification in numerical derivatives. We validate the method's generalization capabilities across different physical regimes (beta between 0.5 and 2.0) and varying data availability (between 100 and 1000 training points), demonstrating consistent sub-1 percent accuracy. Statistical analysis over multiple independent runs confirms robustness (standard deviation less than 0.15 percent for beta equals 1.0). The complete pipeline executes in approximately 80 minutes on modest cloud GPU resources (NVIDIA Tesla T4), making the approach accessible for widespread adoption. Our results indicate that physics-based regularization acts as an effective filter against high measurement uncertainty, positioning PINNs as a viable alternative to traditional optimization methods for inverse problems in spatiotemporal dynamics where experimental data is scarce and noisy. All code is made publicly available to facilitate reproducibility.


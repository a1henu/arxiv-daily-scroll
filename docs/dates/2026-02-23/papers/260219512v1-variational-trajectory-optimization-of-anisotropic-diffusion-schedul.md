---
layout: default
title: Variational Trajectory Optimization of Anisotropic Diffusion Schedules
---

# Variational Trajectory Optimization of Anisotropic Diffusion Schedules
**arXiv**：[2602.19512v1](https://arxiv.org/abs/2602.19512) · [PDF](https://arxiv.org/pdf/2602.19512.pdf)  
**作者**：Pengxi Liu, Zeyu Michael Li, Xiang Cheng  

**一句话要点**：提出变分轨迹优化框架以改进各向异性扩散模型的噪声调度

**关键词**：扩散模型, 变分优化, 噪声调度, 各向异性扩散, 轨迹优化, 反向ODE求解器

## 3 点简述
- 核心问题：扩散模型中噪声调度通常为各向同性，限制了模型在子空间中的噪声分配灵活性。
- 方法要点：引入矩阵值路径参数化噪声调度，通过轨迹级目标联合训练分数网络并优化调度参数。
- 实验或效果：在CIFAR-10等数据集上，相比基线EDM模型，在所有NFE机制下均实现性能提升。

## 摘要（原文）

> We introduce a variational framework for diffusion models with anisotropic noise schedules parameterized by a matrix-valued path $M_t(θ)$ that allocates noise across subspaces. Central to our framework is a trajectory-level objective that jointly trains the score network and learns $M_t(θ)$, which encompasses general parameterization classes of matrix-valued noise schedules. We further derive an estimator for the derivative with respect to $θ$ of the score that enables efficient optimization of the $M_t(θ)$ schedule. For inference, we develop an efficiently-implementable reverse-ODE solver that is an anisotropic generalization of the second-order Heun discretization algorithm. Across CIFAR-10, AFHQv2, FFHQ, and ImageNet-64, our method consistently improves upon the baseline EDM model in all NFE regimes. Code is available at https://github.com/lizeyu090312/anisotropic-diffusion-paper.


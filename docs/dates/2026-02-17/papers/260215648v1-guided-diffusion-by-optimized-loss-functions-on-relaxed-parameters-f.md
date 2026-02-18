---
layout: default
title: Guided Diffusion by Optimized Loss Functions on Relaxed Parameters for Inverse Material Design
---

# Guided Diffusion by Optimized Loss Functions on Relaxed Parameters for Inverse Material Design
**arXiv**：[2602.15648v1](https://arxiv.org/abs/2602.15648) · [PDF](https://arxiv.org/pdf/2602.15648.pdf)  
**作者**：Jens U. Kreber, Christian Weißenfels, Joerg Stueckler  

**一句话要点**：提出基于扩散模型的逆材料设计方法，通过松弛参数空间和可微模拟实现梯度引导采样。

**关键词**：逆材料设计, 扩散模型, 可微模拟, 梯度引导采样, 复合材料优化, 多模态解空间

## 3 点简述
- 逆设计问题中，离散参数或约束阻碍梯度优化，需处理多模态解空间。
- 方法松弛设计空间为连续网格，训练扩散模型作为先验，利用可微模拟进行梯度引导采样。
- 在复合材料设计中，以线性FEM为前向模型，生成满足目标体积模量的多样设计，误差在1%以内。

## 摘要（原文）

> Inverse design problems are common in engineering and materials science. The forward direction, i.e., computing output quantities from design parameters, typically requires running a numerical simulation, such as a FEM, as an intermediate step, which is an optimization problem by itself. In many scenarios, several design parameters can lead to the same or similar output values. For such cases, multi-modal probabilistic approaches are advantageous to obtain diverse solutions. A major difficulty in inverse design stems from the structure of the design space, since discrete parameters or further constraints disallow the direct use of gradient-based optimization. To tackle this problem, we propose a novel inverse design method based on diffusion models. Our approach relaxes the original design space into a continuous grid representation, where gradients can be computed by implicit differentiation in the forward simulation. A diffusion model is trained on this relaxed parameter space in order to serve as a prior for plausible relaxed designs. Parameters are sampled by guided diffusion using gradients that are propagated from an objective function specified at inference time through the differentiable simulation. A design sample is obtained by backprojection into the original parameter space. We develop our approach for a composite material design problem where the forward process is modeled as a linear FEM problem. We evaluate the performance of our approach in finding designs that match a specified bulk modulus. We demonstrate that our method can propose diverse designs within 1% relative error margin from medium to high target bulk moduli in 2D and 3D settings. We also demonstrate that the material density of generated samples can be minimized simultaneously by using a multi-objective loss function.


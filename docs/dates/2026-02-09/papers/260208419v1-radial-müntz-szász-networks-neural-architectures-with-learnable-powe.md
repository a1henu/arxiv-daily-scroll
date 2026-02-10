---
layout: default
title: Radial Müntz-Szász Networks: Neural Architectures with Learnable Power Bases for Multidimensional Singularities
---

# Radial Müntz-Szász Networks: Neural Architectures with Learnable Power Bases for Multidimensional Singularities
**arXiv**：[2602.08419v1](https://arxiv.org/abs/2602.08419) · [PDF](https://arxiv.org/pdf/2602.08419.pdf)  
**作者**：Gnankan Landry Regis N'guessan, Bum Jun Kim  

**一句话要点**：提出径向Müntz-Szász网络以解决多维奇异性建模问题

**关键词**：径向奇异性建模, 可学习幂基网络, 物理信息学习, 多维函数逼近, 神经网络架构

## 3 点简述
- 径向奇异性场如1/r和log r难以用坐标可分离神经网络建模
- 引入可学习径向幂基r^μ和稳定对数原语，支持精确梯度计算
- 在10个基准测试中，RMN以少量参数实现比MLP和SIREN更低的RMSE

## 摘要（原文）

> Radial singular fields, such as $1/r$, $\log r$, and crack-tip profiles, are difficult to model for coordinate-separable neural architectures. We show that any $C^2$ function that is both radial and additively separable must be quadratic, establishing a fundamental obstruction for coordinate-wise power-law models. Motivated by this result, we introduce Radial Müntz-Szász Networks (RMN), which represent fields as linear combinations of learnable radial powers $r^μ$, including negative exponents, together with a limit-stable log-primitive for exact $\log r$ behavior. RMN admits closed-form spatial gradients and Laplacians, enabling physics-informed learning on punctured domains. Across ten 2D and 3D benchmarks, RMN achieves 1.5$\times$--51$\times$ lower RMSE than MLPs and 10$\times$--100$\times$ lower RMSE than SIREN while using 27 parameters, compared with 33,537 for MLPs and 8,577 for SIREN. We extend RMN to angular dependence (RMN-Angular) and to multiple sources with learnable centers (RMN-MC); when optimization converges, source-center recovery errors fall below $10^{-4}$. We also report controlled failures on smooth, strongly non-radial targets to delineate RMN's operating regime.


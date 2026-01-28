---
layout: default
title: Accelerated Multiple Wasserstein Gradient Flows for Multi-objective Distributional Optimization
---

# Accelerated Multiple Wasserstein Gradient Flows for Multi-objective Distributional Optimization
**arXiv**：[2601.19220v1](https://arxiv.org/abs/2601.19220) · [PDF](https://arxiv.org/pdf/2601.19220.pdf)  
**作者**：Dai Hai Nguyen, Duc Dung Nguyen, Atsuyoshi Nakamura, Hiroshi Mamitsuka  

**一句话要点**：提出加速多目标Wasserstein梯度流算法A-MWGraD，以提升多目标分布优化的收敛速度与采样效率。

**关键词**：Wasserstein空间, 多目标优化, 梯度流加速, 概率分布优化, 测地凸性, 核方法

## 3 点简述
- 研究Wasserstein空间中概率分布的多目标优化问题，扩展了MWGraD算法。
- 引入Nesterov加速技术，理论证明在测地凸目标下收敛率提升至O(1/t²)。
- 通过核基离散化与数值实验验证A-MWGraD在收敛速度和采样效率上优于MWGraD。

## 摘要（原文）

> We study multi-objective optimization over probability distributions in Wasserstein space. Recently, Nguyen et al. (2025) introduced Multiple Wasserstein Gradient Descent (MWGraD) algorithm, which exploits the geometric structure of Wasserstein space to jointly optimize multiple objectives. Building on this approach, we propose an accelerated variant, A-MWGraD, inspired by Nesterov's acceleration. We analyze the continuous-time dynamics and establish convergence to weakly Pareto optimal points in probability space. Our theoretical results show that A-MWGraD achieves a convergence rate of O(1/t^2) for geodesically convex objectives and O(e^{-\sqrtβt}) for $β$-strongly geodesically convex objectives, improving upon the O(1/t) rate of MWGraD in the geodesically convex setting. We further introduce a practical kernel-based discretization for A-MWGraD and demonstrate through numerical experiments that it consistently outperforms MWGraD in convergence speed and sampling efficiency on multi-target sampling tasks.


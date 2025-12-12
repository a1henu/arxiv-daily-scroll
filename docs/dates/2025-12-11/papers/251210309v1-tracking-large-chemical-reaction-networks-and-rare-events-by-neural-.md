---
layout: default
title: Tracking large chemical reaction networks and rare events by neural networks
---

# Tracking large chemical reaction networks and rare events by neural networks
**arXiv**：[2512.10309v1](https://arxiv.org/abs/2512.10309) · [PDF](https://arxiv.org/pdf/2512.10309.pdf)  
**作者**：Jiayu Weng, Xinyi Zhu, Jing Liu, Linyuan Lü, Pan Zhang, Ying Tang  

**一句话要点**：提出基于神经网络的优化与增强采样方法，以高效建模大型化学反应网络和稀有事件

**关键词**：化学反应网络, 神经网络优化, 稀有事件采样, 化学主方程求解, 反应-扩散系统, 计算加速

## 3 点简述
- 核心问题：化学反应网络的状态空间随系统规模指数增长，传统方法求解化学主方程计算成本高，尤其在处理高维系统和稀有事件时效率受限。
- 方法要点：利用自然梯度下降和时间依赖变分原理加速优化，实现5至22倍速度提升；结合增强采样策略捕获稀有事件，提高计算效率。
- 实验或效果：在MAPK级联网络等挑战性反应网络中，相比先前神经网络方法，计算成本降低且精度更高；扩展至二维反应-扩散系统，超越现有张量网络方法的一维处理能力。

## 摘要（原文）

> Chemical reaction networks are widely used to model stochastic dynamics in chemical kinetics, systems biology and epidemiology. Solving the chemical master equation that governs these systems poses a significant challenge due to the large state space exponentially growing with system sizes. The development of autoregressive neural networks offers a flexible framework for this problem; however, its efficiency is limited especially for high-dimensional systems and in scenarios with rare events. Here, we push the frontier of neural-network approach by exploiting faster optimizations such as natural gradient descent and time-dependent variational principle, achieving a 5- to 22-fold speedup, and by leveraging enhanced-sampling strategies to capture rare events. We demonstrate reduced computational cost and higher accuracy over the previous neural-network method in challenging reaction networks, including the mitogen-activated protein kinase (MAPK) cascade network, the hitherto largest biological network handled by the previous approaches of solving the chemical master equation. We further apply the approach to spatially extended reaction-diffusion systems, the Schlögl model with rare events, on two-dimensional lattices, beyond the recent tensor-network approach that handles one-dimensional lattices. The present approach thus enables efficient modeling of chemical reaction networks in general.


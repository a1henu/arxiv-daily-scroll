---
layout: default
title: BONNI: Gradient-Informed Bayesian and Interior Point Optimization for Efficient Inverse Design in Nanophotonics
---

# BONNI: Gradient-Informed Bayesian and Interior Point Optimization for Efficient Inverse Design in Nanophotonics
**arXiv**：[2602.18148v1](https://arxiv.org/abs/2602.18148) · [PDF](https://arxiv.org/pdf/2602.18148.pdf)  
**作者**：Yannik Mahlau, Yannick Augenstein, Tyler W. Hughes, Marius Lindauer, Bodo Rosenhahn  

**一句话要点**：提出BONNI方法，结合贝叶斯优化与内点法，用于纳米光子学高效逆设计

**关键词**：纳米光子学, 逆设计, 贝叶斯优化, 内点法, 梯度信息, 神经网络集成

## 3 点简述
- 核心问题：纳米光子学逆设计中，全局优化收敛慢，局部优化易陷局部最优
- 方法要点：通过神经网络集成代理模型，融入梯度信息指导采样，提升优化效率
- 实验或效果：在分布式布拉格反射器等设计中，相比现有方法显著降低误差

## 摘要（原文）

> Inverse design, particularly geometric shape optimization, provides a systematic approach for developing high-performance nanophotonic devices. While numerous optimization algorithms exist, previous global approaches exhibit slow convergence and conversely local search strategies frequently become trapped in local optima. To address the limitations inherent to both local and global approaches, we introduce BONNI: Bayesian optimization through neural network ensemble surrogates with interior point optimization. It augments global optimization with an efficient incorporation of gradient information to determine optimal sampling points. This capability allows BONNI to circumvent the local optima found in many nanophotonic applications, while capitalizing on the efficiency of gradient-based optimization. We demonstrate BONNI's capabilities in the design of a distributed Bragg reflector as well as a dual-layer grating coupler through an exhaustive comparison against other optimization algorithms commonly used in literature. Using BONNI, we were able to design a 10-layer distributed Bragg reflector with only 4.5% mean spectral error, compared to the previously reported results of 7.8% error with 16 layers. Further designs of a broadband waveguide taper and photonic crystal waveguide transition validate the capabilities of BONNI.


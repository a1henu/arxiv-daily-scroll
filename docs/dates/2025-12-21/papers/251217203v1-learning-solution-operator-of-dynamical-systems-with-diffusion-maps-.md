---
layout: default
title: Learning solution operator of dynamical systems with diffusion maps kernel ridge regression
---

# Learning solution operator of dynamical systems with diffusion maps kernel ridge regression
**arXiv**：[2512.17203v1](https://arxiv.org/abs/2512.17203) · [PDF](https://arxiv.org/pdf/2512.17203.pdf)  
**作者**：Jiwoo Song, Daning Huang, John Harlim  

**一句话要点**：提出扩散映射核岭回归方法，用于复杂动力系统的长期预测，提升几何适应性与数据效率。

**关键词**：动力系统预测, 扩散映射核, 核岭回归, 几何适应, 数据驱动建模, 长期预测

## 3 点简述
- 核心问题：复杂非线性动力系统的长期预测困难，几何结构未知时模型性能下降。
- 方法要点：结合扩散映射核与核岭回归，无需显式流形重建，自适应系统内在几何。
- 实验或效果：在多种系统中优于随机特征、神经网络和算子学习方法，准确性和数据效率更高。

## 摘要（原文）

> Many scientific and engineering systems exhibit complex nonlinear dynamics that are difficult to predict accurately over long time horizons. Although data-driven models have shown promise, their performance often deteriorates when the geometric structures governing long-term behavior are unknown or poorly represented. We demonstrate that a simple kernel ridge regression (KRR) framework, when combined with a dynamics-aware validation strategy, provides a strong baseline for long-term prediction of complex dynamical systems. By employing a data-driven kernel derived from diffusion maps, the proposed Diffusion Maps Kernel Ridge Regression (DM-KRR) method implicitly adapts to the intrinsic geometry of the system's invariant set, without requiring explicit manifold reconstruction or attractor modeling, procedures that often limit predictive performance. Across a broad range of systems, including smooth manifolds, chaotic attractors, and high-dimensional spatiotemporal flows, DM-KRR consistently outperforms state-of-the-art random feature, neural-network and operator-learning methods in both accuracy and data efficiency. These findings underscore that long-term predictive skill depends not only on model expressiveness, but critically on respecting the geometric constraints encoded in the data through dynamically consistent model selection. Together, simplicity, geometry awareness, and strong empirical performance point to a promising path for reliable and efficient learning of complex dynamical systems.


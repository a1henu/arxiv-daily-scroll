---
layout: default
title: Well-Posed KL-Regularized Control via Wasserstein and Kalman-Wasserstein KL Divergences
---

# Well-Posed KL-Regularized Control via Wasserstein and Kalman-Wasserstein KL Divergences
**arXiv**：[2602.02250v1](https://arxiv.org/abs/2602.02250) · [PDF](https://arxiv.org/pdf/2602.02250.pdf)  
**作者**：Viktor Stein, Adwait Datar, Nihat Ay  

**一句话要点**：提出基于Wasserstein和Kalman-Wasserstein KL散度的正则化控制方法，以解决KL正则化在支持不匹配和低噪声极限下的问题。

**关键词**：KL正则化, Wasserstein散度, 最优控制, 信息几何, 强化学习, 高斯过程

## 3 点简述
- 核心问题：KL正则化在强化学习中因支持不匹配和低噪声极限而失效或退化。
- 方法要点：通过信息几何框架，用传输几何替换Fisher-Rao几何，定义新散度并推导闭式解。
- 实验或效果：在线性时不变系统和高斯噪声下，新方法消除奇异性，在双积分器和倒立摆示例中表现更优。

## 摘要（原文）

> Kullback-Leibler divergence (KL) regularization is widely used in reinforcement learning, but it becomes infinite under support mismatch and can degenerate in low-noise limits. Utilizing a unified information-geometric framework, we introduce (Kalman)-Wasserstein-based KL analogues by replacing the Fisher-Rao geometry in the dynamical formulation of the KL with transport-based geometries, and we derive closed-form values for common distribution families. These divergences remain finite under support mismatch and yield a geometric interpretation of regularization heuristics used in Kalman ensemble methods. We demonstrate the utility of these divergences in KL-regularized optimal control. In the fully tractable setting of linear time-invariant systems with Gaussian process noise, the classical KL reduces to a quadratic control penalty that becomes singular as process noise vanishes. Our variants remove this singularity, yielding well-posed problems. On a double integrator and a cart-pole example, the resulting controls outperform KL-based regularization.


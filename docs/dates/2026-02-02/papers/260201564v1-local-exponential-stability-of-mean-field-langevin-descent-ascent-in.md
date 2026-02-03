---
layout: default
title: Local Exponential Stability of Mean-Field Langevin Descent-Ascent in Wasserstein Space
---

# Local Exponential Stability of Mean-Field Langevin Descent-Ascent in Wasserstein Space
**arXiv**：[2602.01564v1](https://arxiv.org/abs/2602.01564) · [PDF](https://arxiv.org/pdf/2602.01564.pdf)  
**作者**：Geuntaek Seo, Minseop Shin, Pierre Monmarché, Beomjun Choi  

**一句话要点**：证明平均场Langevin下降-上升在Wasserstein空间中局部指数稳定，解决非凸非凹博弈的局部收敛问题

**关键词**：平均场博弈, Langevin动力学, Wasserstein空间, 局部稳定性, 熵正则化, 非凸非凹优化

## 3 点简述
- 研究平均场Langevin下降-上升在概率测度空间中的局部稳定性，针对熵正则化二人零和博弈
- 通过谱分析建立线性化算子的强制性估计，揭示局部位移凸凹结构，驱动指数收敛
- 证明在Wasserstein度量下，初始化足够接近时，动力学以指数速率趋向唯一混合纳什均衡

## 摘要（原文）

> We study the mean-field Langevin descent-ascent (MFL-DA), a coupled optimization dynamics on the space of probability measures for entropically regularized two-player zero-sum games. Although the associated mean-field objective admits a unique mixed Nash equilibrium, the long-time behavior of the original MFL-DA for general nonconvex-nonconcave payoffs has remained largely open. Answering an open question posed by Wang and Chizat (COLT 2024), we provide a partial resolution by proving that this equilibrium is locally exponentially stable: if the initialization is sufficiently close in Wasserstein metric, the dynamics trends to the equilibrium at an exponential rate. The key to our analysis is to establish a coercivity estimate for the entropy near equilibrium via spectral analysis of the linearized operator. We show that this coercivity effectively reveals a local displacement convex-concave structure, thereby driving contraction. This result settles the local stability and quantitative rate questions of Wang and Chizat, leaving global convergence as a remaining open challenge.


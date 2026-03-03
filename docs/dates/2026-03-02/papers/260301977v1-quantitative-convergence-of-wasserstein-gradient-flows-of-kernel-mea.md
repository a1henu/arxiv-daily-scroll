---
layout: default
title: Quantitative Convergence of Wasserstein Gradient Flows of Kernel Mean Discrepancies
---

# Quantitative Convergence of Wasserstein Gradient Flows of Kernel Mean Discrepancies
**arXiv**：[2603.01977v1](https://arxiv.org/abs/2603.01977) · [PDF](https://arxiv.org/pdf/2603.01977.pdf)  
**作者**：Lénaïc Chizat, Maria Colombo, Roberto Colombo, Xavier Fernández-Real  

**一句话要点**：量化分析核均值差异Wasserstein梯度流的收敛性，应用于无限宽度神经网络训练和平均场粒子系统。

**关键词**：Wasserstein梯度流, 核均值差异, 神经网络训练, 平均场极限, Sobolev空间, 收敛分析

## 3 点简述
- 研究核均值差异（KMD）Wasserstein梯度流的定量收敛问题，覆盖无限宽度浅层神经网络和平均场粒子系统。
- 基于Sobolev距离模型，证明s=1时全局指数收敛，s>1时局部多项式收敛，并推导神经网络训练的显式收敛率。
- 通过一维数值实验验证理论分析，使用PDE和粒子方法。

## 摘要（原文）

> We study the quantitative convergence of Wasserstein gradient flows of Kernel Mean Discrepancy (KMD) (also known as Maximum Mean Discrepancy (MMD)) functionals. Our setting covers in particular the training dynamics of shallow neural networks in the infinite-width and continuous time limit, as well as interacting particle systems with pairwise Riesz kernel interaction in the mean-field and overdamped limit. Our main analysis concerns the model case of KMD functionals given by the squared Sobolev distance $ \mathscr{E}^ν_{s}(μ)= \frac{1}{2}\lVert μ-ν\rVert_{\dot H^{-s}}^{2}$ for any $s\geq 1 $ and $ν$ a fixed probability measure on the $d$-dimensional torus. First, inspired by Yudovich theory for the $2d$-Euler equation, we establish existence and uniqueness in natural weak regularity classes. Next, we show that for $s=1$ the flow converges globally at an exponential rate under minimal assumptions, while for $s>1$ we prove local convergence at polynomial rates that depend explicitly on $s$ and on the Sobolev regularity of $μ$ and $ν$. These rates hold both at the energy level and in higher regularity classes and are tight for $ν$ uniform. We then consider the gradient flow of the population loss for shallow neural networks with ReLU activation, which can be cast as a Wasserstein--Fisher--Rao gradient flow on the space of nonnegative measures on the sphere $\mathbb{S}^d$. Exploiting a correspondence with the Sobolev energy case with $s=(d+3)/2$, we derive an explicit polynomial local convergence rate for this dynamics. Except for the special case $s=1$, even non-quantitative convergence was previously open in all these settings. We also include numerical experiments in dimension $d=1$ using both PDE and particle methods which illustrate our analysis.


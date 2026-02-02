---
layout: default
title: DC-LA: Difference-of-Convex Langevin Algorithm
---

# DC-LA: Difference-of-Convex Langevin Algorithm
**arXiv**：[2601.22932v1](https://arxiv.org/abs/2601.22932) · [PDF](https://arxiv.org/pdf/2601.22932.pdf)  
**作者**：Hoang Phuc Hau Luu, Zhongjian Wang  

**一句话要点**：提出DC-LA算法以解决非光滑DC正则化项的采样问题

**关键词**：采样算法, DC规划, Langevin算法, 非光滑优化, Wasserstein距离, 不确定性量化

## 3 点简述
- 研究目标分布为π∝exp(-f-r)的采样问题，其中r为非光滑DC函数
- 利用DC结构平滑正则化项，提出DC-LA算法并建立收敛性理论
- 数值实验验证DC-LA在合成和真实CT应用中提供准确分布和不确定性量化

## 摘要（原文）

> We study a sampling problem whose target distribution is $π\propto \exp(-f-r)$ where the data fidelity term $f$ is Lipschitz smooth while the regularizer term $r=r_1-r_2$ is a non-smooth difference-of-convex (DC) function, i.e., $r_1,r_2$ are convex. By leveraging the DC structure of $r$, we can smooth out $r$ by applying Moreau envelopes to $r_1$ and $r_2$ separately. In line of DC programming, we then redistribute the concave part of the regularizer to the data fidelity and study its corresponding proximal Langevin algorithm (termed DC-LA). We establish convergence of DC-LA to the target distribution $π$, up to discretization and smoothing errors, in the $q$-Wasserstein distance for all $q \in \mathbb{N}^*$, under the assumption that $V$ is distant dissipative. Our results improve previous work on non-log-concave sampling in terms of a more general framework and assumptions. Numerical experiments show that DC-LA produces accurate distributions in synthetic settings and reliably provides uncertainty quantification in a real-world Computed Tomography application.


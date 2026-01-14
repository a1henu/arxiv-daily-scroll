---
layout: default
title: LDLT L-Lipschitz Network Weight Parameterization Initialization
---

# LDLT L-Lipschitz Network Weight Parameterization Initialization
**arXiv**：[2601.08253v1](https://arxiv.org/abs/2601.08253) · [PDF](https://arxiv.org/pdf/2601.08253.pdf)  
**作者**：Marius F. R. Juston, Ramavarapu S. Sreenivas, Dustin Nottage, Ahmet Soylemezoglu  

**一句话要点**：分析LDLT参数化L-Lipschitz网络初始化动态，推导输出方差并提出初始化超参数选择建议。

**关键词**：L-Lipschitz网络, 初始化动态, Wishart分布, 输出方差分析, 深度学习理论, 参数化方法

## 3 点简述
- 核心问题：L-Lipschitz网络初始化时输出方差快速衰减导致信息损失。
- 方法要点：基于Wishart分布和组合展开推导输出方差闭式解，提供截断矩近似。
- 实验或效果：理论估计与蒙特卡洛实验一致，新参数化提升方差但He初始化在真实数据上表现更优。

## 摘要（原文）

> We analyze initialization dynamics for LDLT-based $\mathcal{L}$-Lipschitz layers by deriving the exact marginal output variance when the underlying parameter matrix $W_0\in \mathbb{R}^{m\times n}$ is initialized with IID Gaussian entries $\mathcal{N}(0,σ^2)$. The Wishart distribution, $S=W_0W_0^\top\sim\mathcal{W}_m(n,σ^2 \boldsymbol{I}_m)$, used for computing the output marginal variance is derived in closed form using expectations of zonal polynomials via James' theorem and a Laplace-integral expansion of $(α\boldsymbol{I}_m+S)^{-1}$. We develop an Isserlis/Wick-based combinatorial expansion for $\operatorname{\mathbb{E}}\left[\operatorname{tr}(S^k)\right]$ and provide explicit truncated moments up to $k=10$, which yield accurate series approximations for small-to-moderate $σ^2$. Monte Carlo experiments confirm the theoretical estimates. Furthermore, empirical analysis was performed to quantify that, using current He or Kaiming initialization with scaling $1/\sqrt{n}$, the output variance is $0.41$, whereas the new parameterization with $10/ \sqrt{n}$ for $α=1$ results in an output variance of $0.9$. The findings clarify why deep $\mathcal{L}$-Lipschitz networks suffer rapid information loss at initialization and offer practical prescriptions for choosing initialization hyperparameters to mitigate this effect. However, using the Higgs boson classification dataset, a hyperparameter sweep over optimizers, initialization scale, and depth was conducted to validate the results on real-world data, showing that although the derivation ensures variance preservation, empirical results indicate He initialization still performs better.


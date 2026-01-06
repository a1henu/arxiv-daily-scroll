---
layout: default
title: Prior Diffusiveness and Regret in the Linear-Gaussian Bandit
---

# Prior Diffusiveness and Regret in the Linear-Gaussian Bandit
**arXiv**：[2601.02022v1](https://arxiv.org/abs/2601.02022) · [PDF](https://arxiv.org/pdf/2601.02022.pdf)  
**作者**：Yifan Zhu, John C. Duchi, Benjamin Van Roy  

**一句话要点**：在线性高斯赌博机中，证明Thompson采样贝叶斯遗憾的加性先验依赖项与极小极大遗憾解耦。

**关键词**：线性高斯赌博机, Thompson采样, 贝叶斯遗憾, 先验分布, 椭圆势引理, 遗憾界分析

## 3 点简述
- 研究线性高斯赌博机中Thompson采样的贝叶斯遗憾界，关注先验分布对遗憾的影响。
- 提出新的椭圆势引理，证明先验依赖项与长期遗憾项可加性分离，而非现有界的乘法依赖。
- 提供下界表明先验依赖项不可避免，并通过理论分析验证结果，未提及具体实验。

## 摘要（原文）

> We prove that Thompson sampling exhibits $\tilde{O}(σd \sqrt{T} + d r \sqrt{\mathrm{Tr}(Σ_0)})$ Bayesian regret in the linear-Gaussian bandit with a $\mathcal{N}(μ_0, Σ_0)$ prior distribution on the coefficients, where $d$ is the dimension, $T$ is the time horizon, $r$ is the maximum $\ell_2$ norm of the actions, and $σ^2$ is the noise variance. In contrast to existing regret bounds, this shows that to within logarithmic factors, the prior-dependent ``burn-in'' term $d r \sqrt{\mathrm{Tr}(Σ_0)}$ decouples additively from the minimax (long run) regret $σd \sqrt{T}$. Previous regret bounds exhibit a multiplicative dependence on these terms. We establish these results via a new ``elliptical potential'' lemma, and also provide a lower bound indicating that the burn-in term is unavoidable.


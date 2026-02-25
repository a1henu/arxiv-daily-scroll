---
layout: default
title: Statistical Query Lower Bounds for Smoothed Agnostic Learning
---

# Statistical Query Lower Bounds for Smoothed Agnostic Learning
**arXiv**：[2602.21191v1](https://arxiv.org/abs/2602.21191) · [PDF](https://arxiv.org/pdf/2602.21191.pdf)  
**作者**：Ilias Diakonikolas, Daniel M. Kane  

**一句话要点**：提出统计查询下界证明，表明平滑不可知半空间学习复杂度接近最优。

**关键词**：平滑不可知学习, 统计查询下界, 半空间学习, 高斯扰动, 复杂度分析, 矩匹配

## 3 点简述
- 研究平滑不可知学习复杂度，聚焦高斯扰动下不可知半空间学习任务。
- 通过线性规划对偶构造矩匹配硬分布，推导统计查询下界。
- 下界复杂度为d^{Ω(1/σ^{2}+log(1/ε))}，与已知上界几乎匹配。

## 摘要（原文）

> We study the complexity of smoothed agnostic learning, recently introduced by~\cite{CKKMS24}, in which the learner competes with the best classifier in a target class under slight Gaussian perturbations of the inputs. Specifically, we focus on the prototypical task of agnostically learning halfspaces under subgaussian distributions in the smoothed model. The best known upper bound for this problem relies on $L_1$-polynomial regression and has complexity $d^{\tilde{O}(1/σ^2) \log(1/ε)}$, where $σ$ is the smoothing parameter and $ε$ is the excess error. Our main result is a Statistical Query (SQ) lower bound providing formal evidence that this upper bound is close to best possible. In more detail, we show that (even for Gaussian marginals) any SQ algorithm for smoothed agnostic learning of halfspaces requires complexity $d^{Ω(1/σ^{2}+\log(1/ε))}$. This is the first non-trivial lower bound on the complexity of this task and nearly matches the known upper bound. Roughly speaking, we show that applying $L_1$-polynomial regression to a smoothed version of the function is essentially best possible. Our techniques involve finding a moment-matching hard distribution by way of linear programming duality. This dual program corresponds exactly to finding a low-degree approximating polynomial to the smoothed version of the target function (which turns out to be the same condition required for the $L_1$-polynomial regression to work). Our explicit SQ lower bound then comes from proving lower bounds on this approximation degree for the class of halfspaces.


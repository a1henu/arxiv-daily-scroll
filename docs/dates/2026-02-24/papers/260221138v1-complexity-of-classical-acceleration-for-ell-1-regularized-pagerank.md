---
layout: default
title: Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank
---

# Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank
**arXiv**：[2602.21138v1](https://arxiv.org/abs/2602.21138) · [PDF](https://arxiv.org/pdf/2602.21138.pdf)  
**作者**：Kimon Fountoulakis, David Martínez-Rubio  

**一句话要点**：分析FISTA在ℓ1正则化PageRank中的加速复杂度，揭示边界集对计算成本的影响。

**关键词**：ℓ1正则化PageRank, 加速近端梯度法, 计算复杂度, 图结构分析, 度加权工作

## 3 点简述
- 研究FISTA加速方法在ℓ1正则化PageRank中的计算复杂度，关注梯度评估的度加权工作。
- 通过过正则化目标和可检查约束条件，证明虚假激活被限制在边界集内，推导出复杂度界限。
- 在合成和真实图上实验，展示度加权工作模型下的加速和减速机制。

## 摘要（原文）

> We study the degree-weighted work required to compute $\ell_1$-regularized PageRank using the standard one-gradient-per-iteration accelerated proximal-gradient method (FISTA). For non-accelerated local methods, the best known worst-case work scales as $\widetilde{O} ((αρ)^{-1})$, where $α$ is the teleportation parameter and $ρ$ is the $\ell_1$-regularization parameter. A natural question is whether FISTA can improve the dependence on $α$ from $1/α$ to $1/\sqrtα$ while preserving the $1/ρ$ locality scaling. The challenge is that acceleration can break locality by transiently activating nodes that are zero at optimality, thereby increasing the cost of gradient evaluations. We analyze FISTA on a slightly over-regularized objective and show that, under a checkable confinement condition, all spurious activations remain inside a boundary set $\mathcal{B}$. This yields a bound consisting of an accelerated $(ρ\sqrtα)^{-1}\log(α/\varepsilon)$ term plus a boundary overhead $\sqrt{vol(\mathcal{B})}/(ρα^{3/2})$. We provide graph-structural conditions that imply such confinement. Experiments on synthetic and real graphs show the resulting speedup and slowdown regimes under the degree-weighted work model.


---
layout: default
title: Asymptotic Smoothing of the Lipschitz Loss Landscape in Overparameterized One-Hidden-Layer ReLU Networks
---

# Asymptotic Smoothing of the Lipschitz Loss Landscape in Overparameterized One-Hidden-Layer ReLU Networks
**arXiv**：[2602.17596v1](https://arxiv.org/abs/2602.17596) · [PDF](https://arxiv.org/pdf/2602.17596.pdf)  
**作者**：Saveliy Baturin  

**一句话要点**：证明过参数化单隐藏层ReLU网络的损失景观在宽度增长时渐近平滑，连接性增强。

**关键词**：过参数化神经网络, 损失景观平滑, ReLU网络拓扑, 能量间隙分析, 动态字符串采样

## 3 点简述
- 研究过参数化单隐藏层ReLU网络的损失景观拓扑结构，关注局部与全局最小值间的能量间隙。
- 理论证明：对于凸L-Lipschitz损失，ℓ1正则化第二层下，任意同损失水平模型可通过连续路径连接，能量间隙随宽度增长渐近消失。
- 实证验证：在合成Moons和威斯康星乳腺癌数据集上，使用动态字符串采样测量能量间隙，发现更宽网络间隙更小，排列检验p=0。

## 摘要（原文）

> We study the topology of the loss landscape of one-hidden-layer ReLU networks under overparameterization. On the theory side, we (i) prove that for convex $L$-Lipschitz losses with an $\ell_1$-regularized second layer, every pair of models at the same loss level can be connected by a continuous path within an arbitrarily small loss increase $ε$ (extending a known result for the quadratic loss); (ii) obtain an asymptotic upper bound on the energy gap $ε$ between local and global minima that vanishes as the width $m$ grows, implying that the landscape flattens and sublevel sets become connected in the limit. Empirically, on a synthetic Moons dataset and on the Wisconsin Breast Cancer dataset, we measure pairwise energy gaps via Dynamic String Sampling (DSS) and find that wider networks exhibit smaller gaps; in particular, a permutation test on the maximum gap yields $p_{perm}=0$, indicating a clear reduction in the barrier height.


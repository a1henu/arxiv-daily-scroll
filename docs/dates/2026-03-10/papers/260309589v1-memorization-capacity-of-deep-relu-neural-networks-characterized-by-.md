---
layout: default
title: Memorization capacity of deep ReLU neural networks characterized by width and depth
---

# Memorization capacity of deep ReLU neural networks characterized by width and depth
**arXiv**：[2603.09589v1](https://arxiv.org/abs/2603.09589) · [PDF](https://arxiv.org/pdf/2603.09589.pdf)  
**作者**：Xin Yang, Yunfei Yang  

**一句话要点**：提出基于宽度与深度的深度ReLU网络记忆容量表征，实现数据点记忆的最优构造。

**关键词**：记忆容量, 深度神经网络, ReLU激活, 宽度深度权衡, 最优构造, 数据点分离

## 3 点简述
- 研究深度ReLU网络记忆任意N个数据点的最小规模问题。
- 构造网络满足W²L²=O(Nlog(δ⁻¹))，证明其记忆能力。
- 证明下界W²L²=Ω(Nlog(δ⁻¹))，表明构造在多项式δ⁻¹下最优。

## 摘要（原文）

> This paper studies the memorization capacity of deep neural networks with ReLU activation. Specifically, we investigate the minimal size of such networks to memorize any $N$ data points in the unit ball with pairwise separation distance $δ$ and discrete labels. Most prior studies characterize the memorization capacity by the number of parameters or neurons. We generalize these results by constructing neural networks, whose width $W$ and depth $L$ satisfy $W^2L^2= \mathcal{O}(N\log(δ^{-1}))$, that can memorize any $N$ data samples. We also prove that any such networks should also satisfy the lower bound $W^2L^2=Ω(N \log(δ^{-1}))$, which implies that our construction is optimal up to logarithmic factors when $δ^{-1}$ is polynomial in $N$. Hence, we explicitly characterize the trade-off between width and depth for the memorization capacity of deep neural networks in this regime.


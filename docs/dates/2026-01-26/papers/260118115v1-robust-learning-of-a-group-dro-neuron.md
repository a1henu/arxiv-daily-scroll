---
layout: default
title: Robust Learning of a Group DRO Neuron
---

# Robust Learning of a Group DRO Neuron
**arXiv**：[2601.18115v1](https://arxiv.org/abs/2601.18115) · [PDF](https://arxiv.org/pdf/2601.18115.pdf)  
**作者**：Guyang Cao, Shuyao Li, Sushrut Karmalkar, Jelena Diakonikolas  

**一句话要点**：提出高效原对偶算法以解决带任意标签噪声和组分布偏移的神经元学习问题

**关键词**：分布鲁棒优化, 神经元学习, 标签噪声, 组分布偏移, 原对偶算法, 非凸优化

## 3 点简述
- 研究在任意标签噪声和组分布偏移下学习单个神经元的问题，目标是最小化最坏情况组加权损失
- 开发计算高效的原对偶算法，输出与最优参数在常数因子内竞争的向量，直接处理损失函数的非凸性
- 算法在LLM预训练基准上显示潜力，提供面对标签损坏和组特定分布偏移的鲁棒学习保证

## 摘要（原文）

> We study the problem of learning a single neuron under standard squared loss in the presence of arbitrary label noise and group-level distributional shifts, for a broad family of covariate distributions. Our goal is to identify a ''best-fit'' neuron parameterized by $\mathbf{w}_*$ that performs well under the most challenging reweighting of the groups. Specifically, we address a Group Distributionally Robust Optimization problem: given sample access to $K$ distinct distributions $\mathcal p_{[1]},\dots,\mathcal p_{[K]}$, we seek to approximate $\mathbf{w}_*$ that minimizes the worst-case objective over convex combinations of group distributions $\boldsymbolλ \in Δ_K$, where the objective is $\sum_{i \in [K]}λ_{[i]}\,\mathbb E_{(\mathbf x,y)\sim\mathcal p_{[i]}}(σ(\mathbf w\cdot\mathbf x)-y)^2 - νd_f(\boldsymbolλ,\frac{1}{K}\mathbf1)$ and $d_f$ is an $f$-divergence that imposes (optional) penalty on deviations from uniform group weights, scaled by a parameter $ν\geq 0$. We develop a computationally efficient primal-dual algorithm that outputs a vector $\widehat{\mathbf w}$ that is constant-factor competitive with $\mathbf{w}_*$ under the worst-case group weighting. Our analytical framework directly confronts the inherent nonconvexity of the loss function, providing robust learning guarantees in the face of arbitrary label corruptions and group-specific distributional shifts. The implementation of the dual extrapolation update motivated by our algorithmic framework shows promise on LLM pre-training benchmarks.


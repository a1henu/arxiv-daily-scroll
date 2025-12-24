---
layout: default
title: Shallow Neural Networks Learn Low-Degree Spherical Polynomials with Learnable Channel Attention
---

# Shallow Neural Networks Learn Low-Degree Spherical Polynomials with Learnable Channel Attention
**arXiv**：[2512.20562v1](https://arxiv.org/abs/2512.20562) · [PDF](https://arxiv.org/pdf/2512.20562.pdf)  
**作者**：Yingzhen Yang  

**一句话要点**：提出带可学习通道注意力的浅层神经网络，以低样本复杂度学习低度球面多项式。

**关键词**：浅层神经网络, 通道注意力, 球面多项式, 样本复杂度, 梯度下降, 非参数回归

## 3 点简述
- 研究学习低度球面多项式的问题，目标函数定义在单位球面上。
- 设计两层神经网络，结合通道注意力，通过两阶段训练实现特征学习。
- 证明训练后的网络达到极小极大最优回归风险率，样本复杂度显著改进。

## 摘要（原文）

> We study the problem of learning a low-degree spherical polynomial of degree $\ell_0 = Θ(1) \ge 1$ defined on the unit sphere in $\RR^d$ by training an over-parameterized two-layer neural network (NN) with channel attention in this paper. Our main result is the significantly improved sample complexity for learning such low-degree polynomials. We show that, for any regression risk $\eps \in (0,1)$, a carefully designed two-layer NN with channel attention and finite width of $m \ge Θ({n^4 \log (2n/δ)}/{d^{2\ell_0}})$ trained by the vanilla gradient descent (GD) requires the lowest sample complexity of $n \asymp Θ(d^{\ell_0}/\eps)$ with probability $1-δ$ for every $δ\in (0,1)$, in contrast with the representative sample complexity $Θ\pth{d^{\ell_0} \max\set{\eps^{-2},\log d}}$, where $n$ is the training daata size. Moreover, such sample complexity is not improvable since the trained network renders a sharp rate of the nonparametric regression risk of the order $Θ(d^{\ell_0}/{n})$ with probability at least $1-δ$. On the other hand, the minimax optimal rate for the regression risk with a kernel of rank $Θ(d^{\ell_0})$ is $Θ(d^{\ell_0}/{n})$, so that the rate of the nonparametric regression risk of the network trained by GD is minimax optimal. The training of the two-layer NN with channel attention consists of two stages. In Stage 1, a provable learnable channel selection algorithm identifies the ground-truth channel number $\ell_0$ from the initial $L \ge \ell_0$ channels in the first-layer activation, with high probability. This learnable selection is achieved by an efficient one-step GD update on both layers, enabling feature learning for low-degree polynomial targets. In Stage 2, the second layer is trained by standard GD using the activation function with the selected channels.


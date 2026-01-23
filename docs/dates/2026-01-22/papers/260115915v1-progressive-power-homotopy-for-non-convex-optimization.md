---
layout: default
title: Progressive Power Homotopy for Non-convex Optimization
---

# Progressive Power Homotopy for Non-convex Optimization
**arXiv**：[2601.15915v1](https://arxiv.org/abs/2601.15915) · [PDF](https://arxiv.org/pdf/2601.15915.pdf)  
**作者**：Chen Xu  

**一句话要点**：提出渐进幂同伦方法以解决非凸优化中的复杂景观导航问题

**关键词**：非凸优化, 渐进幂同伦, 随机梯度上升, 相位恢复, 神经网络训练, 全局收敛

## 3 点简述
- 核心问题：非凸优化中标准一阶方法在复杂景观下易陷入局部最优，难以收敛到全局最优。
- 方法要点：通过幂变换和高斯平滑构建代理目标，并渐进调整参数，结合随机梯度上升进行优化。
- 实验或效果：在相位恢复和欠参数化两层神经网络训练中表现优异，尤其在样本维度比接近信息论极限时优势明显。

## 摘要（原文）

> We propose a novel first-order method for non-convex optimization of the form $\max_{\bm{w}\in\mathbb{R}^d}\mathbb{E}_{\bm{x}\sim\mathcal{D}}[f_{\bm{w}}(\bm{x})]$, termed Progressive Power Homotopy (Prog-PowerHP). The method applies stochastic gradient ascent to a surrogate objective obtained by first performing a power transformation and then Gaussian smoothing, $F_{N,σ}(\bmμ):=\mathbb{E}_{\bm{w}\sim\mathcal{N}(\bmμ,σ^2I_d),\bm{x}\sim\mathcal{D}}[e^{Nf_w(\bm{x})}]$, while progressively increasing the power parameter $N$ and decreasing the smoothing scale $σ$ along the optimization trajectory. We prove that, under mild regularity conditions, Prog-PowerHP converges to a small neighborhood of the global optimum with an iteration complexity scaling nearly as $O(d^2\varepsilon^{-2})$. Empirically, Prog-PowerHP demonstrates clear advantages in phase retrieval when the samples-to-dimension ratio approaches the information-theoretic limit, and in training two-layer neural networks in under-parameterized regimes. These results suggest that Prog-PowerHP is particularly effective for navigating cluttered non-convex landscapes where standard first-order methods struggle.


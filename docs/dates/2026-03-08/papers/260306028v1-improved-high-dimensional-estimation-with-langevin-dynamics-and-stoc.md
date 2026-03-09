---
layout: default
title: Improved high-dimensional estimation with Langevin dynamics and stochastic weight averaging
---

# Improved high-dimensional estimation with Langevin dynamics and stochastic weight averaging
**arXiv**：[2603.06028v1](https://arxiv.org/abs/2603.06028) · [PDF](https://arxiv.org/pdf/2603.06028.pdf)  
**作者**：Stanley Wei, Alex Damian, Jason D. Lee  

**一句话要点**：提出基于Langevin动力学和迭代平均的高维估计方法，以降低样本复杂度至d^{k*/2}。

**关键词**：高维估计, Langevin动力学, 迭代平均, 信息指数, 张量PCA, 单指标模型

## 3 点简述
- 研究高维估计中梯度下降恢复隐藏方向的问题，关注信息指数k*对样本复杂度的影响。
- 通过Langevin动力学结合迭代平均，模拟平滑化景观效果，无需显式平滑即可降低样本需求。
- 应用于张量PCA和单指标模型，验证方法有效性，并推测小批量SGD也能达到相同速率。

## 摘要（原文）

> Significant recent work has studied the ability of gradient descent to recover a hidden planted direction $θ^\star \in S^{d-1}$ in different high-dimensional settings, including tensor PCA and single-index models. The key quantity that governs the ability of gradient descent to traverse these landscapes is the information exponent $k^\star$ (Ben Arous et al., (2021)), which corresponds to the order of the saddle at initialization in the population landscape. Ben Arous et al., (2021) showed that $n \gtrsim d^{\max(1, k^\star-1)}$ samples were necessary and sufficient for online SGD to recover $θ^\star$, and Ben Arous et al., (2020) proved a similar lower bound for Langevin dynamics. More recently, Damian et al., (2023) showed it was possible to circumvent these lower bounds by running gradient descent on a smoothed landscape, and that this algorithm succeeds with $n \gtrsim d^{\max(1, k^\star/2)}$ samples, which is optimal in the worst case. This raises the question of whether it is possible to achieve the same rate without explicit smoothing. In this paper, we show that Langevin dynamics can succeed with $n \gtrsim d^{ k^\star/2 }$ samples if one considers the average iterate, rather than the last iterate. The key idea is that the combination of noise-injection and iterate averaging is able to emulate the effect of landscape smoothing. We apply this result to both the tensor PCA and single-index model settings. Finally, we conjecture that minibatch SGD can also achieve the same rate without adding any additional noise.


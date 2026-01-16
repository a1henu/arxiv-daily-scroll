---
layout: default
title: Fundamental Limitations of Favorable Privacy-Utility Guarantees for DP-SGD
---

# Fundamental Limitations of Favorable Privacy-Utility Guarantees for DP-SGD
**arXiv**：[2601.10237v1](https://arxiv.org/abs/2601.10237) · [PDF](https://arxiv.org/pdf/2601.10237.pdf)  
**作者**：Murat Bilgehan Ertan, Marten van Dijk  

**一句话要点**：揭示DP-SGD在f-差分隐私下隐私-效用权衡的基本限制

**关键词**：差分隐私, DP-SGD, 隐私-效用权衡, f-差分隐私, 噪声乘子, 对抗模型

## 3 点简述
- 分析DP-SGD在f-差分隐私框架下的隐私-效用权衡曲线，推导出显式次优上界
- 证明小分离度κ要求高噪声乘子σ，导致强隐私与高效用无法同时实现
- 实验验证噪声水平导致实际训练中准确度显著下降，扩展至泊松子采样

## 摘要（原文）

> Differentially Private Stochastic Gradient Descent (DP-SGD) is the dominant paradigm for private training, but its fundamental limitations under worst-case adversarial privacy definitions remain poorly understood. We analyze DP-SGD in the $f$-differential privacy framework, which characterizes privacy via hypothesis-testing trade-off curves, and study shuffled sampling over a single epoch with $M$ gradient updates. We derive an explicit suboptimal upper bound on the achievable trade-off curve. This result induces a geometric lower bound on the separation $κ$ which is the maximum distance between the mechanism's trade-off curve and the ideal random-guessing line. Because a large separation implies significant adversarial advantage, meaningful privacy requires small $κ$. However, we prove that enforcing a small separation imposes a strict lower bound on the Gaussian noise multiplier $σ$, which directly limits the achievable utility. In particular, under the standard worst-case adversarial model, shuffled DP-SGD must satisfy
>   $σ\ge \frac{1}{\sqrt{2\ln M}}$ $\quad\text{or}\quad$ $κ\ge\ \frac{1}{\sqrt{8}}\!\left(1-\frac{1}{\sqrt{4π\ln M}}\right)$,
>   and thus cannot simultaneously achieve strong privacy and high utility. Although this bound vanishes asymptotically as $M \to \infty$, the convergence is extremely slow: even for practically relevant numbers of updates the required noise magnitude remains substantial. We further show that the same limitation extends to Poisson subsampling up to constant factors. Our experiments confirm that the noise levels implied by this bound leads to significant accuracy degradation at realistic training settings, thus showing a critical bottleneck in DP-SGD under standard worst-case adversarial assumptions.


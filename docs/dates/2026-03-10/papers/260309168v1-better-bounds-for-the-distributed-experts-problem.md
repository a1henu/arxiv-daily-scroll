---
layout: default
title: Better Bounds for the Distributed Experts Problem
---

# Better Bounds for the Distributed Experts Problem
**arXiv**：[2603.09168v1](https://arxiv.org/abs/2603.09168) · [PDF](https://arxiv.org/pdf/2603.09168.pdf)  
**作者**：David P. Woodruff, Samson Zhou  

**一句话要点**：提出分布式专家协议，以更优通信成本最小化分布式专家问题的遗憾

**关键词**：分布式专家问题, 遗憾最小化, 通信复杂度, ℓ_p范数损失, 多服务器优化

## 3 点简述
- 研究分布式专家问题，专家分布在服务器上，损失基于ℓ_p范数
- 设计协议实现遗憾约R≳1/(√T·poly log(nsT))，改进先前工作
- 通信成本为O((n/R²+s/R²)·max(s^{1-2/p},1)·poly log(nsT))比特

## 摘要（原文）

> In this paper, we study the distributed experts problem, where $n$ experts are distributed across $s$ servers for $T$ timesteps. The loss of each expert at each time $t$ is the $\ell_p$ norm of the vector that consists of the losses of the expert at each of the $s$ servers at time $t$. The goal is to minimize the regret $R$, i.e., the loss of the distributed protocol compared to the loss of the best expert, amortized over the all $T$ times, while using the minimum amount of communication. We give a protocol that achieves regret roughly $R\gtrsim\frac{1}{\sqrt{T}\cdot\text{poly}\log(nsT)}$, using $\mathcal{O}\left(\frac{n}{R^2}+\frac{s}{R^2}\right)\cdot\max(s^{1-2/p},1)\cdot\text{poly}\log(nsT)$ bits of communication, which improves on previous work.


---
layout: default
title: Variational Distributional Neuron
---

# Variational Distributional Neuron
**arXiv**：[2602.18250v1](https://arxiv.org/abs/2602.18250) · [PDF](https://arxiv.org/pdf/2602.18250.pdf)  
**作者**：Yves Ruffenach  

**一句话要点**：提出变分分布神经元，将计算单元从确定性标量扩展为分布，以在约束下收缩可能性空间。

**关键词**：变分自编码器, 分布神经元, 局部ELBO, 不确定性计算, 自回归先验

## 3 点简述
- 核心问题：传统计算单元传播标量，不确定性由全局机制承载，而非单元本身。
- 方法要点：神经元作为VAE模块，包含先验、摊销后验和局部ELBO，通过KL项正则化。
- 实验或效果：分析崩溃模式，定义“活神经元”条件，并通过自回归先验扩展时间贡献。

## 摘要（原文）

> We propose a proof of concept for a variational distributional neuron: a compute unit formulated as a VAE brick, explicitly carrying a prior, an amortized posterior and a local ELBO. The unit is no longer a deterministic scalar but a distribution: computing is no longer about propagating values, but about contracting a continuous space of possibilities under constraints. Each neuron parameterizes a posterior, propagates a reparameterized sample and is regularized by the KL term of a local ELBO - hence, the activation is distributional. This "contraction" becomes testable through local constraints and can be monitored via internal measures. The amount of contextual information carried by the unit, as well as the temporal persistence of this information, are locally tuned by distinct constraints. This proposal addresses a structural tension: in sequential generation, causality is predominantly organized in the symbolic space and, even when latents exist, they often remain auxiliary, while the effective dynamics are carried by a largely deterministic decoder. In parallel, probabilistic latent models capture factors of variation and uncertainty, but that uncertainty typically remains borne by global or parametric mechanisms, while units continue to propagate scalars - hence the pivot question: if uncertainty is intrinsic to computation, why does the compute unit not carry it explicitly? We therefore draw two axes: (i) the composition of probabilistic constraints, which must be made stable, interpretable and controllable; and (ii) granularity: if inference is a negotiation of distributions under constraints, should the primitive unit remain deterministic or become distributional? We analyze "collapse" modes and the conditions for a "living neuron", then extend the contribution over time via autoregressive priors over the latent, per unit.


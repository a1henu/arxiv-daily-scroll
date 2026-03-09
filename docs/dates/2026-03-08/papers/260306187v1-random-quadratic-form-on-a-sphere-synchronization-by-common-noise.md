---
layout: default
title: Random Quadratic Form on a Sphere: Synchronization by Common Noise
---

# Random Quadratic Form on a Sphere: Synchronization by Common Noise
**arXiv**：[2603.06187v1](https://arxiv.org/abs/2603.06187) · [PDF](https://arxiv.org/pdf/2603.06187.pdf)  
**作者**：Maximilian Engel, Anna Shalova  

**一句话要点**：提出随机二次形式模型以解释Transformer中线性层的同步聚类现象

**关键词**：随机微分方程, 同步现象, Transformer模型, 不变测度, 随机吸引子, 聚类行为

## 3 点简述
- 研究随机二次形式在球面上的梯度流，分析其两点运动的同步行为
- 通过不变测度和随机吸引子，提供分布和路径层面的同步特征化
- 模型独立于自注意力机制，为Transformer中token聚类提供替代解释

## 摘要（原文）

> We introduce the Random Quadratic Form (RQF): a stochastic differential equation which formally corresponds to the gradient flow of a random quadratic functional on a sphere. While the one-point dynamics of the system is a Brownian motion and thus has no preferred direction, the two-point motion exhibits nontrivial synchronizing behaviour. In this work we study synchronization of the RQF, namely we give both distributional and path-wise characterizations of the solutions by studying invariant measures and random attractors of the system.
>   The RQF model is motivated by the study of the role of linear layers in transformers and illustrates the synchronization by common noise phenomena arising in the simplified models of transformers. In particular, we provide an alternative (independent of self-attention) explanation of the clustering behaviour in deep transformers and show that tokens cluster even in the absence of the self-attention mechanism.


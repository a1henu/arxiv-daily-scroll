---
layout: default
title: Perceptrons and localization of attention's mean-field landscape
---

# Perceptrons and localization of attention's mean-field landscape
**arXiv**：[2601.21366v1](https://arxiv.org/abs/2601.21366) · [PDF](https://arxiv.org/pdf/2601.21366.pdf)  
**作者**：Antonio Álvarez-López, Borjan Geshkovski, Domènec Ruiz-Balet  

**一句话要点**：研究Transformer前向传播中感知器块对临界点原子性与局部化的影响

**关键词**：Transformer, 感知器块, 临界点, Wasserstein梯度流, 注意力机制, 单位球面

## 3 点简述
- 核心问题：Transformer前向传播在单位球面上作为交互粒子系统，感知器块如何影响临界点性质
- 方法要点：利用Wasserstein梯度流分析无限上下文长度极限，证明临界点通常为原子化且局部化
- 实验或效果：理论推导表明临界点集中在球面子集，支持Transformer注意力机制的局部化解释

## 摘要（原文）

> The forward pass of a Transformer can be seen as an interacting particle system on the unit sphere: time plays the role of layers, particles that of token embeddings, and the unit sphere idealizes layer normalization. In some weight settings the system can even be seen as a gradient flow for an explicit energy, and one can make sense of the infinite context length (mean-field) limit thanks to Wasserstein gradient flows. In this paper we study the effect of the perceptron block in this setting, and show that critical points are generically atomic and localized on subsets of the sphere.


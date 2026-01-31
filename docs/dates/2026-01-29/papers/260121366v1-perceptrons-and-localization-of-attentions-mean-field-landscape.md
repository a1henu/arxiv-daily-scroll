---
layout: default
title: Perceptrons and localization of attention's mean-field landscape
---

# Perceptrons and localization of attention's mean-field landscape
**arXiv**：[2601.21366v1](https://arxiv.org/abs/2601.21366) · [PDF](https://arxiv.org/pdf/2601.21366.pdf)  
**作者**：Antonio Álvarez-López, Borjan Geshkovski, Domènec Ruiz-Balet  

**一句话要点**：研究Transformer中感知器块对注意力平均场景观临界点局部化的影响

**关键词**：Transformer模型, 平均场理论, Wasserstein梯度流, 临界点分析, 注意力机制, 感知器块

## 3 点简述
- 核心问题：Transformer前向传播在平均场极限下，感知器块如何影响注意力机制的临界点分布。
- 方法要点：将Transformer建模为球面上的交互粒子系统，利用Wasserstein梯度流分析无限上下文长度极限。
- 实验或效果：证明临界点通常为原子性，并局部化在球面的子集上。

## 摘要（原文）

> The forward pass of a Transformer can be seen as an interacting particle system on the unit sphere: time plays the role of layers, particles that of token embeddings, and the unit sphere idealizes layer normalization. In some weight settings the system can even be seen as a gradient flow for an explicit energy, and one can make sense of the infinite context length (mean-field) limit thanks to Wasserstein gradient flows. In this paper we study the effect of the perceptron block in this setting, and show that critical points are generically atomic and localized on subsets of the sphere.


---
layout: default
title: Perceptrons and localization of attention's mean-field landscape
---

# Perceptrons and localization of attention's mean-field landscape
**arXiv**：[2601.21366v1](https://arxiv.org/abs/2601.21366) · [PDF](https://arxiv.org/pdf/2601.21366.pdf)  
**作者**：Antonio Álvarez-López, Borjan Geshkovski, Domènec Ruiz-Balet  

**一句话要点**：研究Transformer前向传播中感知器块对临界点原子性和局部化的影响

**关键词**：Transformer模型, 均值场极限, Wasserstein梯度流, 临界点分析, 感知器块, 注意力机制

## 3 点简述
- 将Transformer前向传播建模为球面上的交互粒子系统，分析无限上下文长度极限
- 探讨感知器块在梯度流设置下的作用，证明临界点通常为原子性并局部化于球面子集
- 基于Wasserstein梯度流理论，提供理论分析以理解注意力机制的均值场景观

## 摘要（原文）

> The forward pass of a Transformer can be seen as an interacting particle system on the unit sphere: time plays the role of layers, particles that of token embeddings, and the unit sphere idealizes layer normalization. In some weight settings the system can even be seen as a gradient flow for an explicit energy, and one can make sense of the infinite context length (mean-field) limit thanks to Wasserstein gradient flows. In this paper we study the effect of the perceptron block in this setting, and show that critical points are generically atomic and localized on subsets of the sphere.


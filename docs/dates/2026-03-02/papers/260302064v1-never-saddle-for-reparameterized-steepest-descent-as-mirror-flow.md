---
layout: default
title: Never Saddle for Reparameterized Steepest Descent as Mirror Flow
---

# Never Saddle for Reparameterized Steepest Descent as Mirror Flow
**arXiv**：[2603.02064v1](https://arxiv.org/abs/2603.02064) · [PDF](https://arxiv.org/pdf/2603.02064.pdf)  
**作者**：Tom Jacobs, Chao Zhou, Rebekka Burkholz  

**一句话要点**：提出最速镜像流框架，解释Adam类优化器在微调中优于SGD的机制。

**关键词**：优化算法, 最速下降法, 鞍点逃逸, 特征学习, Adam优化器, 微调

## 3 点简述
- 研究优化算法如何影响模型特征学习能力，聚焦最速下降法。
- 引入最速镜像流统一理论框架，揭示优化几何对学习动态和稀疏性的影响。
- 通过实验验证鞍点逃逸是微调关键挑战，并展示解耦权重衰减的稳定作用。

## 摘要（原文）

> How does the choice of optimization algorithm shape a model's ability to learn features? To address this question for steepest descent methods --including sign descent, which is closely related to Adam --we introduce steepest mirror flows as a unifying theoretical framework. This framework reveals how optimization geometry governs learning dynamics, implicit bias, and sparsity and it provides two explanations for why Adam and AdamW often outperform SGD in fine-tuning. Focusing on diagonal linear networks and deep diagonal linear reparameterizations (a simplified proxy for attention), we show that steeper descent facilitates both saddle-point escape and feature learning. In contrast, gradient descent requires unrealistically large learning rates to escape saddles, an uncommon regime in fine-tuning. Empirically, we confirm that saddle-point escape is a central challenge in fine-tuning. Furthermore, we demonstrate that decoupled weight decay, as in AdamW, stabilizes feature learning by enforcing novel balance equations. Together, these results highlight two mechanisms how steepest descent can aid modern optimization.


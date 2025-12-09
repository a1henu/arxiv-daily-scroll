---
layout: default
title: LogicCBMs: Logic-Enhanced Concept-Based Learning
---

# LogicCBMs: Logic-Enhanced Concept-Based Learning
**arXiv**：[2512.07383v1](https://arxiv.org/abs/2512.07383) · [PDF](https://arxiv.org/pdf/2512.07383.pdf)  
**作者**：Deepika SN Vemuri, Gautham Bellamkonda, Aditya Pola, Vineeth N Balasubramanian  

**一句话要点**：提出LogicCBM以增强概念瓶颈模型，通过逻辑模块提升表达力与可解释性。

**关键词**：概念瓶颈模型, 逻辑增强学习, 可解释人工智能, 可微分逻辑, 概念关系建模

## 3 点简述
- 概念瓶颈模型线性组合概念限制表达力，需超越简单加权。
- 引入可微分逻辑模块连接概念，支持逻辑操作以捕获概念间关系。
- 实验表明模型在基准数据集上提高准确性，并保持端到端可学习性。

## 摘要（原文）

> Concept Bottleneck Models (CBMs) provide a basis for semantic abstractions within a neural network architecture. Such models have primarily been seen through the lens of interpretability so far, wherein they offer transparency by inferring predictions as a linear combination of semantic concepts. However, a linear combination is inherently limiting. So we propose the enhancement of concept-based learning models through propositional logic. We introduce a logic module that is carefully designed to connect the learned concepts from CBMs through differentiable logic operations, such that our proposed LogicCBM can go beyond simple weighted combinations of concepts to leverage various logical operations to yield the final predictions, while maintaining end-to-end learnability. Composing concepts using a set of logic operators enables the model to capture inter-concept relations, while simultaneously improving the expressivity of the model in terms of logic operations. Our empirical studies on well-known benchmarks and synthetic datasets demonstrate that these models have better accuracy, perform effective interventions and are highly interpretable.


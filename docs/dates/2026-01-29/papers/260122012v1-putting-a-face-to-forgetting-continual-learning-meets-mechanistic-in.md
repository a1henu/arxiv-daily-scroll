---
layout: default
title: Putting a Face to Forgetting: Continual Learning meets Mechanistic Interpretability
---

# Putting a Face to Forgetting: Continual Learning meets Mechanistic Interpretability
**arXiv**：[2601.22012v1](https://arxiv.org/abs/2601.22012) · [PDF](https://arxiv.org/pdf/2601.22012.pdf)  
**作者**：Sergi Masip, Gido M. van de Ven, Javier Ferrando, Tinne Tuytelaars  

**一句话要点**：提出机制解释框架，从特征层面分析持续学习中的灾难性遗忘问题。

**关键词**：持续学习, 灾难性遗忘, 机制解释, 特征编码, Vision Transformer

## 3 点简述
- 核心问题：灾难性遗忘常从性能或最后一层表征衡量，忽略底层机制。
- 方法要点：引入几何解释框架，将遗忘视为个体特征编码的变换导致。
- 实验或效果：通过可处理模型分析验证，并在Vision Transformer上应用案例研究。

## 摘要（原文）

> Catastrophic forgetting in continual learning is often measured at the performance or last-layer representation level, overlooking the underlying mechanisms. We introduce a mechanistic framework that offers a geometric interpretation of catastrophic forgetting as the result of transformations to the encoding of individual features. These transformations can lead to forgetting by reducing the allocated capacity of features (worse representation) and disrupting their readout by downstream computations. Analysis of a tractable model formalizes this view, allowing us to identify best- and worst-case scenarios. Through experiments on this model, we empirically test our formal analysis and highlight the detrimental effect of depth. Finally, we demonstrate how our framework can be used in the analysis of practical models through the use of Crosscoders. We present a case study of a Vision Transformer trained on sequential CIFAR-10. Our work provides a new, feature-centric vocabulary for continual learning.


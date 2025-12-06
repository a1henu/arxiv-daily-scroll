---
layout: default
title: SuperActivators: Only the Tail of the Distribution Contains Reliable Concept Signals
---

# SuperActivators: Only the Tail of the Distribution Contains Reliable Concept Signals
**arXiv**：[2512.05038v1](https://arxiv.org/abs/2512.05038) · [PDF](https://arxiv.org/pdf/2512.05038.pdf)  
**作者**：Cassandra Goldberg, Chaehyeon Kim, Adam Stein, Eric Wong  

**一句话要点**：提出SuperActivator机制，利用概念分布高尾端信号提升概念检测可靠性

**关键词**：概念向量, 模型可解释性, 激活分布, 概念检测, 特征归因

## 3 点简述
- 概念向量常因激活噪声而效用受限，存在信号重叠问题
- 发现概念分布高尾端激活提供可靠概念信号，称为SuperActivator机制
- 实验显示该方法在跨模态和架构中提升F1分数达14%，改善特征归因

## 摘要（原文）

> Concept vectors aim to enhance model interpretability by linking internal representations with human-understandable semantics, but their utility is often limited by noisy and inconsistent activations. In this work, we uncover a clear pattern within the noise, which we term the SuperActivator Mechanism: while in-concept and out-of-concept activations overlap considerably, the token activations in the extreme high tail of the in-concept distribution provide a reliable signal of concept presence. We demonstrate the generality of this mechanism by showing that SuperActivator tokens consistently outperform standard vector-based and prompting concept detection approaches, achieving up to a 14% higher F1 score across image and text modalities, model architectures, model layers, and concept extraction techniques. Finally, we leverage SuperActivator tokens to improve feature attributions for concepts.


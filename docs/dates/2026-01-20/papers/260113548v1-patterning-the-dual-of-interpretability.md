---
layout: default
title: Patterning: The Dual of Interpretability
---

# Patterning: The Dual of Interpretability
**arXiv**：[2601.13548v1](https://arxiv.org/abs/2601.13548) · [PDF](https://arxiv.org/pdf/2601.13548.pdf)  
**作者**：George Wang, Daniel Murfet  

**一句话要点**：提出patterning作为可解释性的对偶问题，通过数据干预引导模型内部结构形成

**关键词**：可解释性, 数据干预, 敏感性分析, 泛化控制, 模型结构形成

## 3 点简述
- 核心问题：如何从期望的泛化形式反推所需训练数据，作为可解释性的对偶
- 方法要点：基于敏感性度量，线性反演数据分布微小变化以干预模型内部配置
- 实验或效果：在小型语言模型中加速或延迟结构形成，在合成任务中选择学习算法

## 摘要（原文）

> Mechanistic interpretability aims to understand how neural networks generalize beyond their training data by reverse-engineering their internal structures. We introduce patterning as the dual problem: given a desired form of generalization, determine what training data produces it. Our approach is based on susceptibilities, which measure how posterior expectation values of observables respond to infinitesimal shifts in the data distribution. Inverting this linear response relationship yields the data intervention that steers the model toward a target internal configuration. We demonstrate patterning in a small language model, showing that re-weighting training data along principal susceptibility directions can accelerate or delay the formation of structure, such as the induction circuit. In a synthetic parentheses balancing task where multiple algorithms achieve perfect training accuracy, we show that patterning can select which algorithm the model learns by targeting the local learning coefficient of each solution. These results establish that the same mathematical framework used to read internal structure can be inverted to write it.


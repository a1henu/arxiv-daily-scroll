---
layout: default
title: DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems
---

# DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems
**arXiv**：[2601.01931v1](https://arxiv.org/abs/2601.01931) · [PDF](https://arxiv.org/pdf/2601.01931.pdf)  
**作者**：Willem Röpke, Samuel Coward, Andrei Lupu, Thomas Foster, Tim Rocktäschel, Jakob Foerster  

**一句话要点**：提出DéjàQ框架，通过联合进化合成数学问题与模型训练，以增强数学推理的泛化能力。

**关键词**：数学推理, 数据进化, LLM驱动突变, 强化学习训练, 泛化能力

## 3 点简述
- 核心问题：静态数据集可能导致模型记忆而非泛化，限制数学推理能力。
- 方法要点：使用LLM驱动突变策略，模型自身进化训练数据，优化问题可学习性。
- 实验或效果：模型能生成新颖问题，LLM驱动突变提升强化学习训练效果，支持开源代码。

## 摘要（原文）

> Recent advances in reasoning models have yielded impressive results in mathematics and coding. However, most approaches rely on static datasets, which have been suggested to encourage memorisation and limit generalisation. We introduce DéjàQ, a framework that departs from this paradigm by jointly evolving a diverse set of synthetic mathematical problems alongside model training. This evolutionary process adapts to the model's ability throughout training, optimising problems for learnability. We propose two LLM-driven mutation strategies in which the model itself mutates the training data, either by altering contextual details or by directly modifying problem structure. We find that the model can generate novel and meaningful problems, and that these LLM-driven mutations improve RL training. We analyse key aspects of DéjàQ, including the validity of generated problems and computational overhead. Our results underscore the potential of dynamically evolving training data to enhance mathematical reasoning and indicate broader applicability, which we will support by open-sourcing our code.


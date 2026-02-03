---
layout: default
title: Structure Enables Effective Self-Localization of Errors in LLMs
---

# Structure Enables Effective Self-Localization of Errors in LLMs
**arXiv**：[2602.02416v1](https://arxiv.org/abs/2602.02416) · [PDF](https://arxiv.org/pdf/2602.02416.pdf)  
**作者**：Ankur Samanta, Akshayaa Magesh, Ayush Jain, Kavosh Asadi, Youliang Yu, Daniel Jiang, Boris Vidolov, Kaveh Hassani, Paul Sajda, Jalaj Bhandari, Yonathan Efroni  

**一句话要点**：提出Thought-ICS框架，通过结构化推理步骤实现大语言模型错误自定位与自纠正

**关键词**：大语言模型自纠正, 结构化推理, 错误定位, 迭代采样, 思维步骤分解

## 3 点简述
- 核心问题：大语言模型在传统链式推理中难以有效自定位错误，阻碍自纠正能力发展
- 方法要点：引入结构化提示方法，将推理分解为离散语义连贯的思维步骤，并基于此设计迭代纠正采样框架
- 实验或效果：在外部验证下，Thought-ICS提升自纠正率20-40%；在完全自主设置中，优于现有自纠正基线

## 摘要（原文）

> Self-correction in language models remains elusive. In this work, we explore whether language models can explicitly localize errors in incorrect reasoning, as a path toward building AI systems that can effectively correct themselves. We introduce a prompting method that structures reasoning as discrete, semantically coherent thought steps, and show that models are able to reliably localize errors within this structure, while failing to do so in conventional, unstructured chain-of-thought reasoning. Motivated by how the human brain monitors errors at discrete decision points and resamples alternatives, we introduce Iterative Correction Sampling of Thoughts (Thought-ICS), a self-correction framework. Thought-ICS iteratively prompts the model to generate reasoning one discrete and complete thought at a time--where each thought represents a deliberate decision by the model--creating natural boundaries for precise error localization. Upon verification, the model localizes the first erroneous step, and the system backtracks to generate alternative reasoning from the last correct point. When asked to correct reasoning verified as incorrect by an oracle, Thought-ICS achieves 20-40% self-correction lift. In a completely autonomous setting without external verification, it outperforms contemporary self-correction baselines.


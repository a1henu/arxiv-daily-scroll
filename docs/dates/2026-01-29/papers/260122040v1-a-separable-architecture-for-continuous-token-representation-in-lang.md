---
layout: default
title: A Separable Architecture for Continuous Token Representation in Language Models
---

# A Separable Architecture for Continuous Token Representation in Language Models
**arXiv**：[2601.22040v1](https://arxiv.org/abs/2601.22040) · [PDF](https://arxiv.org/pdf/2601.22040.pdf)  
**作者**：Reza T. Batley, Sourav Saha  

**一句话要点**：提出Leviathan架构，通过连续嵌入生成器替换离散查找表，提升小语言模型的参数效率。

**关键词**：小语言模型, 连续嵌入, 参数效率, Transformer架构, Pile数据集

## 3 点简述
- 核心问题：小语言模型中嵌入矩阵参数占比高，导致参数分配不优。
- 方法要点：设计连续嵌入生成器，替代传统离散查找表，优化参数使用。
- 实验或效果：在Pile数据集上，Leviathan在等参数设置下优于标准架构，有效参数容量提升1.47至2.11倍。

## 摘要（原文）

> Transformer scaling law analyses typically treat parameters as interchangeable; an abstraction that accurately predicts loss-compute relationships. Yet, in sub-billion-parameter small language models (SLMs), embedding matrices dominate the parameter budget. This work argues that this allocation is as suboptimal as it is counterintuitive. Leviathan is an architecture with a continuous embedding generator to replace the discrete lookup tables of canonical models. Evaluating on the Pile dataset under isoparametric settings, Leviathan consistently outperforms a standard, LLaMA-style architecture. By means of an empirical power-law fit, Leviathan exhibits a markedly superior effective parameter capacity. Across the regime studied, Leviathan behaves as a dense model with $1.47$ to $2.11 \times$ more parameters.


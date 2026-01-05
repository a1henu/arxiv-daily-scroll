---
layout: default
title: Fast-weight Product Key Memory
---

# Fast-weight Product Key Memory
**arXiv**：[2601.00671v1](https://arxiv.org/abs/2601.00671) · [PDF](https://arxiv.org/pdf/2601.00671.pdf)  
**作者**：Tianyu Zhao, Llion Jones  

**一句话要点**：提出快速权重乘积键记忆以解决序列建模中存储容量与计算效率的权衡问题

**关键词**：快速权重记忆, 乘积键记忆, 序列建模, 长上下文处理, 情景记忆, 梯度下降更新

## 3 点简述
- 核心问题：现代语言模型序列层面临存储容量与计算效率的权衡，Softmax注意力成本高，线性变体存储有限
- 方法要点：将稀疏乘积键记忆转化为动态快速权重情景记忆，通过局部块级梯度下降动态更新参数
- 实验或效果：在长上下文数据集上显著降低困惑度，在128K令牌上下文中泛化良好，仅用4K令牌序列训练

## 摘要（原文）

> Sequence modeling layers in modern language models typically face a trade-off between storage capacity and computational efficiency. While Softmax attention offers unbounded storage at prohibitive quadratic costs, linear variants provide efficiency but suffer from limited, fixed-size storage. We propose Fast-weight Product Key Memory (FwPKM), a novel architecture that resolves this tension by transforming the sparse Product Key Memory (PKM) from a static module into a dynamic, "fast-weight" episodic memory. Unlike PKM, FwPKM updates its parameters dynamically at both training and inference time via local chunk-level gradient descent, allowing the model to rapidly memorize and retrieve new key-value pairs from input sequences. Experiments reveal that FwPKM functions as an effective episodic memory that complements the semantic memory of standard modules, yielding significant perplexity reductions on long-context datasets. Notably, in Needle in a Haystack evaluations, FwPKM generalizes to 128K-token contexts despite being trained on only 4K-token sequences.


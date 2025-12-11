---
layout: default
title: Circuits, Features, and Heuristics in Molecular Transformers
---

# Circuits, Features, and Heuristics in Molecular Transformers
**arXiv**：[2512.09757v1](https://arxiv.org/abs/2512.09757) · [PDF](https://arxiv.org/pdf/2512.09757.pdf)  
**作者**：Kristof Varadi, Mark Marosi, Peter Antal  

**一句话要点**：提出基于稀疏自编码器的机制分析，揭示分子Transformer在药物分子生成中的计算结构。

**关键词**：分子Transformer, 机制分析, 稀疏自编码器, 化学结构生成, 药物分子

## 3 点简述
- 核心问题：Transformer模型在分子生成中捕获化学规则的具体机制未知。
- 方法要点：使用稀疏自编码器提取与化学相关激活模式的特征字典。
- 实验或效果：在多个下游任务中验证机制洞察，提升预测性能。

## 摘要（原文）

> Transformers generate valid and diverse chemical structures, but little is known about the mechanisms that enable these models to capture the rules of molecular representation. We present a mechanistic analysis of autoregressive transformers trained on drug-like small molecules to reveal the computational structure underlying their capabilities across multiple levels of abstraction. We identify computational patterns consistent with low-level syntactic parsing and more abstract chemical validity constraints. Using sparse autoencoders (SAEs), we extract feature dictionaries associated with chemically relevant activation patterns. We validate our findings on downstream tasks and find that mechanistic insights can translate to predictive performance in various practical settings.


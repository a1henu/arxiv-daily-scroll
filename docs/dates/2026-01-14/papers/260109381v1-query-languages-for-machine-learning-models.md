---
layout: default
title: Query Languages for Machine-Learning Models
---

# Query Languages for Machine-Learning Models
**arXiv**：[2601.09381v1](https://arxiv.org/abs/2601.09381) · [PDF](https://arxiv.org/pdf/2601.09381.pdf)  
**作者**：Martin Grohe  

**一句话要点**：提出FO(SUM)和IFP(SUM)逻辑作为机器学习模型的查询语言，用于神经网络等加权图表示

**关键词**：查询语言, 机器学习模型, 神经网络, 加权图, 逻辑表达, 计算复杂性

## 3 点简述
- 核心问题：如何为机器学习模型（如神经网络）开发查询语言，以表达对模型结构的查询
- 方法要点：基于加权有限结构的逻辑，包括带求和的一阶逻辑FO(SUM)及其递归扩展IFP(SUM)
- 实验或效果：提供查询神经网络的示例，并分析这些逻辑的表达能力和计算复杂性

## 摘要（原文）

> In this paper, I discuss two logics for weighted finite structures: first-order logic with summation (FO(SUM)) and its recursive extension IFP(SUM). These logics originate from foundational work by Grädel, Gurevich, and Meer in the 1990s. In recent joint work with Standke, Steegmans, and Van den Bussche, we have investigated these logics as query languages for machine learning models, specifically neural networks, which are naturally represented as weighted graphs. I present illustrative examples of queries to neural networks that can be expressed in these logics and discuss fundamental results on their expressiveness and computational complexity.


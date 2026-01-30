---
layout: default
title: ECSEL: Explainable Classification via Signomial Equation Learning
---

# ECSEL: Explainable Classification via Signomial Equation Learning
**arXiv**：[2601.21789v1](https://arxiv.org/abs/2601.21789) · [PDF](https://arxiv.org/pdf/2601.21789.pdf)  
**作者**：Adia Lumadjeng, Ilker Birbil, Erman Acar  

**一句话要点**：提出ECSEL方法，通过符号方程学习实现可解释分类，应用于符号回归和分类任务。

**关键词**：可解释分类, 符号方程学习, 符号回归, 闭式表达式, 特征分析, 反事实推理

## 3 点简述
- 核心问题：现有分类方法在保持高准确率的同时缺乏可解释性，难以提供结构化解释。
- 方法要点：ECSEL学习符号方程形式的表达式，直接构建结构化的闭式表达式，兼具分类和解释功能。
- 实验或效果：在符号回归基准上恢复更多目标方程，计算效率高；分类准确率与主流模型相当，支持特征分析和反事实推理。

## 摘要（原文）

> We introduce ECSEL, an explainable classification method that learns formal expressions in the form of signomial equations, motivated by the observation that many symbolic regression benchmarks admit compact signomial structure. ECSEL directly constructs a structural, closed-form expression that serves as both a classifier and an explanation. On standard symbolic regression benchmarks, our method recovers a larger fraction of target equations than competing state-of-the-art approaches while requiring substantially less computation. Leveraging this efficiency, ECSEL achieves classification accuracy competitive with established machine learning models without sacrificing interpretability. Further, we show that ECSEL satisfies some desirable properties regarding global feature behavior, decision-boundary analysis, and local feature attributions. Experiments on benchmark datasets and two real-world case studies i.e., e-commerce and fraud detection, demonstrate that the learned equations expose dataset biases, support counterfactual reasoning, and yield actionable insights.


---
layout: default
title: ECSEL: Explainable Classification via Signomial Equation Learning
---

# ECSEL: Explainable Classification via Signomial Equation Learning
**arXiv**：[2601.21789v1](https://arxiv.org/abs/2601.21789) · [PDF](https://arxiv.org/pdf/2601.21789.pdf)  
**作者**：Adia Lumadjeng, Ilker Birbil, Erman Acar  

**一句话要点**：提出ECSEL方法，通过符号方程学习实现可解释分类，应用于符号回归基准和实际案例。

**关键词**：可解释分类, 符号方程学习, 符号回归, 闭式表达式, 计算效率, 实际应用

## 3 点简述
- 核心问题：现有分类方法在可解释性和计算效率上存在权衡，难以同时提供结构化的解释和高效性能。
- 方法要点：ECSEL学习符号方程形式的正式表达式，直接构建结构化的闭式表达式，兼具分类器和解释功能。
- 实验或效果：在符号回归基准上恢复更多目标方程，计算量显著减少；在基准数据集和实际案例中展示高准确性和可解释性。

## 摘要（原文）

> We introduce ECSEL, an explainable classification method that learns formal expressions in the form of signomial equations, motivated by the observation that many symbolic regression benchmarks admit compact signomial structure. ECSEL directly constructs a structural, closed-form expression that serves as both a classifier and an explanation. On standard symbolic regression benchmarks, our method recovers a larger fraction of target equations than competing state-of-the-art approaches while requiring substantially less computation. Leveraging this efficiency, ECSEL achieves classification accuracy competitive with established machine learning models without sacrificing interpretability. Further, we show that ECSEL satisfies some desirable properties regarding global feature behavior, decision-boundary analysis, and local feature attributions. Experiments on benchmark datasets and two real-world case studies i.e., e-commerce and fraud detection, demonstrate that the learned equations expose dataset biases, support counterfactual reasoning, and yield actionable insights.


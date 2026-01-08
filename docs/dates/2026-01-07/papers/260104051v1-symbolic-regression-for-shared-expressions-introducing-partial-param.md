---
layout: default
title: Symbolic Regression for Shared Expressions: Introducing Partial Parameter Sharing
---

# Symbolic Regression for Shared Expressions: Introducing Partial Parameter Sharing
**arXiv**：[2601.04051v1](https://arxiv.org/abs/2601.04051) · [PDF](https://arxiv.org/pdf/2601.04051.pdf)  
**作者**：Viktor Martinek, Roland Herzog  

**一句话要点**：提出部分参数共享方法以扩展符号回归在多个分类变量下的表达共享能力

**关键词**：符号回归, 参数共享, 分类变量, 科学发现, 模型简化

## 3 点简述
- 符号回归用于数据集的符号表达式发现，但现有方法在参数共享上有限制
- 引入中间级参数共享，支持多个分类变量，减少参数数量并揭示问题结构
- 通过合成和天体物理数据集验证，在保持拟合质量的同时显著降低参数需求

## 摘要（原文）

> Symbolic Regression aims to find symbolic expressions that describe datasets. Due to better interpretability, it is a machine learning paradigm particularly powerful for scientific discovery. In recent years, several works have expanded the concept to allow the description of similar phenomena using a single expression with varying sets of parameters, thereby introducing categorical variables. Some previous works allow only "non-shared" (category-value-specific) parameters, and others also incorporate "shared" (category-value-agnostic) parameters. We expand upon those efforts by considering multiple categorical variables, and introducing intermediate levels of parameter sharing. With two categorical variables, an intermediate level of parameter sharing emerges, i.e., parameters which are shared across either category but change across the other. The new approach potentially decreases the number of parameters, while revealing additional information about the problem. Using a synthetic, fitting-only example, we test the limits of this setup in terms of data requirement reduction and transfer learning. As a real-world symbolic regression example, we demonstrate the benefits of the proposed approach on an astrophysics dataset used in a previous study, which considered only one categorical variable. We achieve a similar fit quality but require significantly fewer individual parameters, and extract additional information about the problem.


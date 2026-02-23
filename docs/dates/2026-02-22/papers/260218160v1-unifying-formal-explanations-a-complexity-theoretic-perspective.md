---
layout: default
title: Unifying Formal Explanations: A Complexity-Theoretic Perspective
---

# Unifying Formal Explanations: A Complexity-Theoretic Perspective
**arXiv**：[2602.18160v1](https://arxiv.org/abs/2602.18160) · [PDF](https://arxiv.org/pdf/2602.18160.pdf)  
**作者**：Shahaf Bassan, Xuanxiang Huang, Guy Katz  

**一句话要点**：提出统一概率价值函数框架，分析机器学习解释的计算复杂性

**关键词**：机器学习解释, 计算复杂性, 概率框架, 组合优化, 全局可解释性

## 3 点简述
- 核心问题：统一分析充分原因与对比原因解释的计算复杂性
- 方法要点：基于价值函数的单调性、子模性和超模性，区分局部与全局设置
- 实验或效果：证明全局设置下多项式时间可解，局部设置下NP难

## 摘要（原文）

> Previous work has explored the computational complexity of deriving two fundamental types of explanations for ML model predictions: (1) *sufficient reasons*, which are subsets of input features that, when fixed, determine a prediction, and (2) *contrastive reasons*, which are subsets of input features that, when modified, alter a prediction. Prior studies have examined these explanations in different contexts, such as non-probabilistic versus probabilistic frameworks and local versus global settings. In this study, we introduce a unified framework for analyzing these explanations, demonstrating that they can all be characterized through the minimization of a unified probabilistic value function. We then prove that the complexity of these computations is influenced by three key properties of the value function: (1) *monotonicity*, (2) *submodularity*, and (3) *supermodularity* - which are three fundamental properties in *combinatorial optimization*. Our findings uncover some counterintuitive results regarding the nature of these properties within the explanation settings examined. For instance, although the *local* value functions do not exhibit monotonicity or submodularity/supermodularity whatsoever, we demonstrate that the *global* value functions do possess these properties. This distinction enables us to prove a series of novel polynomial-time results for computing various explanations with provable guarantees in the global explainability setting, across a range of ML models that span the interpretability spectrum, such as neural networks, decision trees, and tree ensembles. In contrast, we show that even highly simplified versions of these explanations become NP-hard to compute in the corresponding local explainability setting.


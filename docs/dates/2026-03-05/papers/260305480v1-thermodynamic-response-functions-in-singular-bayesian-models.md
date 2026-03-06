---
layout: default
title: Thermodynamic Response Functions in Singular Bayesian Models
---

# Thermodynamic Response Functions in Singular Bayesian Models
**arXiv**：[2603.05480v1](https://arxiv.org/abs/2603.05480) · [PDF](https://arxiv.org/pdf/2603.05480.pdf)  
**作者**：Sean Plummer  

**一句话要点**：提出热力学响应理论框架，统一解释奇异贝叶斯模型中的复杂性与预测变异性

**关键词**：奇异学习理论, 热力学响应, 贝叶斯模型, 参数不可识别性, 后验调温, 复杂度度量

## 3 点简述
- 奇异统计模型因参数不可识别性违反正则渐近理论，导致传统学习理论量难以操作解释
- 通过后验调温诱导热力学响应函数，将WAIC、WBIC和奇异涨落纳入统一框架，赋予RLCT和奇异涨落热力学意义
- 在对称高斯混合、降秩回归和过参数化神经网络等示例中，实证展示调温下的相变行为与结构重组

## 摘要（原文）

> Singular statistical models-including mixtures, matrix factorization, and neural networks-violate regular asymptotics due to parameter non-identifiability and degenerate Fisher geometry. Although singular learning theory characterizes marginal likelihood behavior through invariants such as the real log canonical threshold and singular fluctuation, these quantities remain difficult to interpret operationally. At the same time, widely used criteria such as WAIC and WBIC appear disconnected from underlying singular geometry. We show that posterior tempering induces a one-parameter deformation of the posterior distribution whose associated observables generate a hierarchy of thermodynamic response functions. A universal covariance identity links derivatives of tempered expectations to posterior fluctuations, placing WAIC, WBIC, and singular fluctuation within a unified response framework. Within this framework, classical quantities from singular learning theory acquire natural thermodynamic interpretations: RLCT governs the leading free-energy slope, singular fluctuation corresponds to curvature of the tempered free energy, and WAIC measures predictive fluctuation. We formalize an observable algebra that quotients out non-identifiable directions, allowing structurally meaningful order parameters to be constructed in singular models. Across canonical singular examples-including symmetric Gaussian mixtures, reduced-rank regression, and overparameterized neural networks-we empirically demonstrate phase-transition-like behavior under tempering. Order parameters collapse, susceptibilities peak, and complexity measures align with structural reorganization in posterior geometry. Our results suggest that thermodynamic response theory provides a natural organizing framework for interpreting complexity, predictive variability, and structural reorganization in singular Bayesian learning.


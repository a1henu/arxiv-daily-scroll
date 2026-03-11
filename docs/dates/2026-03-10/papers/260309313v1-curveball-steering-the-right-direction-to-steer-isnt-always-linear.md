---
layout: default
title: Curveball Steering: The Right Direction To Steer Isn't Always Linear
---

# Curveball Steering: The Right Direction To Steer Isn't Always Linear
**arXiv**：[2603.09313v1](https://arxiv.org/abs/2603.09313) · [PDF](https://arxiv.org/pdf/2603.09313.pdf)  
**作者**：Shivam Raval, Hae Jin Song, Linlin Wu, Abir Harrasse, Jeff Phillips, Amirali Abdullah  

**一句话要点**：提出Curveball steering以解决激活空间中非线性几何失真导致的线性干预不一致问题。

**关键词**：激活干预, 非线性几何, 核PCA, 大语言模型控制, 表示学习

## 3 点简述
- 核心问题：线性表示假设在实践中常导致激活干预行为不一致，源于激活空间存在显著几何失真。
- 方法要点：基于多项式核PCA的非线性干预方法，在特征空间中执行干预，更好地适应学习到的激活几何。
- 实验或效果：Curveball steering在几何失真强的场景下，一致优于基于线性PCA的干预方法。

## 摘要（原文）

> Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations. Existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. In practice, however, such linear interventions often behave inconsistently. We question this assumption by analyzing the intrinsic geometry of LLM activation spaces. Measuring geometric distortion via the ratio of geodesic to Euclidean distances, we observe substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry. Motivated by this, we propose "Curveball steering", a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry. Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions.


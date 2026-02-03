---
layout: default
title: Provably Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function
---

# Provably Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function
**arXiv**：[2602.02406v1](https://arxiv.org/abs/2602.02406) · [PDF](https://arxiv.org/pdf/2602.02406.pdf)  
**作者**：Tung Quoc Le, Anh Tuan Nguyen, Viet Anh Nguyen  

**一句话要点**：提出首个多维超参数调优的泛化保证框架，基于实代数几何工具强化分析。

**关键词**：数据驱动算法设计, 多维超参数调优, 泛化保证, 实代数几何, 半代数函数类, 验证损失

## 3 点简述
- 核心问题：现有数据驱动超参数调优的统计基础有限，缺乏多维超参数的泛化保证。
- 方法要点：利用实代数几何工具，为半代数函数类建立更尖锐、更广泛适用的泛化保证框架。
- 实验或效果：框架应用于加权群套索和加权融合套索，展示新的可学习性结果。

## 摘要（原文）

> Data-driven algorithm design automates hyperparameter tuning, but its statistical foundations remain limited because model performance can depend on hyperparameters in implicit and highly non-smooth ways. Existing guarantees focus on the simple case of a one-dimensional (scalar) hyperparameter. This leaves the practically important, multi-dimensional hyperparameter tuning setting unresolved. We address this open question by establishing the first general framework for establishing generalization guarantees for tuning multi-dimensional hyperparameters in data-driven settings. Our approach strengthens the generalization guarantee framework for semi-algebraic function classes by exploiting tools from real algebraic geometry, yielding sharper, more broadly applicable guarantees. We then extend the analysis to hyperparameter tuning using the validation loss under minimal assumptions, and derive improved bounds when additional structure is available. Finally, we demonstrate the scope of the framework with new learnability results, including data-driven weighted group lasso and weighted fused lasso.


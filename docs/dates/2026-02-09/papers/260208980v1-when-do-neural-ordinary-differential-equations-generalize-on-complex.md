---
layout: default
title: When do neural ordinary differential equations generalize on complex networks?
---

# When do neural ordinary differential equations generalize on complex networks?
**arXiv**：[2602.08980v1](https://arxiv.org/abs/2602.08980) · [PDF](https://arxiv.org/pdf/2602.08980.pdf)  
**作者**：Moritz Laber, Tina Eliassi-Rad, Brennan Klein  

**一句话要点**：研究神经常微分方程在图数据上的泛化能力，揭示度异质性和动力学类型是关键因素

**关键词**：神经常微分方程, 图数据泛化, 度异质性, 动力学系统, S¹模型, 复杂网络

## 3 点简述
- 核心问题：神经常微分方程在图结构数据上的泛化行为，尤其在训练未见图大小或结构时表现未知
- 方法要点：使用Barabási-Barzel形式向量场和S¹模型生成图，分析五种常见图动力学系统
- 实验或效果：发现度异质性和动力学类型主导泛化能力，平均聚类起次要作用，影响固定点捕捉和缺失数据性能

## 摘要（原文）

> Neural ordinary differential equations (neural ODEs) can effectively learn dynamical systems from time series data, but their behavior on graph-structured data remains poorly understood, especially when applied to graphs with different size or structure than encountered during training. We study neural ODEs ($\mathtt{nODE}$s) with vector fields following the Barabási-Barzel form, trained on synthetic data from five common dynamical systems on graphs. Using the $\mathbb{S}^1$-model to generate graphs with realistic and tunable structure, we find that degree heterogeneity and the type of dynamical system are the primary factors in determining $\mathtt{nODE}$s' ability to generalize across graph sizes and properties. This extends to $\mathtt{nODE}$s' ability to capture fixed points and maintain performance amid missing data. Average clustering plays a secondary role in determining $\mathtt{nODE}$ performance. Our findings highlight $\mathtt{nODE}$s as a powerful approach to understanding complex systems but underscore challenges emerging from degree heterogeneity and clustering in realistic graphs.


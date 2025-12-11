---
layout: default
title: Bayesian Networks, Markov Networks, Moralisation, Triangulation: a Categorical Perspective
---

# Bayesian Networks, Markov Networks, Moralisation, Triangulation: a Categorical Perspective
**arXiv**：[2512.09908v1](https://arxiv.org/abs/2512.09908) · [PDF](https://arxiv.org/pdf/2512.09908.pdf)  
**作者**：Antonio Lorenzin, Fabio Zanasi  

**一句话要点**：提出范畴框架以建模贝叶斯网络与马尔可夫网络间的道德化和三角化变换

**关键词**：概率图模型, 范畴论, 道德化, 三角化, 变量消除, 语法语义区分

## 3 点简述
- 核心问题：道德化和三角化作为概率图模型间的变换，缺乏统一理论框架
- 方法要点：将网络表示为函子，通过函子前复合定义变换，区分语法与语义
- 实验或效果：重新解释变量消除算法为函子，分割三角化过程为纯语法和纯语义部分

## 摘要（原文）

> Moralisation and Triangulation are transformations allowing to switch between different ways of factoring a probability distribution into a graphical model. Moralisation allows to view a Bayesian network (a directed model) as a Markov network (an undirected model), whereas triangulation addresses the opposite direction. We present a categorical framework where these transformations are modelled as functors between a category of Bayesian networks and one of Markov networks. The two kinds of network (the objects of these categories) are themselves represented as functors from a `syntax' domain to a `semantics' codomain. Notably, moralisation and triangulation can be defined inductively on such syntax via functor pre-composition. Moreover, while moralisation is fully syntactic, triangulation relies on semantics. This leads to a discussion of the variable elimination algorithm, reinterpreted here as a functor in its own right, that splits the triangulation procedure in two: one purely syntactic, the other purely semantic. This approach introduces a functorial perspective into the theory of probabilistic graphical models, which highlights the distinctions between syntactic and semantic modifications.


---
layout: default
title: Mining Generalizable Activation Functions
---

# Mining Generalizable Activation Functions
**arXiv**：[2602.05688v1](https://arxiv.org/abs/2602.05688) · [PDF](https://arxiv.org/pdf/2602.05688.pdf)  
**作者**：Alex Vitvitskyi, Michael Boratko, Matej Grcic, Razvan Pascanu, Deep Shah, Petar Veličković  

**一句话要点**：提出基于AlphaEvolve的进化搜索框架，以发现具有泛化能力的激活函数

**关键词**：激活函数搜索, 进化算法, 归纳偏置, AlphaEvolve, 分布外泛化

## 3 点简述
- 核心问题：激活函数选择影响模型优化和归纳偏置，需提升泛化能力
- 方法要点：利用前沿LLM作为变异算子，在Python函数空间搜索，无需手动设计
- 实验或效果：通过分布外数据评估，小规模合成数据集可发现有效激活函数

## 摘要（原文）

> The choice of activation function is an active area of research, with different proposals aimed at improving optimization, while maintaining expressivity. Additionally, the activation function can significantly alter the implicit inductive bias of the architecture, controlling its non-linear behavior. In this paper, in line with previous work, we argue that evolutionary search provides a useful framework for finding new activation functions, while we also make two novel observations. The first is that modern pipelines, such as AlphaEvolve, which relies on frontier LLMs as a mutator operator, allows for a much wider and flexible search space; e.g., over all possible python functions within a certain FLOP budget, eliminating the need for manually constructed search spaces. In addition, these pipelines will be biased towards meaningful activation functions, given their ability to represent common knowledge, leading to a potentially more efficient search of the space. The second observation is that, through this framework, one can target not only performance improvements but also activation functions that encode particular inductive biases. This can be done by using performance on out-of-distribution data as a fitness function, reflecting the degree to which the architecture respects the inherent structure in the data in a manner independent of distribution shifts. We carry an empirical exploration of this proposal and show that relatively small scale synthetic datasets can be sufficient for AlphaEvolve to discover meaningful activations.


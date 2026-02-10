---
layout: default
title: TreeTensor: Boost AI System on Nested Data with Constrained Tree-Like Tensor
---

# TreeTensor: Boost AI System on Nested Data with Constrained Tree-Like Tensor
**arXiv**：[2602.08517v1](https://arxiv.org/abs/2602.08517) · [PDF](https://arxiv.org/pdf/2602.08517.pdf)  
**作者**：Shaoang Zhang, Yazhe Niu  

**一句话要点**：提出TreeTensor以解决嵌套数据在AI系统中编程不便与效率低下的问题。

**关键词**：嵌套数据, 树状张量, AI系统优化, 并行计算, 多模态数据处理

## 3 点简述
- 核心问题：传统张量处理嵌套数据时因固定形状导致编程不便和效率低下。
- 方法要点：通过约束树状结构建模数据关系，支持零成本应用任意函数和操作。
- 实验或效果：在AlphaStar等复杂系统中展示强大可用性和无开销的运行时效率。

## 摘要（原文）

> Tensor is the most basic and essential data structure of nowadays artificial intelligence (AI) system. The natural properties of Tensor, especially the memory-continuity and slice-independence, make it feasible for training system to leverage parallel computing unit like GPU to process data simultaneously in batch, spatial or temporal dimensions. However, if we look beyond perception tasks, the data in a complicated cognitive AI system usually has hierarchical structures (i.e. nested data) with various modalities. They are inconvenient and inefficient to program directly with conventional Tensor with fixed shape. To address this issue, we summarize two main computational patterns of nested data, and then propose a general nested data container: TreeTensor. Through various constraints and magic utilities of TreeTensor, one can apply arbitrary functions and operations to nested data with almost zero cost, including some famous machine learning libraries, such as Scikit-Learn, Numpy and PyTorch. Our approach utilizes a constrained tree-structure perspective to systematically model data relationships, and it can also easily be combined with other methods to extend more usages, such as asynchronous execution and variable-length data computation. Detailed examples and benchmarks show TreeTensor not only provides powerful usability in various problems, especially one of the most complicated AI systems at present: AlphaStar for StarCraftII, but also exhibits excellent runtime efficiency without any overhead. Our project is available at https://github.com/opendilab/DI-treetensor.


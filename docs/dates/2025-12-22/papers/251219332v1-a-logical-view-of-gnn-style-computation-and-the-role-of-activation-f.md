---
layout: default
title: A Logical View of GNN-Style Computation and the Role of Activation Functions
---

# A Logical View of GNN-Style Computation and the Role of Activation Functions
**arXiv**：[2512.19332v1](https://arxiv.org/abs/2512.19332) · [PDF](https://arxiv.org/pdf/2512.19332.pdf)  
**作者**：Pablo Barceló, Floris Geerts, Matthias Lanzinger, Klara Pakhomenko, Jan Van den Bussche  

**一句话要点**：提出MPLang语言以刻画图神经网络计算，分析激活函数对表达力的影响。

**关键词**：图神经网络, 表达力分析, 激活函数, 线性消息传递, 逻辑刻画

## 3 点简述
- 研究MPLang语言的数值与布尔表达力，聚焦线性消息传递和激活函数的作用。
- 证明有界激活函数在温和条件下表达力相同，并涵盖先前逻辑。
- 首次证明无界激活函数（如ReLU）在存在线性层时比有界激活函数表达力更强。

## 摘要（原文）

> We study the numerical and Boolean expressiveness of MPLang, a declarative language that captures the computation of graph neural networks (GNNs) through linear message passing and activation functions. We begin with A-MPLang, the fragment without activation functions, and give a characterization of its expressive power in terms of walk-summed features. For bounded activation functions, we show that (under mild conditions) all eventually constant activations yield the same expressive power - numerical and Boolean - and that it subsumes previously established logics for GNNs with eventually constant activation functions but without linear layers. Finally, we prove the first expressive separation between unbounded and bounded activations in the presence of linear layers: MPLang with ReLU is strictly more powerful for numerical queries than MPLang with eventually constant activation functions, e.g., truncated ReLU. This hinges on subtle interactions between linear aggregation and eventually constant non-linearities, and it establishes that GNNs using ReLU are more expressive than those restricted to eventually constant activations and linear layers.


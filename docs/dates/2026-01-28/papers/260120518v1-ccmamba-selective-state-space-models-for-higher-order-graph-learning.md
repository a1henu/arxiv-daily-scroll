---
layout: default
title: CCMamba: Selective State-Space Models for Higher-Order Graph Learning on Combinatorial Complexes
---

# CCMamba: Selective State-Space Models for Higher-Order Graph Learning on Combinatorial Complexes
**arXiv**：[2601.20518v1](https://arxiv.org/abs/2601.20518) · [PDF](https://arxiv.org/pdf/2601.20518.pdf)  
**作者**：Jiawen Chen, Qi Shao, Mingtong Zhou, Duxin Chen, Wenwu Yu  

**一句话要点**：提出CCMamba框架，基于选择性状态空间模型实现组合复形上的高效高阶图学习。

**关键词**：组合复形学习, 选择性状态空间模型, 高阶图神经网络, 拓扑深度学习, 线性复杂度

## 3 点简述
- 问题：现有拓扑深度学习方法依赖注意力机制，计算复杂度高且难以处理高阶复形中的秩感知信息聚合。
- 方法：将多秩关联关系组织为结构化序列，通过秩感知状态空间模型实现线性时间内的自适应、定向和长程信息传播。
- 效果：在多种基准测试中性能优于现有方法，并展现出更好的可扩展性和深度鲁棒性。

## 摘要（原文）

> Topological deep learning has emerged for modeling higher-order relational structures beyond pairwise interactions that standard graph neural networks fail to capture. Although combinatorial complexes offer a unified topological framework, most existing topological deep learning methods rely on local message passing via attention mechanisms, which incur quadratic complexity and remain low-dimensional, limiting scalability and rank-aware information aggregation in higher-order complexes.We propose Combinatorial Complex Mamba (CCMamba), the first unified mamba-based neural framework for learning on combinatorial complexes. CCMamba reformulates message passing as a selective state-space modeling problem by organizing multi-rank incidence relations into structured sequences processed by rank-aware state-space models. This enables adaptive, directional, and long range information propagation in linear time without self attention. We further establish the theoretical analysis that the expressive power upper-bound of CCMamba message passing is the 1-Weisfeiler-Lehman test. Experiments on graph, hypergraph, and simplicial benchmarks demonstrate that CCMamba consistently outperforms existing methods while exhibiting improved scalability and robustness to depth.


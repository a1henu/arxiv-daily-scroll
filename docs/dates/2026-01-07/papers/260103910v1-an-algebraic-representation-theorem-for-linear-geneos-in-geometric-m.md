---
layout: default
title: An Algebraic Representation Theorem for Linear GENEOs in Geometric Machine Learning
---

# An Algebraic Representation Theorem for Linear GENEOs in Geometric Machine Learning
**arXiv**：[2601.03910v1](https://arxiv.org/abs/2601.03910) · [PDF](https://arxiv.org/pdf/2601.03910.pdf)  
**作者**：Francesco Conti, Patrizio Frosini, Nicola Quercioli  

**一句话要点**：提出线性GENEOs在异构数据空间中的代数表示定理，基于广义T-置换测度

**关键词**：几何深度学习, 拓扑深度学习, 群等变算子, 表示定理, 异构数据处理, 自编码器优化

## 3 点简述
- 核心问题：现有线性GENEOs表示定理仅适用于同类型数据，无法处理异构数据空间的实际应用需求
- 方法要点：引入广义T-置换测度，在温和假设下完全表征作用于不同感知对的线性GENEOs，并证明其空间的紧致性与凸性
- 实验或效果：应用该框架提升自编码器性能，突显GENEOs在现代机器学习中的实用性

## 摘要（原文）

> Geometric and Topological Deep Learning are rapidly growing research areas that enhance machine learning through the use of geometric and topological structures. Within this framework, Group Equivariant Non-Expansive Operators (GENEOs) have emerged as a powerful class of operators for encoding symmetries and designing efficient, interpretable neural architectures. Originally introduced in Topological Data Analysis, GENEOs have since found applications in Deep Learning as tools for constructing equivariant models with reduced parameter complexity. GENEOs provide a unifying framework bridging Geometric and Topological Deep Learning and include the operator computing persistence diagrams as a special case. Their theoretical foundations rely on group actions, equivariance, and compactness properties of operator spaces, grounding them in algebra and geometry while enabling both mathematical rigor and practical relevance. While a previous representation theorem characterized linear GENEOs acting on data of the same type, many real-world applications require operators between heterogeneous data spaces. In this work, we address this limitation by introducing a new representation theorem for linear GENEOs acting between different perception pairs, based on generalized T-permutant measures. Under mild assumptions on the data domains and group actions, our result provides a complete characterization of such operators. We also prove the compactness and convexity of the space of linear GENEOs. We further demonstrate the practical impact of this theory by applying the proposed framework to improve the performance of autoencoders, highlighting the relevance of GENEOs in modern machine learning applications.


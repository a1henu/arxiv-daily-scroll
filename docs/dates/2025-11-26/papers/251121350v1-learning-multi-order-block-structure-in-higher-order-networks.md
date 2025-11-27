---
layout: default
title: Learning Multi-Order Block Structure in Higher-Order Networks
---

# Learning Multi-Order Block Structure in Higher-Order Networks
**arXiv**：[2511.21350v1](https://arxiv.org/abs/2511.21350) · [PDF](https://arxiv.org/pdf/2511.21350.pdf)  
**作者**：Kazuki Nakajima, Yuya Sasaki, Takeaki Uno, Masaki Aida  

**一句话要点**：提出多阶块结构框架以解决高阶网络中阶依赖结构建模问题

**关键词**：高阶网络, 超图建模, 随机块模型, 多阶结构, 预测性能, 可解释性

## 3 点简述
- 核心问题：单阶模型假设所有交互阶共享亲和模式，可能忽略阶依赖结构细节。
- 方法要点：引入多阶随机块模型，优化交互阶划分以最大化超链接预测性能。
- 实验或效果：在真实网络中，多阶结构普遍存在，提升预测性能与可解释性。

## 摘要（原文）

> Higher-order networks, naturally described as hypergraphs, are essential for modeling real-world systems involving interactions among three or more entities. Stochastic block models offer a principled framework for characterizing mesoscale organization, yet their extension to hypergraphs involves a trade-off between expressive power and computational complexity. A recent simplification, a single-order model, mitigates this complexity by assuming a single affinity pattern governs interactions of all orders. This universal assumption, however, may overlook order-dependent structural details. Here, we propose a framework that relaxes this assumption by introducing a multi-order block structure, in which different affinity patterns govern distinct subsets of interaction orders. Our framework is based on a multi-order stochastic block model and searches for the optimal partition of the set of interaction orders that maximizes out-of-sample hyperlink prediction performance. Analyzing a diverse range of real-world networks, we find that multi-order block structures are prevalent. Accounting for them not only yields better predictive performance over the single-order model but also uncovers sharper, more interpretable mesoscale organization. Our findings reveal that order-dependent mechanisms are a key feature of the mesoscale organization of real-world higher-order networks.


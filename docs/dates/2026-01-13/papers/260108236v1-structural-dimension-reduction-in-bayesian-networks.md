---
layout: default
title: Structural Dimension Reduction in Bayesian Networks
---

# Structural Dimension Reduction in Bayesian Networks
**arXiv**：[2601.08236v1](https://arxiv.org/abs/2601.08236) · [PDF](https://arxiv.org/pdf/2601.08236.pdf)  
**作者**：Pei Heng, Yi Sun, Jianhua Guo  

**一句话要点**：提出结构降维技术，通过有向凸壳将贝叶斯网络压缩为最小局部网络，保持概率推断一致性。

**关键词**：贝叶斯网络, 结构降维, 有向凸壳, 概率推断, 多项式时间算法, 网络压缩

## 3 点简述
- 核心问题：如何在贝叶斯网络中实现高效降维，同时确保概率推断结果与原网络一致。
- 方法要点：引入有向凸壳作为组合结构，等价于最小局部贝叶斯网络，并设计多项式时间算法识别。
- 实验或效果：在真实网络中展示高降维能力，基于有向凸壳的推断效率显著优于变量消除和信念传播等传统方法。

## 摘要（原文）

> This work introduces a novel technique, named structural dimension reduction, to collapse a Bayesian network onto a minimum and localized one while ensuring that probabilistic inferences between the original and reduced networks remain consistent. To this end, we propose a new combinatorial structure in directed acyclic graphs called the directed convex hull, which has turned out to be equivalent to their minimum localized Bayesian networks. An efficient polynomial-time algorithm is devised to identify them by determining the unique directed convex hulls containing the variables of interest from the original networks. Experiments demonstrate that the proposed technique has high dimension reduction capability in real networks, and the efficiency of probabilistic inference based on directed convex hulls can be significantly improved compared with traditional methods such as variable elimination and belief propagation algorithms. The code of this study is open at \href{https://github.com/Balance-H/Algorithms}{https://github.com/Balance-H/Algorithms} and the proofs of the results in the main body are postponed to the appendix.


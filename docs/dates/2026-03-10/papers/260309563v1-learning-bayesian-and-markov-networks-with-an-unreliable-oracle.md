---
layout: default
title: Learning Bayesian and Markov Networks with an Unreliable Oracle
---

# Learning Bayesian and Markov Networks with an Unreliable Oracle
**arXiv**：[2603.09563v1](https://arxiv.org/abs/2603.09563) · [PDF](https://arxiv.org/pdf/2603.09563.pdf)  
**作者**：Juha Harviainen, Pekka Parviainen, Vidya Sagar Sharma  

**一句话要点**：研究不可靠条件独立性预言机下的贝叶斯与马尔可夫网络结构学习

**关键词**：贝叶斯网络, 马尔可夫网络, 结构学习, 条件独立性, 图参数, 错误容忍

## 3 点简述
- 核心问题：在条件独立性预言机最多有界错误下，学习贝叶斯和马尔可夫网络结构
- 方法要点：分析图参数对结构可识别性的影响，并给出可识别时的算法
- 实验或效果：证明马尔可夫网络可容忍指数级错误，而贝叶斯网络无法容忍任何错误

## 摘要（原文）

> We study constraint-based structure learning of Markov networks and Bayesian networks in the presence of an unreliable conditional independence oracle that makes at most a bounded number of errors. For Markov networks, we observe that a low maximum number of vertex-wise disjoint paths implies that the structure is uniquely identifiable even if the number of errors is (moderately) exponential in the number of vertices. For Bayesian networks, however, we prove that one cannot tolerate any errors to always identify the structure even when many commonly used graph parameters like treewidth are bounded. Finally, we give algorithms for structure learning when the structure is uniquely identifiable.


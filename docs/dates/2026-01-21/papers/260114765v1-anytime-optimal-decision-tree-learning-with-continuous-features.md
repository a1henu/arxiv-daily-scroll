---
layout: default
title: Anytime Optimal Decision Tree Learning with Continuous Features
---

# Anytime Optimal Decision Tree Learning with Continuous Features
**arXiv**：[2601.14765v1](https://arxiv.org/abs/2601.14765) · [PDF](https://arxiv.org/pdf/2601.14765.pdf)  
**作者**：Harold Kiossou, Pierre Schaus, Siegfried Nijssen  

**一句话要点**：提出基于有限差异搜索的任意时间最优决策树学习方法，以解决连续特征下深度优先搜索的任意时间性能差问题。

**关键词**：最优决策树学习, 连续特征处理, 有限差异搜索, 任意时间算法, 计算优化

## 3 点简述
- 核心问题：现有最优决策树方法在连续特征下计算时间增长快，深度优先搜索导致任意时间中断时解质量低。
- 方法要点：采用有限差异搜索策略，均匀分配计算资源，确保任意中断点都能获得高质量决策树。
- 实验或效果：实验显示，该方法在任意时间性能上优于现有方法，提升中断时的解质量。

## 摘要（原文）

> In recent years, significant progress has been made on algorithms for learning optimal decision trees, primarily in the context of binary features. Extending these methods to continuous features remains substantially more challenging due to the large number of potential splits for each feature. Recently, an elegant exact algorithm was proposed for learning optimal decision trees with continuous features; however, the rapidly increasing computational time limits its practical applicability to shallow depths (typically 3 or 4). It relies on a depth-first search optimization strategy that fully optimizes the left subtree of each split before exploring the corresponding right subtree. While effective in finding optimal solutions given sufficient time, this strategy can lead to poor anytime behavior: when interrupted early, the best-found tree is often highly unbalanced and suboptimal. In such cases, purely greedy methods such as C4.5 may, paradoxically, yield better solutions. To address this limitation, we propose an anytime, yet complete approach leveraging limited discrepancy search, distributing the computational effort more evenly across the entire tree structure, and thus ensuring that a high-quality decision tree is available at any interruption point. Experimental results show that our approach outperforms the existing one in terms of anytime performance.


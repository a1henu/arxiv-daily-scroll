---
layout: default
title: Coarsening Causal DAG Models
---

# Coarsening Causal DAG Models
**arXiv**：[2601.10531v1](https://arxiv.org/abs/2601.10531) · [PDF](https://arxiv.org/pdf/2601.10531.pdf)  
**作者**：Francisco Madaleno, Pratik Misra, Alex Markham  

**一句话要点**：提出抽象因果图学习算法，解决干预数据中未知目标的因果模型粗化问题。

**关键词**：因果抽象, 因果发现, 干预数据, 图模型, 算法学习

## 3 点简述
- 核心问题：在干预数据中，当干预目标未知时，如何从给定特征粒度直接学习抽象因果图。
- 方法要点：提供图形可识别性结果，设计高效一致算法，并分析搜索空间的格结构理论。
- 实验或效果：在合成和真实数据集（如光强与偏振交互系统）上验证算法，与已知真实情况对比。

## 摘要（原文）

> Directed acyclic graphical (DAG) models are a powerful tool for representing causal relationships among jointly distributed random variables, especially concerning data from across different experimental settings. However, it is not always practical or desirable to estimate a causal model at the granularity of given features in a particular dataset. There is a growing body of research on causal abstraction to address such problems. We contribute to this line of research by (i) providing novel graphical identifiability results for practically-relevant interventional settings, (ii) proposing an efficient, provably consistent algorithm for directly learning abstract causal graphs from interventional data with unknown intervention targets, and (iii) uncovering theoretical insights about the lattice structure of the underlying search space, with connections to the field of causal discovery more generally. As proof of concept, we apply our algorithm on synthetic and real datasets with known ground truths, including measurements from a controlled physical system with interacting light intensity and polarization.


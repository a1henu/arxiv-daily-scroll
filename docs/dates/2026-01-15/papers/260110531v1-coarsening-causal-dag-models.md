---
layout: default
title: Coarsening Causal DAG Models
---

# Coarsening Causal DAG Models
**arXiv**：[2601.10531v1](https://arxiv.org/abs/2601.10531) · [PDF](https://arxiv.org/pdf/2601.10531.pdf)  
**作者**：Francisco Madaleno, Pratik Misra, Alex Markham  

**一句话要点**：提出基于干预数据的抽象因果图学习算法，解决因果模型粒度粗化问题。

**关键词**：因果抽象, 因果图学习, 干预数据, 图形可识别性, 算法一致性

## 3 点简述
- 核心问题：因果模型在给定特征粒度下估计不切实际，需粗化表示。
- 方法要点：提供图形可识别性结果，提出高效一致算法学习抽象因果图。
- 实验或效果：在合成和真实数据集上验证，包括光强与偏振交互的物理系统。

## 摘要（原文）

> Directed acyclic graphical (DAG) models are a powerful tool for representing causal relationships among jointly distributed random variables, especially concerning data from across different experimental settings. However, it is not always practical or desirable to estimate a causal model at the granularity of given features in a particular dataset. There is a growing body of research on causal abstraction to address such problems. We contribute to this line of research by (i) providing novel graphical identifiability results for practically-relevant interventional settings, (ii) proposing an efficient, provably consistent algorithm for directly learning abstract causal graphs from interventional data with unknown intervention targets, and (iii) uncovering theoretical insights about the lattice structure of the underlying search space, with connections to the field of causal discovery more generally. As proof of concept, we apply our algorithm on synthetic and real datasets with known ground truths, including measurements from a controlled physical system with interacting light intensity and polarization.


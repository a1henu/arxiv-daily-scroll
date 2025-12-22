---
layout: default
title: Bayesian Optimisation: Which Constraints Matter?
---

# Bayesian Optimisation: Which Constraints Matter?
**arXiv**：[2512.17569v1](https://arxiv.org/abs/2512.17569) · [PDF](https://arxiv.org/pdf/2512.17569.pdf)  
**作者**：Xietao Wang Lin, Juan Ungredda, Max Butler, James Town, Alma Rahat, Hemant Singh, Juergen Branke  

**一句话要点**：提出基于知识梯度的贝叶斯优化变体，用于解耦黑盒约束优化问题。

**关键词**：贝叶斯优化, 解耦约束, 知识梯度, 黑盒优化, 全局优化

## 3 点简述
- 核心问题：解耦黑盒约束优化中，仅少数约束在最优解处有效，需高效评估。
- 方法要点：扩展知识梯度采集函数，优先评估相关约束，减少不必要计算。
- 实验或效果：实证基准测试显示优于现有方法，提升优化效率。

## 摘要（原文）

> Bayesian optimisation has proven to be a powerful tool for expensive global black-box optimisation problems. In this paper, we propose new Bayesian optimisation variants of the popular Knowledge Gradient acquisition functions for problems with \emph{decoupled} black-box constraints, in which subsets of the objective and constraint functions may be evaluated independently. In particular, our methods aim to take into account that often only a handful of the constraints may be binding at the optimum, and hence we should evaluate only relevant constraints when trying to optimise a function. We empirically benchmark these methods against existing methods and demonstrate their superiority over the state-of-the-art.


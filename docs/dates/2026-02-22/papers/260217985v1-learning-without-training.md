---
layout: default
title: Learning Without Training
---

# Learning Without Training
**arXiv**：[2602.17985v1](https://arxiv.org/abs/2602.17985) · [PDF](https://arxiv.org/pdf/2602.17985.pdf)  
**作者**：Ryan O'Dowd  

**一句话要点**：提出基于数学理论的机器学习方法，涵盖监督学习、迁移学习和主动学习分类任务。

**关键词**：监督学习, 迁移学习, 主动学习, 函数逼近, 信号分离, 数学理论

## 3 点简述
- 核心问题：监督学习中函数逼近的理论缺陷，迁移学习中跨域函数提升的可行性，以及分类任务中信号分离技术的应用。
- 方法要点：引入新方法改进监督学习范式，研究函数提升的局部平滑性关系，提出统一信号分离与分类的理论及快速算法。
- 实验或效果：新算法在主动学习中达到竞争性准确度，且计算速度显著更快。

## 摘要（原文）

> Machine learning is at the heart of managing the real-world problems associated with massive data. With the success of neural networks on such large-scale problems, more research in machine learning is being conducted now than ever before. This dissertation focuses on three different projects rooted in mathematical theory for machine learning applications.
>   The first project deals with supervised learning and manifold learning. In theory, one of the main problems in supervised learning is that of function approximation: that is, given some data set $\mathcal{D}=\{(x_j,f(x_j))\}_{j=1}^M$, can one build a model $F\approx f$? We introduce a method which aims to remedy several of the theoretical shortcomings of the current paradigm for supervised learning.
>   The second project deals with transfer learning, which is the study of how an approximation process or model learned on one domain can be leveraged to improve the approximation on another domain. We study such liftings of functions when the data is assumed to be known only on a part of the whole domain. We are interested in determining subsets of the target data space on which the lifting can be defined, and how the local smoothness of the function and its lifting are related.
>   The third project is concerned with the classification task in machine learning, particularly in the active learning paradigm. Classification has often been treated as an approximation problem as well, but we propose an alternative approach leveraging techniques originally introduced for signal separation problems. We introduce theory to unify signal separation with classification and a new algorithm which yields competitive accuracy to other recent active learning algorithms while providing results much faster.


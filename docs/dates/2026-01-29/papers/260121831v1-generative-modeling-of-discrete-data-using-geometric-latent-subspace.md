---
layout: default
title: Generative Modeling of Discrete Data Using Geometric Latent Subspaces
---

# Generative Modeling of Discrete Data Using Geometric Latent Subspaces
**arXiv**：[2601.21831v1](https://arxiv.org/abs/2601.21831) · [PDF](https://arxiv.org/pdf/2601.21831.pdf)  
**作者**：Daniel Gonzalez-Alvarado, Jonas Cassel, Stefania Petra, Christoph Schnörr  

**一句话要点**：提出在分类分布乘积流形的指数参数空间中使用潜在子空间，以学习离散数据的生成模型。

**关键词**：离散数据生成, 潜在子空间, 黎曼几何, 流匹配, 分类分布, 生成模型

## 3 点简述
- 核心问题：离散数据生成建模中，分类变量间存在统计依赖和冗余自由度，需高效编码。
- 方法要点：引入黎曼几何，使参数域具有等距性，实现一致流匹配，将测地线变为直线。
- 实验或效果：实证表明，低维潜在空间足以表示数据，支持有效生成建模。

## 摘要（原文）

> We introduce the use of latent subspaces in the exponential parameter space of product manifolds of categorial distributions, as a tool for learning generative models of discrete data. The low-dimensional latent space encodes statistical dependencies and removes redundant degrees of freedom among the categorial variables. We equip the parameter domain with a Riemannian geometry such that the spaces and distances are related by isometries which enables consistent flow matching. In particular, geodesics become straight lines which makes model training by flow matching effective. Empirical results demonstrate that reduced latent dimensions suffice to represent data for generative modeling.


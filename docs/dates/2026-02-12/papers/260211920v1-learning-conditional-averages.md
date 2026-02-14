---
layout: default
title: Learning Conditional Averages
---

# Learning Conditional Averages
**arXiv**：[2602.11920v1](https://arxiv.org/abs/2602.11920) · [PDF](https://arxiv.org/pdf/2602.11920.pdf)  
**作者**：Marco Bressan, Nataly Brukhim, Nicolo Cesa-Bianchi, Emmanuel Esposito, Yishay Mansour, Shay Moran, Maximilian Thiessen  

**一句话要点**：提出学习条件平均问题，在PAC框架中刻画可学习性并给出样本复杂度界。

**关键词**：条件平均学习, PAC学习, 可学习性刻画, 样本复杂度, 邻域系统, 组合参数

## 3 点简述
- 核心问题：在PAC学习中预测实例邻域的平均标签，而非目标概念本身。
- 方法要点：基于概念类和邻域系统定义新组合参数，完全刻画可学习性条件。
- 实验或效果：样本复杂度界紧至对数因子，适用于可解释性、公平性等场景。

## 摘要（原文）

> We introduce the problem of learning conditional averages in the PAC framework. The learner receives a sample labeled by an unknown target concept from a known concept class, as in standard PAC learning. However, instead of learning the target concept itself, the goal is to predict, for each instance, the average label over its neighborhood -- an arbitrary subset of points that contains the instance. In the degenerate case where all neighborhoods are singletons, the problem reduces exactly to classic PAC learning. More generally, it extends PAC learning to a setting that captures learning tasks arising in several domains, including explainability, fairness, and recommendation systems. Our main contribution is a complete characterization of when conditional averages are learnable, together with sample complexity bounds that are tight up to logarithmic factors. The characterization hinges on the joint finiteness of two novel combinatorial parameters, which depend on both the concept class and the neighborhood system, and are closely related to the independence number of the associated neighborhood graph.


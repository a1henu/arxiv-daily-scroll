---
layout: default
title: Multi-domain performance analysis with scores tailored to user preferences
---

# Multi-domain performance analysis with scores tailored to user preferences
**arXiv**：[2512.08715v1](https://arxiv.org/abs/2512.08715) · [PDF](https://arxiv.org/pdf/2512.08715.pdf)  
**作者**：Sébastien Piérard, Adrien Deliège, Marc Van Droogenbroeck  

**一句话要点**：提出基于用户偏好多域性能分析方法，定义关键域并开发可视化工具

**关键词**：多域性能分析, 用户偏好评分, 加权平均, 概率框架, 二分类可视化

## 3 点简述
- 核心问题：算法性能依赖应用域分布，需多域评估与加权平均分析
- 方法要点：采用概率框架，识别满足加权算术平均的评分族，定义四种关键域
- 实验或效果：针对二分类任务开发新可视化工具，支持性能分析

## 摘要（原文）

> The performance of algorithms, methods, and models tends to depend heavily on the distribution of cases on which they are applied, this distribution being specific to the applicative domain. After performing an evaluation in several domains, it is highly informative to compute a (weighted) mean performance and, as shown in this paper, to scrutinize what happens during this averaging. To achieve this goal, we adopt a probabilistic framework and consider a performance as a probability measure (e.g., a normalized confusion matrix for a classification task). It appears that the corresponding weighted mean is known to be the summarization, and that only some remarkable scores assign to the summarized performance a value equal to a weighted arithmetic mean of the values assigned to the domain-specific performances. These scores include the family of ranking scores, a continuum parameterized by user preferences, and that the weights to consider in the arithmetic mean depend on the user preferences. Based on this, we rigorously define four domains, named easiest, most difficult, preponderant, and bottleneck domains, as functions of user preferences. After establishing the theory in a general setting, regardless of the task, we develop new visual tools for two-class classification.


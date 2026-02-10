---
layout: default
title: Positive Distribution Shift as a Framework for Understanding Tractable Learning
---

# Positive Distribution Shift as a Framework for Understanding Tractable Learning
**arXiv**：[2602.08907v1](https://arxiv.org/abs/2602.08907) · [PDF](https://arxiv.org/pdf/2602.08907.pdf)  
**作者**：Marko Medvedev, Idan Attias, Elisabetta Cornacchia, Theodor Misiakiewicz, Gal Vardi, Nathan Srebro  

**一句话要点**：提出正分布偏移框架，通过优化训练分布使学习更易处理

**关键词**：分布偏移, 正分布偏移, 计算复杂性, 梯度训练, 成员查询学习

## 3 点简述
- 研究在目标分布与训练分布不同的情况下学习目标函数的问题
- 论证通过精心选择训练分布，分布偏移可带来计算上的益处而非统计损失
- 形式化正分布偏移变体，展示其使某些难学类变得易学

## 摘要（原文）

> We study a setting where the goal is to learn a target function f(x) with respect to a target distribution D(x), but training is done on i.i.d. samples from a different training distribution D'(x), labeled by the true target f(x). Such a distribution shift (here in the form of covariate shift) is usually viewed negatively, as hurting or making learning harder, and the traditional distribution shift literature is mostly concerned with limiting or avoiding this negative effect. In contrast, we argue that with a well-chosen D'(x), the shift can be positive and make learning easier -- a perspective called Positive Distribution Shift (PDS). Such a perspective is central to contemporary machine learning, where much of the innovation is in finding good training distributions D'(x), rather than changing the training algorithm. We further argue that the benefit is often computational rather than statistical, and that PDS allows computationally hard problems to become tractable even using standard gradient-based training. We formalize different variants of PDS, show how certain hard classes are easily learnable under PDS, and make connections with membership query learning.


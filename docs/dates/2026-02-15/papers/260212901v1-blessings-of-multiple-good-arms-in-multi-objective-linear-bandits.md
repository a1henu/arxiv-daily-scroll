---
layout: default
title: Blessings of Multiple Good Arms in Multi-Objective Linear Bandits
---

# Blessings of Multiple Good Arms in Multi-Objective Linear Bandits
**arXiv**：[2602.12901v1](https://arxiv.org/abs/2602.12901) · [PDF](https://arxiv.org/pdf/2602.12901.pdf)  
**作者**：Heesang Ann, Min-hwan Oh  

**一句话要点**：提出多目标线性赌博机中多好臂的隐式探索优势，以简化算法设计

**关键词**：多目标赌博机, 隐式探索, 线性赌博机, 帕累托公平, 贪婪算法, 无分布假设

## 3 点简述
- 核心问题：多目标赌博机传统上被视为复杂，需同时优化多个目标
- 方法要点：当存在多个好臂时，可诱导隐式探索，使贪婪算法在多数轮次中表现优异
- 实验或效果：理论证明和实证验证了算法性能，无需上下文分布假设

## 摘要（原文）

> The multi objective bandit setting has traditionally been regarded as more complex than the single objective case, as multiple objectives must be optimized simultaneously. In contrast to this prevailing view, we demonstrate that when multiple good arms exist for multiple objectives, they can induce a surprising benefit, implicit exploration. Under this condition, we show that simple algorithms that greedily select actions in most rounds can nonetheless achieve strong performance, both theoretically and empirically. To our knowledge, this is the first study to introduce implicit exploration in both multi objective and parametric bandit settings without any distributional assumptions on the contexts. We further introduce a framework for effective Pareto fairness, which provides a principled approach to rigorously analyzing fairness of multi objective bandit algorithms.


---
layout: default
title: Generational Replacement and Learning for High-Performing and Diverse Populations in Evolvable Robots
---

# Generational Replacement and Learning for High-Performing and Diverse Populations in Evolvable Robots
**arXiv**：[2601.03807v1](https://arxiv.org/abs/2601.03807) · [PDF](https://arxiv.org/pdf/2601.03807.pdf)  
**作者**：K. Ege de Bruin, Kyrre Glette, Kai Olav Ellefsen  

**一句话要点**：结合全代替换与个体内学习以提升演化机器人种群多样性与性能

**关键词**：演化机器人, 形态控制器协同优化, 种群多样性, 个体内学习, 全代替换, 性能评估

## 3 点简述
- 核心问题：演化机器人中形态与控制器协同优化困难，新设计难以进入种群，且种群多样性易丧失。
- 方法要点：引入全代替换策略增加多样性，结合个体内学习优化控制器以维持性能。
- 实验或效果：实验表明该方法能同时提升多样性和性能，并强调性能评估指标对结论的影响。

## 摘要（原文）

> Evolutionary Robotics offers the possibility to design robots to solve a specific task automatically by optimizing their morphology and control together. However, this co-optimization of body and control is challenging, because controllers need some time to adapt to the evolving morphology - which may make it difficult for new and promising designs to enter the evolving population. A solution to this is to add intra-life learning, defined as an additional controller optimization loop, to each individual in the evolving population. A related problem is the lack of diversity often seen in evolving populations as evolution narrows the search down to a few promising designs too quickly. This problem can be mitigated by implementing full generational replacement, where offspring robots replace the whole population. This solution for increasing diversity usually comes at the cost of lower performance compared to using elitism. In this work, we show that combining such generational replacement with intra-life learning can increase diversity while retaining performance. We also highlight the importance of performance metrics when studying learning in morphologically evolving robots, showing that evaluating according to function evaluations versus according to generations of evolution can give different conclusions.


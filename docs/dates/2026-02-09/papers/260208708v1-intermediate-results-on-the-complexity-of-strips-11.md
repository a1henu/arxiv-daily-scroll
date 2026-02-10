---
layout: default
title: Intermediate Results on the Complexity of STRIPS$_{1}^{1}$
---

# Intermediate Results on the Complexity of STRIPS$_{1}^{1}$
**arXiv**：[2602.08708v1](https://arxiv.org/abs/2602.08708) · [PDF](https://arxiv.org/pdf/2602.08708.pdf)  
**作者**：Stefan Edelkamp, Jiří Fink, Petr Gregor, Anders Jonsson, Bernhard Nebel  

**一句话要点**：探究STRIPS$^1_1$规划问题的小解假设，通过SAT求解器、字面图与Petri网映射分析其计算复杂性。

**关键词**：STRIPS规划, 计算复杂性, NP完全性, 字面图, Petri网, SAT求解器

## 3 点简述
- 核心问题：命题STRIPS规划中，操作符仅含一个前提和一个效果时，其规划存在性是否为NP完全问题。
- 方法要点：引入字面图表示规划结构，并将其映射到Petri网以分析复杂性。
- 实验或效果：调用SAT求解器处理小规模实例，为小解假设提供实证支持。

## 摘要（原文）

> This paper is based on Bylander's results on the computational complexity of propositional STRIPS planning. He showed that when only ground literals are permitted, determining plan existence is PSPACE-complete even if operators are limited to two preconditions and two postconditions. While NP-hardness is settled, it is unknown whether propositional STRIPS with operators that only have one precondition and one effect is NP-complete. We shed light on the question whether this small solution hypothesis for STRIPS$^1_1$ is true, calling a SAT solver for small instances, introducing the literal graph, and mapping it to Petri nets.


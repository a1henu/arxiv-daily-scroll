---
layout: default
title: Neural Network Approximation: A View from Polytope Decomposition
---

# Neural Network Approximation: A View from Polytope Decomposition
**arXiv**：[2601.18264v1](https://arxiv.org/abs/2601.18264) · [PDF](https://arxiv.org/pdf/2601.18264.pdf)  
**作者**：ZeYu Li, ShiJun Zhang, TieYong Zeng, FengLei Fan  

**一句话要点**：提出基于多面体分解的ReLU网络通用逼近方法，提升目标函数局部奇点处的逼近效率。

**关键词**：通用逼近理论, ReLU网络, 多面体分解, 核多项式方法, 函数逼近, 奇点处理

## 3 点简述
- 核心问题：现有逼近理论忽略目标函数局部正则性，导致逼近效率不足。
- 方法要点：通过多面体分解和核多项式方法，构建ReLU网络在子域中分别逼近连续函数。
- 实验或效果：方法在函数奇点附近更高效灵活，并扩展至解析函数实现更高逼近率。

## 摘要（原文）

> Universal approximation theory offers a foundational framework to verify neural network expressiveness, enabling principled utilization in real-world applications. However, most existing theoretical constructions are established by uniformly dividing the input space into tiny hypercubes without considering the local regularity of the target function. In this work, we investigate the universal approximation capabilities of ReLU networks from a view of polytope decomposition, which offers a more realistic and task-oriented approach compared to current methods. To achieve this, we develop an explicit kernel polynomial method to derive an universal approximation of continuous functions, which is characterized not only by the refined Totik-Ditzian-type modulus of continuity, but also by polytopical domain decomposition. Then, a ReLU network is constructed to approximate the kernel polynomial in each subdomain separately. Furthermore, we find that polytope decomposition makes our approximation more efficient and flexible than existing methods in many cases, especially near singular points of the objective function. Lastly, we extend our approach to analytic functions to reach a higher approximation rate.


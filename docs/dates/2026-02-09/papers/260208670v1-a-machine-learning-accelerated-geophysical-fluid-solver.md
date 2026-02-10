---
layout: default
title: A Machine Learning accelerated geophysical fluid solver
---

# A Machine Learning accelerated geophysical fluid solver
**arXiv**：[2602.08670v1](https://arxiv.org/abs/2602.08670) · [PDF](https://arxiv.org/pdf/2602.08670.pdf)  
**作者**：Yang Bai  

**一句话要点**：提出基于数据驱动离散化的机器学习加速流体求解器，用于浅水方程和欧拉方程求解。

**关键词**：机器学习加速求解器, 数据驱动离散化, 偏微分方程求解, 浅水方程, 欧拉方程, 结构化网格

## 3 点简述
- 核心问题：机器学习在数学约束领域如偏微分方程求解中的应用方法尚不明确。
- 方法要点：采用数据驱动离散化方法，预测准线性模板系数以加速和改进结构化网格上的求解器。
- 实验或效果：实现经典求解器优于Pyclaw，四种深度神经网络中两种能输出满意解。

## 摘要（原文）

> Machine learning methods have been successful in many areas, like image classification and natural language processing. However, it still needs to be determined how to apply ML to areas with mathematical constraints, like solving PDEs. Among various approaches to applying ML techniques to solving PDEs, the data-driven discretization method presents a promising way of accelerating and improving existing PDE solver on structured grids where it predicts the coefficients of quasi-linear stencils for computing values or derivatives of a function at given positions. It can improve the accuracy and stability of low-resolution simulation compared with using traditional finite difference or finite volume schemes. Meanwhile, it can also benefit from traditional numerical schemes like achieving conservation law by adapting finite volume type formulations. In this thesis, we have implemented the shallow water equation and Euler equation classic solver under a different framework. Experiments show that our classic solver performs much better than the Pyclaw solver. Then we propose four different deep neural networks for the ML-based solver. The results indicate that two of these approaches could output satisfactory solutions.


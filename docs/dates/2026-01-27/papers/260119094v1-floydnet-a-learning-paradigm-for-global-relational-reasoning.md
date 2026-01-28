---
layout: default
title: FloydNet: A Learning Paradigm for Global Relational Reasoning
---

# FloydNet: A Learning Paradigm for Global Relational Reasoning
**arXiv**：[2601.19094v1](https://arxiv.org/abs/2601.19094) · [PDF](https://arxiv.org/pdf/2601.19094.pdf)  
**作者**：Jingcheng Yu, Mingliang Zeng, Qiwei Ye  

**一句话要点**：提出FloydNet学习范式，通过动态编程式全局关系张量精炼，解决图神经网络全局推理瓶颈问题。

**关键词**：图神经网络, 动态编程, 全局推理, 关系张量, 算法基准, 表达能力

## 3 点简述
- 核心问题：图神经网络的消息传递机制存在局部瓶颈，限制全局推理能力。
- 方法要点：FloydNet维护全局全对关系张量，学习广义动态编程算子进行迭代精炼。
- 实验或效果：在CLRS-30基准上接近完美分数，显著提升旅行商问题求解率，匹配3-WL表达能力。

## 摘要（原文）

> Developing models capable of complex, multi-step reasoning is a central goal in artificial intelligence. While representing problems as graphs is a powerful approach, Graph Neural Networks (GNNs) are fundamentally constrained by their message-passing mechanism, which imposes a local bottleneck that limits global, holistic reasoning. We argue that dynamic programming (DP), which solves problems by iteratively refining a global state, offers a more powerful and suitable learning paradigm. We introduce FloydNet, a new architecture that embodies this principle. In contrast to local message passing, FloydNet maintains a global, all-pairs relationship tensor and learns a generalized DP operator to progressively refine it. This enables the model to develop a task-specific relational calculus, providing a principled framework for capturing long-range dependencies. Theoretically, we prove that FloydNet achieves 3-WL (2-FWL) expressive power, and its generalized form aligns with the k-FWL hierarchy. FloydNet demonstrates state-of-the-art performance across challenging domains: it achieves near-perfect scores (often >99\%) on the CLRS-30 algorithmic benchmark, finds exact optimal solutions for the general Traveling Salesman Problem (TSP) at rates significantly exceeding strong heuristics, and empirically matches the 3-WL test on the BREC benchmark. Our results establish this learned, DP-style refinement as a powerful and practical alternative to message passing for high-level graph reasoning.


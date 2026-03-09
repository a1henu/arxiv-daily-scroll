---
layout: default
title: A Unified Low-Dimensional Design Embedding for Joint Optimization of Shape, Material, and Actuation in Soft Robots
---

# A Unified Low-Dimensional Design Embedding for Joint Optimization of Shape, Material, and Actuation in Soft Robots
**arXiv**：[2603.06497v1](https://arxiv.org/abs/2603.06497) · [PDF](https://arxiv.org/pdf/2603.06497.pdf)  
**作者**：Vittorio Candiello, Manuel Mekkattu, Mike Y. Michelis, Robert K. Katzschmann  

**一句话要点**：提出统一低维设计嵌入，以联合优化软机器人的形状、材料和驱动

**关键词**：软机器人设计, 协同优化, 低维嵌入, 形状材料驱动联合, 计算力学, 设计空间结构化

## 3 点简述
- 核心问题：软机器人设计需联合考虑几何、材料和驱动，但计算挑战大，如非线性力学和梯度方法限制
- 方法要点：通过共享基函数构建平滑低维嵌入，统一形状变形、多材料分布和驱动参数化
- 实验或效果：在动态任务中超越神经网络和体素基线，使用更少参数实现高效协同设计

## 摘要（原文）

> Soft robots achieve functionality through tight coupling among geometry, material composition, and actuation. As a result, effective design optimization requires these three aspects to be considered jointly rather than in isolation. This coupling is computationally challenging: nonlinear large-deformation mechanics increase simulation cost, while contact, collision handling, and non-smooth state transitions limit the applicability of standard gradient-based approaches. We introduce a smooth, low-dimensional design embedding for soft robots that unifies shape morphing, multi-material distribution, and actuation within a single structured parameter space. Shape variation is modeled through continuous deformation maps of a reference geometry, while material properties are encoded as spatial fields. Both are constructed from shared basis functions. This representation enables expressive co-design while drastically reducing the dimensionality of the search space. In our experiments, we show that design expressiveness increases with the number of basis functions, unlike comparable neural network encodings whose representational capacity does not scale predictably with parameter count. We further show that joint co-optimization of shape, material, and actuation using our unified embedding consistently outperforms sequential strategies. All experiments are performed independently of the underlying simulator, confirming compatibility with black-box simulation pipelines. Across multiple dynamic tasks, the proposed embedding surpasses neural network and voxel-based baseline parameterizations while using significantly fewer design parameters. Together, these findings demonstrate that structuring the design space itself enables efficient co-design of soft robots.


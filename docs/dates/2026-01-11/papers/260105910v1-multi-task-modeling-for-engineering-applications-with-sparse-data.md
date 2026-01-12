---
layout: default
title: Multi-task Modeling for Engineering Applications with Sparse Data
---

# Multi-task Modeling for Engineering Applications with Sparse Data
**arXiv**：[2601.05910v1](https://arxiv.org/abs/2601.05910) · [PDF](https://arxiv.org/pdf/2601.05910.pdf)  
**作者**：Yigitcan Comlek, R. Murali Krishnan, Sandipp Krishnan Ravi, Amin Moghaddas, Rafael Giorjao, Michael Eff, Anirban Samaddar, Nesar S. Ramachandra, Sandeep Madireddy, Liping Wang  

**一句话要点**：提出多任务高斯过程框架，以解决工程应用中多源多保真度数据稀疏性问题。

**关键词**：多任务学习, 高斯过程, 多保真度建模, 数据稀疏性, 工程预测, 计算效率

## 3 点简述
- 核心问题：工程系统常面临高保真度数据稀缺且昂贵，低保真度数据丰富，需同时预测相关任务和保真度。
- 方法要点：利用任务间和保真度间的关系，通过多任务高斯过程建模，提升预测性能并降低计算成本。
- 实验或效果：在Forrester函数基准、3D椭球空洞建模和摩擦搅拌焊接三个场景中验证了框架的鲁棒性和可扩展性。

## 摘要（原文）

> Modern engineering and scientific workflows often require simultaneous predictions across related tasks and fidelity levels, where high-fidelity data is scarce and expensive, while low-fidelity data is more abundant. This paper introduces an Multi-Task Gaussian Processes (MTGP) framework tailored for engineering systems characterized by multi-source, multi-fidelity data, addressing challenges of data sparsity and varying task correlations. The proposed framework leverages inter-task relationships across outputs and fidelity levels to improve predictive performance and reduce computational costs. The framework is validated across three representative scenarios: Forrester function benchmark, 3D ellipsoidal void modeling, and friction-stir welding. By quantifying and leveraging inter-task relationships, the proposed MTGP framework offers a robust and scalable solution for predictive modeling in domains with significant computational and experimental costs, supporting informed decision-making and efficient resource utilization.


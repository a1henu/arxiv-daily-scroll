---
layout: default
title: TopoFair: Linking Topological Bias to Fairness in Link Prediction Benchmarks
---

# TopoFair: Linking Topological Bias to Fairness in Link Prediction Benchmarks
**arXiv**：[2602.11802v1](https://arxiv.org/abs/2602.11802) · [PDF](https://arxiv.org/pdf/2602.11802.pdf)  
**作者**：Lilian Marey, Mathilde Perez, Tiphaine Viard, Charlotte Laclau  

**一句话要点**：提出TopoFair框架，通过拓扑偏差分析提升图链接预测的公平性评估

**关键词**：图链接预测, 公平性评估, 拓扑偏差, 图生成方法, 结构分析

## 3 点简述
- 核心问题：现有公平性方法忽视图结构中的拓扑偏差，仅关注同质性，限制泛化能力
- 方法要点：形式化拓扑偏差度量分类，并开发灵活图生成方法以控制结构偏差
- 实验或效果：评估经典与公平感知模型，揭示公平性与结构偏差的交互作用

## 摘要（原文）

> Graph link prediction (LP) plays a critical role in socially impactful applications, such as job recommendation and friendship formation. Ensuring fairness in this task is thus essential. While many fairness-aware methods manipulate graph structures to mitigate prediction disparities, the topological biases inherent to social graph structures remain poorly understood and are often reduced to homophily alone. This undermines the generalization potential of fairness interventions and limits their applicability across diverse network topologies. In this work, we propose a novel benchmarking framework for fair LP, centered on the structural biases of the underlying graphs. We begin by reviewing and formalizing a broad taxonomy of topological bias measures relevant to fairness in graphs. In parallel, we introduce a flexible graph generation method that simultaneously ensures fidelity to real-world graph patterns and enables controlled variation across a wide spectrum of structural biases. We apply this framework to evaluate both classical and fairness-aware LP models across multiple use cases. Our results provide a fine-grained empirical analysis of the interactions between predictive fairness and structural biases. This new perspective reveals the sensitivity of fairness interventions to beyond-homophily biases and underscores the need for structurally grounded fairness evaluations in graph learning.


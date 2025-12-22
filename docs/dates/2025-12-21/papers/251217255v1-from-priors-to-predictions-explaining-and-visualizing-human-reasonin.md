---
layout: default
title: From Priors to Predictions: Explaining and Visualizing Human Reasoning in a Graph Neural Network Framework
---

# From Priors to Predictions: Explaining and Visualizing Human Reasoning in a Graph Neural Network Framework
**arXiv**：[2512.17255v1](https://arxiv.org/abs/2512.17255) · [PDF](https://arxiv.org/pdf/2512.17255.pdf)  
**作者**：Quan Do, Caroline Ahn, Leah Bakst, Michael Pascale, Joseph T. McGuire, Chantal E. Stern, Michael E. Hasselmo  

**一句话要点**：提出基于图神经网络和先验的框架，以解释人类推理中的归纳偏差和个体差异。

**关键词**：图神经网络, 归纳偏差, 人类推理, 先验建模, 可视化解释

## 3 点简述
- 核心问题：人类推理的归纳偏差计算形式及神经机制尚不明确。
- 方法要点：结合图论和图神经网络，将归纳偏差形式化为可操纵的结构和抽象先验。
- 实验或效果：使用ARC数据集，通过优化和可视化揭示先验结构如何影响泛化和错误。

## 摘要（原文）

> Humans excel at solving novel reasoning problems from minimal exposure, guided by inductive biases, assumptions about which entities and relationships matter. Yet the computational form of these biases and their neural implementation remain poorly understood. We introduce a framework that combines Graph Theory and Graph Neural Networks (GNNs) to formalize inductive biases as explicit, manipulable priors over structure and abstraction. Using a human behavioral dataset adapted from the Abstraction and Reasoning Corpus (ARC), we show that differences in graph-based priors can explain individual differences in human solutions. Our method includes an optimization pipeline that searches over graph configurations, varying edge connectivity and node abstraction, and a visualization approach that identifies the computational graph, the subset of nodes and edges most critical to a model's prediction. Systematic ablation reveals how generalization depends on specific prior structures and internal processing, exposing why human like errors emerge from incorrect or incomplete priors. This work provides a principled, interpretable framework for modeling the representational assumptions and computational dynamics underlying generalization, offering new insights into human reasoning and a foundation for more human aligned AI systems.


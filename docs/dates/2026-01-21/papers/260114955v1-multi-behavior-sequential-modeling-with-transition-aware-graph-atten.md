---
layout: default
title: Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation
---

# Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation
**arXiv**：[2601.14955v1](https://arxiv.org/abs/2601.14955) · [PDF](https://arxiv.org/pdf/2601.14955.pdf)  
**作者**：Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng  

**一句话要点**：提出TGA以解决电商推荐中多行为序列建模的高计算成本问题

**关键词**：多行为推荐, 序列建模, 图注意力网络, 计算效率, 电商平台

## 3 点简述
- 核心问题：传统Transformer在多行为序列建模中计算复杂度高，难以应用于大规模工业系统。
- 方法要点：构建结构化稀疏图，从项目、类别和邻居三个视角识别信息性行为转换，实现线性复杂度建模。
- 实验或效果：TGA在实验中优于现有模型，显著降低计算成本，并在工业部署中提升关键业务指标。

## 摘要（原文）

> User interactions on e-commerce platforms are inherently diverse, involving behaviors such as clicking, favoriting, adding to cart, and purchasing. The transitions between these behaviors offer valuable insights into user-item interactions, serving as a key signal for understanding evolving preferences. Consequently, there is growing interest in leveraging multi-behavior data to better capture user intent. Recent studies have explored sequential modeling of multi-behavior data, many relying on transformer-based architectures with polynomial time complexity. While effective, these approaches often incur high computational costs, limiting their applicability in large-scale industrial systems with long user sequences. To address this challenge, we propose the Transition-Aware Graph Attention Network (TGA), a linear-complexity approach for modeling multi-behavior transitions. Unlike traditional transformers that treat all behavior pairs equally, TGA constructs a structured sparse graph by identifying informative transitions from three perspectives: (a) item-level transitions, (b) category-level transitions, and (c) neighbor-level transitions. Built upon the structured graph, TGA employs a transition-aware graph Attention mechanism that jointly models user-item interactions and behavior transition types, enabling more accurate capture of sequential patterns while maintaining computational efficiency. Experiments show that TGA outperforms all state-of-the-art models while significantly reducing computational cost. Notably, TGA has been deployed in a large-scale industrial production environment, where it leads to impressive improvements in key business metrics.


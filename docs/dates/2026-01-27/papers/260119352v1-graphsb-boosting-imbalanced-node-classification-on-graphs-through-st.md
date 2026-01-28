---
layout: default
title: GraphSB: Boosting Imbalanced Node Classification on Graphs through Structural Balance
---

# GraphSB: Boosting Imbalanced Node Classification on Graphs through Structural Balance
**arXiv**：[2601.19352v1](https://arxiv.org/abs/2601.19352) · [PDF](https://arxiv.org/pdf/2601.19352.pdf)  
**作者**：Zhixiao Wang, Chaofan Zhu, Qihan Feng, Jian Zhang, Xiaobin Rui, Philip S Yu  

**一句话要点**：提出GraphSB框架，通过结构平衡解决图不平衡节点分类问题

**关键词**：图不平衡节点分类, 结构平衡, 图神经网络, 数据增强, 结构优化

## 3 点简述
- 核心问题：现有方法未解决图结构不平衡，导致多数类主导和少数类同化
- 方法要点：引入结构平衡策略，包括结构增强和关系扩散两阶段优化
- 实验或效果：GraphSB显著优于现有方法，结构平衡模块可提升其他方法平均4.57%准确率

## 摘要（原文）

> Imbalanced node classification is a critical challenge in graph learning, where most existing methods typically utilize Graph Neural Networks (GNNs) to learn node representations. These methods can be broadly categorized into the data-level and the algorithm-level. The former aims to synthesize minority-class nodes to mitigate quantity imbalance, while the latter tries to optimize the learning process to highlight minority classes. However, neither of them addresses the inherently imbalanced graph structure, which is a fundamental factor that incurs majority-class dominance and minority-class assimilation in GNNs. Our theoretical analysis further supports this critical insight. Therefore, we propose GraphSB (Graph Structural Balance), a novel framework that incorporates Structural Balance as a key strategy to address the underlying imbalanced graph structure before node synthesis. Structural Balance performs a two-stage structure optimization: Structure Enhancement that mines hard samples near decision boundaries through dual-view analysis and enhances connectivity for minority classes through adaptive augmentation, and Relation Diffusion that propagates the enhanced minority context while simultaneously capturing higher-order structural dependencies. Thus, GraphSB balances structural distribution before node synthesis, enabling more effective learning in GNNs. Extensive experiments demonstrate that GraphSB significantly outperforms the state-of-the-art methods. More importantly, the proposed Structural Balance can be seamlessly integrated into state-of-the-art methods as a simple plug-and-play module, increasing their accuracy by an average of 4.57%.


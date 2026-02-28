---
layout: default
title: MUG: Meta-path-aware Universal Heterogeneous Graph Pre-Training
---

# MUG: Meta-path-aware Universal Heterogeneous Graph Pre-Training
**arXiv**：[2602.22645v1](https://arxiv.org/abs/2602.22645) · [PDF](https://arxiv.org/pdf/2602.22645.pdf)  
**作者**：Lianze Shan, Jitao Zhao, Dongxiao He, Yongqi Huang, Zhiyong Feng, Weixiong Zhang  

**一句话要点**：提出MUG方法以解决异质图通用预训练中的元路径多样性和语义对齐挑战

**关键词**：异质图预训练, 元路径感知, 通用图表示学习, 输入统一模块, 维度感知编码器, 跨数据集泛化

## 3 点简述
- 核心问题：异质图因类型多样和元路径语义差异，难以构建通用预训练编码器
- 方法要点：通过输入统一模块和维度感知编码器对齐不同图结构，共享编码器捕获跨元路径的通用模式
- 实验或效果：在真实数据集上验证了MUG的有效性，提升了跨下游任务的泛化能力

## 摘要（原文）

> Universal graph pre-training has emerged as a key paradigm in graph representation learning, offering a promising way to train encoders to learn transferable representations from unlabeled graphs and to effectively generalize across a wide range of downstream tasks. However, recent explorations in universal graph pre-training primarily focus on homogeneous graphs and it remains unexplored for heterogeneous graphs, which exhibit greater structural and semantic complexity. This heterogeneity makes it highly challenging to train a universal encoder for diverse heterogeneous graphs: (i) the diverse types with dataset-specific semantics hinder the construction of a unified representation space; (ii) the number and semantics of meta-paths vary across datasets, making encoding and aggregation patterns learned from one dataset difficult to apply to others. To address these challenges, we propose a novel Meta-path-aware Universal heterogeneous Graph pre-training (MUG) approach. Specifically, for challenge (i), MUG introduces a input unification module that integrates information from multiple node and relation types within each heterogeneous graph into a unified representation.This representation is then projected into a shared space by a dimension-aware encoder, enabling alignment across graphs with diverse schemas.Furthermore, for challenge (ii), MUG trains a shared encoder to capture consistent structural patterns across diverse meta-path views rather than relying on dataset-specific aggregation strategies, while a global objective encourages discriminability and reduces dataset-specific biases. Extensive experiments demonstrate the effectiveness of MUG on some real datasets.


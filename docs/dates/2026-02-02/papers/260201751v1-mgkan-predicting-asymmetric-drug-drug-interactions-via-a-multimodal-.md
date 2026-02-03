---
layout: default
title: MGKAN: Predicting Asymmetric Drug-Drug Interactions via a Multimodal Graph Kolmogorov-Arnold Network
---

# MGKAN: Predicting Asymmetric Drug-Drug Interactions via a Multimodal Graph Kolmogorov-Arnold Network
**arXiv**：[2602.01751v1](https://arxiv.org/abs/2602.01751) · [PDF](https://arxiv.org/pdf/2602.01751.pdf)  
**作者**：Kunyi Fan, Mengjie Chen, Longlong Li, Cunquan Qu  

**一句话要点**：提出MGKAN以解决药物相互作用预测中的非线性和非对称性问题

**关键词**：药物相互作用预测, 图神经网络, Kolmogorov-Arnold网络, 多模态融合, 非对称建模, 非线性学习

## 3 点简述
- 核心问题：现有图神经网络依赖线性聚合和对称假设，难以捕捉药物相互作用的非线性与异质性模式。
- 方法要点：引入可学习基函数的图Kolmogorov-Arnold网络，结合多模态网络视图和角色特定嵌入，增强非线性建模能力。
- 实验或效果：在两个基准数据集上超越七个先进基线，消融和案例研究验证了预测准确性和方向性药物效应建模的有效性。

## 摘要（原文）

> Predicting drug-drug interactions (DDIs) is essential for safe pharmacological treatments. Previous graph neural network (GNN) models leverage molecular structures and interaction networks but mostly rely on linear aggregation and symmetric assumptions, limiting their ability to capture nonlinear and heterogeneous patterns. We propose MGKAN, a Graph Kolmogorov-Arnold Network that introduces learnable basis functions into asymmetric DDI prediction. MGKAN replaces conventional MLP transformations with KAN-driven basis functions, enabling more expressive and nonlinear modeling of drug relationships. To capture pharmacological dependencies, MGKAN integrates three network views-an asymmetric DDI network, a co-interaction network, and a biochemical similarity network-with role-specific embeddings to preserve directional semantics. A fusion module combines linear attention and nonlinear transformation to enhance representational capacity. On two benchmark datasets, MGKAN outperforms seven state-of-the-art baselines. Ablation studies and case studies confirm its predictive accuracy and effectiveness in modeling directional drug effects.


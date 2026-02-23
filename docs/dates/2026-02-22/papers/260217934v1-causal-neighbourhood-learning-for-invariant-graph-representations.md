---
layout: default
title: Causal Neighbourhood Learning for Invariant Graph Representations
---

# Causal Neighbourhood Learning for Invariant Graph Representations
**arXiv**：[2602.17934v1](https://arxiv.org/abs/2602.17934) · [PDF](https://arxiv.org/pdf/2602.17934.pdf)  
**作者**：Simi Job, Xiaohui Tao, Taotao Cai, Haoran Xie, Jianming Yong  

**一句话要点**：提出CNL-GNN框架，通过因果干预解决图数据中虚假相关性问题，提升图神经网络泛化能力。

**关键词**：因果图学习, 图神经网络, 虚假相关性, 反事实干预, 鲁棒表示学习

## 3 点简述
- 图数据常含虚假相关，传统GNN依赖这些模式导致泛化差和鲁棒性低。
- CNL-GNN通过反事实邻域生成和自适应边扰动，识别并保留因果连接，减少虚假影响。
- 在四个公开数据集上实验，CNL-GNN优于现有GNN模型，验证其有效性和泛化性。

## 摘要（原文）

> Graph data often contain noisy and spurious correlations that mask the true causal relationships, which are essential for enabling graph models to make predictions based on the underlying causal structure of the data. Dependence on spurious connections makes it challenging for traditional Graph Neural Networks (GNNs) to generalize effectively across different graphs. Furthermore, traditional aggregation methods tend to amplify these spurious patterns, limiting model robustness under distribution shifts. To address these issues, we propose Causal Neighbourhood Learning with Graph Neural Networks (CNL-GNN), a novel framework that performs causal interventions on graph structure. CNL-GNN effectively identifies and preserves causally relevant connections and reduces spurious influences through the generation of counterfactual neighbourhoods and adaptive edge perturbation guided by learnable importance masking and an attention-based mechanism. In addition, by combining structural-level interventions with the disentanglement of causal features from confounding factors, the model learns invariant node representations that are robust and generalize well across different graph structures. Our approach improves causal graph learning beyond traditional feature-based methods, resulting in a robust classification model. Extensive experiments on four publicly available datasets, including multiple domain variants of one dataset, demonstrate that CNL-GNN outperforms state-of-the-art GNN models.


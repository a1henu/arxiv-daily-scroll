---
layout: default
title: Edge-Centric Relational Reasoning for 3D Scene Graph Prediction
---

# Edge-Centric Relational Reasoning for 3D Scene Graph Prediction
**arXiv**：[2511.15288v1](https://arxiv.org/abs/2511.15288) · [PDF](https://arxiv.org/pdf/2511.15288.pdf)  
**作者**：Yanni Ma, Hao Liu, Yulan Guo, Theo Gevers, Martin R. Oswald  

**一句话要点**：提出LEO框架以解决3D场景图预测中高阶关系依赖捕获不足的问题

**关键词**：3D场景图预测, 边中心推理, 线图神经网络, 关系预测, 对象感知融合

## 3 点简述
- 现有方法依赖对象中心图神经网络，难以捕捉高阶关系依赖
- LEO通过线图转换实现边中心关系推理，并融合对象感知特征
- 在3DSSG数据集上实验显示，与基线相比有持续改进

## 摘要（原文）

> 3D scene graph prediction aims to abstract complex 3D environments into structured graphs consisting of objects and their pairwise relationships. Existing approaches typically adopt object-centric graph neural networks, where relation edge features are iteratively updated by aggregating messages from connected object nodes. However, this design inherently restricts relation representations to pairwise object context, making it difficult to capture high-order relational dependencies that are essential for accurate relation prediction. To address this limitation, we propose a Link-guided Edge-centric relational reasoning framework with Object-aware fusion, namely LEO, which enables progressive reasoning from relation-level context to object-level understanding. Specifically, LEO first predicts potential links between object pairs to suppress irrelevant edges, and then transforms the original scene graph into a line graph where each relation is treated as a node. A line graph neural network is applied to perform edge-centric relational reasoning to capture inter-relation context. The enriched relation features are subsequently integrated into the original object-centric graph to enhance object-level reasoning and improve relation prediction. Our framework is model-agnostic and can be integrated with any existing object-centric method. Experiments on the 3DSSG dataset with two competitive baselines show consistent improvements, highlighting the effectiveness of our edge-to-object reasoning paradigm.


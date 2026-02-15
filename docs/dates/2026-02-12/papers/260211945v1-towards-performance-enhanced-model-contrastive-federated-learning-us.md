---
layout: default
title: Towards Performance-Enhanced Model-Contrastive Federated Learning using Historical Information in Heterogeneous Scenarios
---

# Towards Performance-Enhanced Model-Contrastive Federated Learning using Historical Information in Heterogeneous Scenarios
**arXiv**：[2602.11945v1](https://arxiv.org/abs/2602.11945) · [PDF](https://arxiv.org/pdf/2602.11945.pdf)  
**作者**：Hongliang Zhang, Jiguo Yu, Guijuan Wang, Wenshuo Ma, Tianqing He, Baobao Chai, Chunqiang Hu  

**一句话要点**：提出PMFL框架，利用历史信息增强模型对比联邦学习在异构场景中的性能

**关键词**：联邦学习, 异构场景, 模型对比学习, 历史信息利用, 自适应聚合

## 3 点简述
- 核心问题：联邦学习在数据分布和参与频率异构的场景中性能下降
- 方法要点：节点端引入历史模型对比项，服务器端自适应调整聚合权重并利用历史全局模型
- 实验或效果：在异构场景中相比现有方法表现更优

## 摘要（原文）

> Federated Learning (FL) enables multiple nodes to collaboratively train a model without sharing raw data. However, FL systems are usually deployed in heterogeneous scenarios, where nodes differ in both data distributions and participation frequencies, which undermines the FL performance. To tackle the above issue, this paper proposes PMFL, a performance-enhanced model-contrastive federated learning framework using historical training information. Specifically, on the node side, we design a novel model-contrastive term into the node optimization objective by incorporating historical local models to capture stable contrastive points, thereby improving the consistency of model updates in heterogeneous data distributions.
>   On the server side, we utilize the cumulative participation count of each node to adaptively adjust its aggregation weight, thereby correcting the bias in the global objective caused by different node participation frequencies. Furthermore, the updated global model incorporates historical global models to reduce its fluctuations in performance between adjacent rounds. Extensive experiments demonstrate that PMFL achieves superior performance compared with existing FL methods in heterogeneous scenarios.


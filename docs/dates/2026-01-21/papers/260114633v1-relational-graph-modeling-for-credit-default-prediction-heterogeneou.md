---
layout: default
title: Relational Graph Modeling for Credit Default Prediction: Heterogeneous GNNs and Hybrid Ensemble Learning
---

# Relational Graph Modeling for Credit Default Prediction: Heterogeneous GNNs and Hybrid Ensemble Learning
**arXiv**：[2601.14633v1](https://arxiv.org/abs/2601.14633) · [PDF](https://arxiv.org/pdf/2601.14633.pdf)  
**作者**：Yvonne Yang, Eranki Vasistha  

**一句话要点**：提出异构图神经网络与混合集成学习，以提升信用违约预测中跨实体依赖的建模能力。

**关键词**：信用违约预测, 异构图神经网络, 混合集成学习, 大规模图建模, 解释性分析, 公平性评估

## 3 点简述
- 核心问题：信用违约风险涉及借款人与交易级实体的复杂交互，传统表格模型难以显式捕获跨实体依赖。
- 方法要点：构建大规模异构图，集成借款人与交易实体，评估异构GNNs，并采用混合集成结合表格特征与GNN嵌入。
- 实验或效果：混合集成在ROC-AUC和PR-AUC上表现最佳，优于单独GNNs和梯度提升树基线，同时进行了解释性与公平性分析。

## 摘要（原文）

> Credit default risk arises from complex interactions among borrowers, financial institutions, and transaction-level behaviors. While strong tabular models remain highly competitive in credit scoring, they may fail to explicitly capture cross-entity dependencies embedded in multi-table financial histories. In this work, we construct a massive-scale heterogeneous graph containing over 31 million nodes and more than 50 million edges, integrating borrower attributes with granular transaction-level entities such as installment payments, POS cash balances, and credit card histories.
>   We evaluate heterogeneous graph neural networks (GNNs), including heterogeneous GraphSAGE and a relation-aware attentive heterogeneous GNN, against strong tabular baselines. We find that standalone GNNs provide limited lift over a competitive gradient-boosted tree baseline, while a hybrid ensemble that augments tabular features with GNN-derived customer embeddings achieves the best overall performance, improving both ROC-AUC and PR-AUC. We further observe that contrastive pretraining can improve optimization stability but yields limited downstream gains under generic graph augmentations. Finally, we conduct structured explainability and fairness analyses to characterize how relational signals affect subgroup behavior and screening-oriented outcomes.


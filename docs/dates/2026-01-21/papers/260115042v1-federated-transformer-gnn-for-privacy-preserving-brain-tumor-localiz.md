---
layout: default
title: Federated Transformer-GNN for Privacy-Preserving Brain Tumor Localization with Modality-Level Explainability
---

# Federated Transformer-GNN for Privacy-Preserving Brain Tumor Localization with Modality-Level Explainability
**arXiv**：[2601.15042v1](https://arxiv.org/abs/2601.15042) · [PDF](https://arxiv.org/pdf/2601.15042.pdf)  
**作者**：Andrea Protani, Riccardo Taiello, Marc Molina Van Den Bosch, Luigi Serio  

**一句话要点**：提出联邦Transformer-GNN框架，用于隐私保护的脑肿瘤定位，并提供模态级可解释性。

**关键词**：联邦学习, 脑肿瘤定位, Transformer-GNN, 隐私保护, 可解释性分析, 医疗影像

## 3 点简述
- 核心问题：脑肿瘤分析需大规模数据，但医疗数据因隐私法规分散，难以集中训练。
- 方法要点：基于Transformer-GNN混合架构，在CAFEIN平台实现联邦学习，避免共享敏感数据。
- 实验或效果：在BraTS数据集上，联邦学习匹配集中式性能，可解释性分析显示深层网络关注T2和FLAIR模态。

## 摘要（原文）

> Deep learning models for brain tumor analysis require large and diverse datasets that are often siloed across healthcare institutions due to privacy regulations. We present a federated learning framework for brain tumor localization that enables multi-institutional collaboration without sharing sensitive patient data. Our method extends a hybrid Transformer-Graph Neural Network architecture derived from prior decoder-free supervoxel GNNs and is deployed within CAFEIN\textsuperscript{\textregistered}, CERN's federated learning platform designed for healthcare environments. We provide an explainability analysis through Transformer attention mechanisms that reveals which MRI modalities drive the model predictions. Experiments on the BraTS dataset demonstrate a key finding: while isolated training on individual client data triggers early stopping well before reaching full training capacity, federated learning enables continued model improvement by leveraging distributed data, ultimately matching centralized performance. This result provides strong justification for federated learning when dealing with complex tasks and high-dimensional input data, as aggregating knowledge from multiple institutions significantly benefits the learning process. Our explainability analysis, validated through rigorous statistical testing on the full test set (paired t-tests with Bonferroni correction), reveals that deeper network layers significantly increase attention to T2 and FLAIR modalities ($p<0.001$, Cohen's $d$=1.50), aligning with clinical practice.


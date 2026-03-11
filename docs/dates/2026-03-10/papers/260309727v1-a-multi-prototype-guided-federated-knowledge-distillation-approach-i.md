---
layout: default
title: A Multi-Prototype-Guided Federated Knowledge Distillation Approach in AI-RAN Enabled Multi-Access Edge Computing System
---

# A Multi-Prototype-Guided Federated Knowledge Distillation Approach in AI-RAN Enabled Multi-Access Edge Computing System
**arXiv**：[2603.09727v1](https://arxiv.org/abs/2603.09727) · [PDF](https://arxiv.org/pdf/2603.09727.pdf)  
**作者**：Luyao Zou, Hayoung Oh, Chu Myaet Thwal, Apurba Adhikary, Seohyeon Hong, Zhu Han  

**一句话要点**：提出多原型引导的联邦知识蒸馏方法，以解决AI-RAN使能多接入边缘计算系统中的非独立同分布数据问题。

**关键词**：联邦学习, 知识蒸馏, 多原型策略, 非独立同分布数据, 边缘计算, AI-RAN

## 3 点简述
- 核心问题：传统联邦学习在处理非独立同分布数据时面临挑战，单原型策略可能导致信息丢失。
- 方法要点：集成自知识蒸馏，采用多原型策略，包括条件层次凝聚聚类和原型对齐方案，并设计LEMGP损失函数。
- 实验或效果：在多个数据集和不同非独立同分布设置下，MP-FedKD在准确性、平均准确性和误差方面优于现有基线方法。

## 摘要（原文）

> With the development of wireless network, Multi-Access Edge Computing (MEC) and Artificial Intelligence (AI)-native Radio Access Network (RAN) have attracted significant attention. Particularly, the integration of AI-RAN and MEC is envisioned to transform network efficiency and responsiveness. Therefore, it is valuable to investigate AI-RAN enabled MEC system. Federated learning (FL) nowadays is emerging as a promising approach for AI-RAN enabled MEC system, in which edge devices are enabled to train a global model cooperatively without revealing their raw data. However, conventional FL encounters the challenge in processing the non-independent and identically distributed (non-IID) data. Single prototype obtained by averaging the embedding vectors per class can be employed in FL to handle the data heterogeneity issue. Nevertheless, this may result in the loss of useful information owing to the average operation. Therefore, in this paper, a multi-prototype-guided federated knowledge distillation (MP-FedKD) approach is proposed. Particularly, self-knowledge distillation is integrated into FL to deal with the non-IID issue. To cope with the problem of information loss caused by single prototype-based strategy, multi-prototype strategy is adopted, where we present a conditional hierarchical agglomerative clustering (CHAC) approach and a prototype alignment scheme. Additionally, we design a novel loss function (called LEMGP loss) for each local client, where the relationship between global prototypes and local embedding will be focused. Extensive experiments over multiple datasets with various non-IID settings showcase that the proposed MP-FedKD approach outperforms the considered state-of-the-art baselines regarding accuracy, average accuracy and errors (RMSE and MAE).


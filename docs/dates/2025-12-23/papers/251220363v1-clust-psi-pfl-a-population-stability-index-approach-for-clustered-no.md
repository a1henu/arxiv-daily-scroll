---
layout: default
title: Clust-PSI-PFL: A Population Stability Index Approach for Clustered Non-IID Personalized Federated Learning
---

# Clust-PSI-PFL: A Population Stability Index Approach for Clustered Non-IID Personalized Federated Learning
**arXiv**：[2512.20363v1](https://arxiv.org/abs/2512.20363) · [PDF](https://arxiv.org/pdf/2512.20363.pdf)  
**作者**：Daniel M. Jimenez-Gutierrez, Mehrdad Hassanzadeh, Aris Anagnostopoulos, Ioannis Chatzigiannakis, Andrea Vitaletti  

**一句话要点**：提出基于PSI聚类的个性化联邦学习框架以解决非独立同分布数据问题

**关键词**：个性化联邦学习, 非独立同分布数据, 人口稳定性指数, 聚类算法, 客户端公平性, 标签偏斜

## 3 点简述
- 联邦学习中非独立同分布数据导致模型偏差和性能下降
- 使用加权PSI量化非独立同分布程度，并通过K-means++聚类形成同质客户端组
- 在多种数据集和协议下，提升全局准确度达18%，客户端公平性相对改善37%

## 摘要（原文）

> Federated learning (FL) supports privacy-preserving, decentralized machine learning (ML) model training by keeping data on client devices. However, non-independent and identically distributed (non-IID) data across clients biases updates and degrades performance. To alleviate these issues, we propose Clust-PSI-PFL, a clustering-based personalized FL framework that uses the Population Stability Index (PSI) to quantify the level of non-IID data. We compute a weighted PSI metric, $WPSI^L$, which we show to be more informative than common non-IID metrics (Hellinger, Jensen-Shannon, and Earth Mover's distance). Using PSI features, we form distributionally homogeneous groups of clients via K-means++; the number of optimal clusters is chosen by a systematic silhouette-based procedure, typically yielding few clusters with modest overhead. Across six datasets (tabular, image, and text modalities), two partition protocols (Dirichlet with parameter $α$ and Similarity with parameter S), and multiple client sizes, Clust-PSI-PFL delivers up to 18% higher global accuracy than state-of-the-art baselines and markedly improves client fairness by a relative improvement of 37% under severe non-IID data. These results establish PSI-guided clustering as a principled, lightweight mechanism for robust PFL under label skew.


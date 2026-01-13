---
layout: default
title: Studying the Role of Synthetic Data for Machine Learning-based Wireless Networks Traffic Forecasting
---

# Studying the Role of Synthetic Data for Machine Learning-based Wireless Networks Traffic Forecasting
**arXiv**：[2601.07646v1](https://arxiv.org/abs/2601.07646) · [PDF](https://arxiv.org/pdf/2601.07646.pdf)  
**作者**：José Pulido, Francesc Wilhelmi, Sergio Fortes, Alfonso Fernández-Durán, Lorenzo Galati Giordano, Raquel Barco  

**一句话要点**：提出基于一阶自回归噪声统计的合成数据生成方法，用于大规模Wi-Fi网络流量预测。

**关键词**：合成数据生成, 无线网络流量预测, 机器学习, 一阶自回归模型, Wi-Fi部署

## 3 点简述
- 核心问题：合成数据在无线网络流量预测中如何提升机器学习模型的性能与泛化能力。
- 方法要点：使用一阶自回归噪声统计生成合成数据，以最小真实数据需求模拟真实接入点行为。
- 实验或效果：合成数据训练的模型在相同接入点上MAE接近真实数据，泛化时预测精度提升高达50%。

## 摘要（原文）

> Synthetic data generation is an appealing tool for augmenting and enriching datasets, playing a crucial role in advancing artificial intelligence (AI) and machine learning (ML). Not only does synthetic data help build robust AI/ML datasets cost-effectively, but it also offers privacy-friendly solutions and bypasses the complexities of storing large data volumes. This paper proposes a novel method to generate synthetic data, based on first-order auto-regressive noise statistics, for large-scale Wi-Fi deployments. The approach operates with minimal real data requirements while producing statistically rich traffic patterns that effectively mimic real Access Point (AP) behavior. Experimental results show that ML models trained on synthetic data achieve Mean Absolute Error (MAE) values within 10 to 15 of those obtained using real data when trained on the same APs, while requiring significantly less training data. Moreover, when generalization is required, synthetic-data-trained models improve prediction accuracy by up to 50 percent compared to real-data-trained baselines, thanks to the enhanced variability and diversity of the generated traces. Overall, the proposed method bridges the gap between synthetic data generation and practical Wi-Fi traffic forecasting, providing a scalable, efficient, and real-time solution for modern wireless networks.


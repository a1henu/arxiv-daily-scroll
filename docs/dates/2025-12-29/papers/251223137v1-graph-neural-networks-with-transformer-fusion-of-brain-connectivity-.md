---
layout: default
title: Graph Neural Networks with Transformer Fusion of Brain Connectivity Dynamics and Tabular Data for Forecasting Future Tobacco Use
---

# Graph Neural Networks with Transformer Fusion of Brain Connectivity Dynamics and Tabular Data for Forecasting Future Tobacco Use
**arXiv**：[2512.23137v1](https://arxiv.org/abs/2512.23137) · [PDF](https://arxiv.org/pdf/2512.23137.pdf)  
**作者**：Runzhi Zhou, Xi Luo  

**一句话要点**：提出GNN-TF模型，融合脑连接动态与表格数据以预测未来烟草使用

**关键词**：图神经网络, Transformer融合, 脑连接动态, 多模态数据整合, 纵向预测, 烟草使用预测

## 3 点简述
- 核心问题：整合非欧几里得脑成像与欧几里得表格数据，预测纵向研究中的未来结果。
- 方法要点：结合时间感知图神经网络与Transformer融合，灵活处理多模态数据的时间顺序。
- 实验或效果：在NCANDA数据集上优于现有方法，提升预测烟草使用的准确性。

## 摘要（原文）

> Integrating non-Euclidean brain imaging data with Euclidean tabular data, such as clinical and demographic information, poses a substantial challenge for medical imaging analysis, particularly in forecasting future outcomes. While machine learning and deep learning techniques have been applied successfully to cross-sectional classification and prediction tasks, effectively forecasting outcomes in longitudinal imaging studies remains challenging. To address this challenge, we introduce a time-aware graph neural network model with transformer fusion (GNN-TF). This model flexibly integrates both tabular data and dynamic brain connectivity data, leveraging the temporal order of these variables within a coherent framework. By incorporating non-Euclidean and Euclidean sources of information from a longitudinal resting-state fMRI dataset from the National Consortium on Alcohol and Neurodevelopment in Adolescence (NCANDA), the GNN-TF enables a comprehensive analysis that captures critical aspects of longitudinal imaging data. Comparative analyses against a variety of established machine learning and deep learning models demonstrate that GNN-TF outperforms these state-of-the-art methods, delivering superior predictive accuracy for predicting future tobacco usage. The end-to-end, time-aware transformer fusion structure of the proposed GNN-TF model successfully integrates multiple data modalities and leverages temporal dynamics, making it a valuable analytic tool for functional brain imaging studies focused on clinical outcome prediction.


---
layout: default
title: Comparative Assessment of Multimodal Earth Observation Data for Soil Moisture Estimation
---

# Comparative Assessment of Multimodal Earth Observation Data for Soil Moisture Estimation
**arXiv**：[2602.18083v1](https://arxiv.org/abs/2602.18083) · [PDF](https://arxiv.org/pdf/2602.18083.pdf)  
**作者**：Ioannis Kontogiorgakis, Athanasios Askitopoulos, Iason Tsardanidis, Dimitrios Bormpoudakis, Ilias Tsoumas, Fotios Balampanis, Charalampos Kontoes  

**一句话要点**：提出结合多模态遥感数据与机器学习的10米分辨率土壤湿度估计框架，用于欧洲植被区精准农业监测。

**关键词**：土壤湿度估计, 多模态遥感, 机器学习, 高分辨率监测, 特征工程, 欧洲植被区

## 3 点简述
- 核心问题：现有卫星土壤湿度产品分辨率粗（>1公里），不适用于农场级应用。
- 方法要点：融合Sentinel-1 SAR、Sentinel-2光学影像和ERA-5再分析数据，通过机器学习实现高分辨率估计。
- 实验或效果：使用113个ISMN站点验证，混合时间匹配策略达到R^2=0.518，传统特征工程优于基础模型嵌入。

## 摘要（原文）

> Accurate soil moisture (SM) estimation is critical for precision agriculture, water resources management and climate monitoring. Yet, existing satellite SM products are too coarse (>1km) for farm-level applications. We present a high-resolution (10m) SM estimation framework for vegetated areas across Europe, combining Sentinel-1 SAR, Sentinel-2 optical imagery and ERA-5 reanalysis data through machine learning. Using 113 International Soil Moisture Network (ISMN) stations spanning diverse vegetated areas, we compare modality combinations with temporal parameterizations, using spatial cross-validation, to ensure geographic generalization. We also evaluate whether foundation model embeddings from IBM-NASA's Prithvi model improve upon traditional hand-crafted spectral features. Results demonstrate that hybrid temporal matching - Sentinel-2 current-day acquisitions with Sentinel-1 descending orbit - achieves R^2=0.514, with 10-day ERA5 lookback window improving performance to R^2=0.518. Foundation model (Prithvi) embeddings provide negligible improvement over hand-crafted features (R^2=0.515 vs. 0.514), indicating traditional feature engineering remains highly competitive for sparse-data regression tasks. Our findings suggest that domain-specific spectral indices combined with tree-based ensemble methods offer a practical and computationally efficient solution for operational pan-European field-scale soil moisture monitoring.


---
layout: default
title: NEXUS : A compact neural architecture for high-resolution spatiotemporal air quality forecasting in Delhi Nationa Capital Region
---

# NEXUS : A compact neural architecture for high-resolution spatiotemporal air quality forecasting in Delhi Nationa Capital Region
**arXiv**：[2602.19654v1](https://arxiv.org/abs/2602.19654) · [PDF](https://arxiv.org/pdf/2602.19654.pdf)  
**作者**：Rampunit Kumar, Aditya Maheshwari  

**一句话要点**：提出NEXUS架构以高效预测德里国家首都区域高分辨率时空空气质量

**关键词**：空气质量预测, 时空预测, 神经网络架构, 低秩投影, 自适应融合, 德里国家首都区域

## 3 点简述
- 核心问题：德里国家首都区域空气污染严重，需高效预测污染物浓度以应对公共健康挑战。
- 方法要点：NEXUS架构集成补丁嵌入、低秩投影和自适应融合机制，参数仅18,748个，实现高精度预测。
- 实验或效果：在四年数据上，R²超过0.94（CO）、0.91（NO）、0.95（SO₂），优于基准模型，支持实时部署。

## 摘要（原文）

> Urban air pollution in megacities poses critical public health challenges, particularly in Delhi National Capital Region (NCR) where severe degradation affects millions. We present NEXUS (Neural Extraction and Unified Spatiotemporal) architecture for forecasting carbon monoxide, nitrogen oxide, and sulfur dioxide. Working with four years (2018--2021) of atmospheric data across sixteen spatial grids, NEXUS achieves R$^2$ exceeding 0.94 for CO, 0.91 for NO, and 0.95 for SO$_2$ using merely 18,748 parameters -- substantially fewer than SCINet (35,552), Autoformer (68,704), and FEDformer (298,080). The architecture integrates patch embedding, low-rank projections, and adaptive fusion mechanisms to decode complex atmospheric chemistry patterns. Our investigation uncovers distinct diurnal rhythms and pronounced seasonal variations, with winter months experiencing severe pollution episodes driven by temperature inversions and agricultural biomass burning. Analysis identifies critical meteorological thresholds, quantifies wind field impacts on pollutant dispersion, and maps spatial heterogeneity across the region. Extensive ablation experiments demonstrate each architectural component's role. NEXUS delivers superior predictive performance with remarkable computational efficiency, enabling real-time deployment for air quality monitoring systems.


---
layout: default
title: GeoFormer: A Swin Transformer-Based Framework for Scene-Level Building Height and Footprint Estimation from Sentinel Imagery
---

# GeoFormer: A Swin Transformer-Based Framework for Scene-Level Building Height and Footprint Estimation from Sentinel Imagery
**arXiv**：[2602.09932v1](https://arxiv.org/abs/2602.09932) · [PDF](https://arxiv.org/pdf/2602.09932.pdf)  
**作者**：Han Jinzhen, JinByeong Lee, JiSung Kim, MinKyung Cho, DaHee Kim, HongSik Yun  

**一句话要点**：提出GeoFormer框架，基于Swin Transformer从Sentinel影像联合估计建筑高度与足迹，提升城市三维数据准确性。

**关键词**：建筑高度估计, 建筑足迹估计, Swin Transformer, Sentinel影像, 多源数据融合, 城市三维建模

## 3 点简述
- 核心问题：城市三维数据稀缺，依赖专有传感器或跨城市泛化能力差，影响气候建模与城市规划。
- 方法要点：使用Swin Transformer框架，融合Sentinel-1/2影像和开放DEM数据，采用地理分块策略确保训练测试集空间独立性。
- 实验或效果：在54个城市评估中，建筑高度RMSE为3.19米，足迹RMSE为0.05，优于CNN基线，跨大陆转移性能稳定。

## 摘要（原文）

> Accurate three-dimensional urban data are critical for climate modelling, disaster risk assessment, and urban planning, yet remain scarce due to reliance on proprietary sensors or poor cross-city generalisation. We propose GeoFormer, an open-source Swin Transformer framework that jointly estimates building height (BH) and footprint (BF) on a 100 m grid using only Sentinel-1/2 imagery and open DEM data. A geo-blocked splitting strategy ensures strict spatial independence between training and test sets. Evaluated over 54 diverse cities, GeoFormer achieves a BH RMSE of 3.19 m and a BF RMSE of 0.05, improving 7.5% and 15.3% over the strongest CNN baseline, while maintaining under 3.5 m BH RMSE in cross-continent transfer. Ablation studies confirm that DEM is indispensable for height estimation and that optical reflectance dominates over SAR, though multi-source fusion yields the best overall accuracy. All code, weights, and global products are publicly released.


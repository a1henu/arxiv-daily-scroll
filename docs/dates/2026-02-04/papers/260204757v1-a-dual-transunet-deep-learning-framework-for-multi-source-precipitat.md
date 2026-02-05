---
layout: default
title: A Dual-TransUNet Deep Learning Framework for Multi-Source Precipitation Merging and Improving Seasonal and Extreme Estimates
---

# A Dual-TransUNet Deep Learning Framework for Multi-Source Precipitation Merging and Improving Seasonal and Extreme Estimates
**arXiv**：[2602.04757v1](https://arxiv.org/abs/2602.04757) · [PDF](https://arxiv.org/pdf/2602.04757.pdf)  
**作者**：Yuchen Ye, Zixuan Qi, Shixuan Li, Wei Qi, Yanpeng Cai, Chaoxia Yuan  

**一句话要点**：提出双阶段TransUNet框架以融合多源降水数据并提升季节与极端降水估计

**关键词**：降水数据融合, TransUNet, 极端降水估计, 深度学习, 多源数据集成, SHAP分析

## 3 点简述
- 多源降水产品存在空间异质性偏差和极端降水估计能力不足的问题
- 采用双阶段TransUNet架构，先分类估计降水发生概率，再回归融合多源数据
- 在中国区域验证显示季节性能提升，极端降水检测增强，适用于数据稀缺区

## 摘要（原文）

> Multi-source precipitation products (MSPs) from satellite retrievals and reanalysis are widely used for hydroclimatic monitoring, yet spatially heterogeneous biases and limited skill for extremes still constrain their hydrologic utility. Here we develop a dual-stage TransUNet-based multi-source precipitation merging framework (DDL-MSPMF) that integrates six MSPs with four ERA5 near-surface physical predictors. A first-stage classifier estimates daily precipitation occurrence probability, and a second-stage regressor fuses the classifier outputs together with all predictors to estimate daily precipitation amount at 0.25 degree resolution over China for 2001-2020. Benchmarking against multiple deep learning and hybrid baselines shows that the TransUNet - TransUNet configuration yields the best seasonal performance (R = 0.75; RMSE = 2.70 mm/day) and improves robustness relative to a single-regressor setting. For heavy precipitation (>25 mm/day), DDL-MSPMF increases equitable threat scores across most regions of eastern China and better reproduces the spatial pattern of the July 2021 Zhengzhou rainstorm, indicating enhanced extreme-event detection beyond seasonal-mean corrections. Independent evaluation over the Qinghai-Tibet Plateau using TPHiPr further supports its applicability in data-scarce regions. SHAP analysis highlights the importance of precipitation occurrence probabilities and surface pressure, providing physically interpretable diagnostics. The proposed framework offers a scalable and explainable approach for precipitation fusion and extreme-event assessment.


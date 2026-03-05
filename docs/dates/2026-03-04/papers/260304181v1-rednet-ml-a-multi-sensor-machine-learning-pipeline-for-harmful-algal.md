---
layout: default
title: REDNET-ML: A Multi-Sensor Machine Learning Pipeline for Harmful Algal Bloom Risk Detection Along the Omani Coast
---

# REDNET-ML: A Multi-Sensor Machine Learning Pipeline for Harmful Algal Bloom Risk Detection Along the Omani Coast
**arXiv**：[2603.04181v1](https://arxiv.org/abs/2603.04181) · [PDF](https://arxiv.org/pdf/2603.04181.pdf)  
**作者**：Ameer Alhashemi  

**一句话要点**：提出REDNET-ML多传感器机器学习流水线，用于阿曼海岸有害藻华风险检测

**关键词**：有害藻华检测, 多传感器融合, 机器学习流水线, 卫星遥感, 风险概率校准

## 3 点简述
- 核心问题：有害藻华威胁沿海基础设施和供水，需高效检测方法
- 方法要点：融合Sentinel-2、MODIS卫星数据及目标检测器信号，使用CatBoost进行决策融合
- 实验或效果：通过AUROC/AUPRC等指标评估，支持端到端推理和风险可视化

## 摘要（原文）

> Harmful algal blooms (HABs) can threaten coastal infrastructure, fisheries, and desalination dependent water supplies. This project (REDNET-ML) develops a reproducible machine learning pipeline for HAB risk detection along the Omani coastline using multi sensor satellite data and non leaky evaluation. The system fuses (i) Sentinel-2 optical chips (high spatial resolution) processed into spectral indices and texture signals, (ii) MODIS Level-3 ocean color and thermal indicators, and (iii) learned image evidence from object detectors trained to highlight bloom like patterns. A compact decision fusion model (CatBoost) integrates these signals into a calibrated probability of HAB risk, which is then consumed by an end to end inference workflow and a risk field viewer that supports operational exploration by site (plant) and time. The report documents the motivation, related work, methodological choices (including label mining and strict split strategies), implementation details, and a critical evaluation using AUROC/AUPRC, confusion matrices, calibration curves, and drift analyses that quantify distribution shift in recent years.


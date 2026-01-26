---
layout: default
title: Calibrated Probabilistic Interpolation for GEDI Biomass
---

# Calibrated Probabilistic Interpolation for GEDI Biomass
**arXiv**：[2601.16834v1](https://arxiv.org/abs/2601.16834) · [PDF](https://arxiv.org/pdf/2601.16834.pdf)  
**作者**：Robin Young, Srinivasan Keshav  

**一句话要点**：提出Attentive Neural Processes以解决GEDI稀疏LiDAR观测在异质景观中插值的不确定性校准问题

**关键词**：GEDI生物量插值, 不确定性校准, Attentive Neural Processes, 地理空间建模, 少样本适应, 异质景观

## 3 点简述
- 核心问题：传统机器学习方法（如随机森林、XGBoost）在GEDI生物量插值中未适应异质景观，导致预测区间未校准。
- 方法要点：引入Attentive Neural Processes，基于局部观测集和地理空间基础模型嵌入学习灵活空间协方差函数。
- 实验或效果：在五个不同生物区验证，ANPs在保持竞争性准确度的同时实现近理想不确定性校准，并展示少样本适应能力。

## 摘要（原文）

> Reliable wall-to-wall biomass mapping from NASA's GEDI mission requires interpolating sparse LiDAR observations across heterogeneous landscapes. While machine learning approaches like Random Forest and XGBoost are standard for this task, they treat spatial predictions of GEDI observations from multispectral or SAR remote sensing data as independent without adapting to the varying difficulty of heterogeneous landscapes. We demonstrate these approaches generally fail to produce calibrated prediction intervals. We identify that this stems from conflating ensemble variance with aleatoric uncertainty and ignoring local spatial context.
>   To resolve this, we introduce Attentive Neural Processes (ANPs), a probabilistic meta-learning framework that explicitly conditions predictions on local observation sets and geospatial foundation model embeddings. Unlike static ensembles, ANPs learn a flexible spatial covariance function, allowing uncertainty estimates to expand in complex landscapes and contract in homogeneous areas. We validate this approach across five distinct biomes ranging from Tropical Amazonian forests to Boreal and Alpine ecosystems, demonstrating that ANPs achieve competitive accuracy while maintaining near-ideal uncertainty calibration. We demonstrate the operational utility of the method through few-shot adaptation, where the model recovers most of the performance gap in cross-region transfer using minimal local data. This work provides a scalable, theoretically rigorous alternative to ensemble variance for continental scale earth observation.


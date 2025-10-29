---
layout: default
title: 50 Years of Water Body Monitoring: The Case of Qaraaoun Reservoir, Lebanon
---

# 50 Years of Water Body Monitoring: The Case of Qaraaoun Reservoir, Lebanon
**arXiv**：[2510.24413v1](https://arxiv.org/abs/2510.24413) · [PDF](https://arxiv.org/pdf/2510.24413.pdf)  
**作者**：Ali Ahmad Faour, Nabil Amacha, Ali J. Ghandour  

**一句话要点**：提出基于卫星影像与机器学习的无传感器方法，以监测黎巴嫩Qaraaoun水库体积。

**关键词**：水体监测, 卫星影像分割, 支持向量回归, 无传感器方法, 水库体积估计

## 3 点简述
- 核心问题：水库体积监测依赖传感器，但易故障且维护困难。
- 方法要点：结合卫星影像、新水分割指数和SVR模型估计体积。
- 实验或效果：模型误差低于1.5%，与实测数据高度一致。

## 摘要（原文）

> The sustainable management of the Qaraaoun Reservoir, the largest surface
> water body in Lebanon located in the Bekaa Plain, depends on reliable
> monitoring of its storage volume despite frequent sensor malfunctions and
> limited maintenance capacity. This study introduces a sensor-free approach that
> integrates open-source satellite imagery, advanced water-extent segmentation,
> and machine learning to estimate the reservoir surface area and volume in near
> real time. Sentinel-2 and Landsat images are processed, where surface water is
> delineated using a newly proposed water segmentation index. A machine learning
> model based on Support Vector Regression (SVR) is trained on a curated dataset
> that includes water surface area, water level, and water volume calculations
> using a reservoir bathymetry survey. The model is then able to estimate
> reservoir volume relying solely on surface area extracted from satellite
> imagery, without the need for ground measurements. Water segmentation using the
> proposed index aligns with ground truth for more than 95 percent of the
> shoreline. Hyperparameter tuning with GridSearchCV yields an optimized SVR
> performance with error under 1.5 percent of full reservoir capacity and
> coefficients of determination exceeding 0.98. These results demonstrate the
> robustness and cost-effectiveness of the method, offering a practical solution
> for continuous, sensor-independent monitoring of reservoir storage. The
> proposed methodology can be replicated for other water bodies, and the
> resulting 50 years of time-series data is valuable for research on climate
> change and environmental patterns.


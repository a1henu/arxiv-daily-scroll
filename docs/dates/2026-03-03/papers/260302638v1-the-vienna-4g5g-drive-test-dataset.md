---
layout: default
title: The Vienna 4G/5G Drive-Test Dataset
---

# The Vienna 4G/5G Drive-Test Dataset
**arXiv**：[2603.02638v1](https://arxiv.org/abs/2603.02638) · [PDF](https://arxiv.org/pdf/2603.02638.pdf)  
**作者**：Wilfried Wiedner, Lukas Eller, Mariam Mussbah, Dominik Rössler, Valerian Maresch, Philipp Svoboda, Markus Rupp  

**一句话要点**：提出维也纳4G/5G路测数据集以解决移动网络机器学习中缺乏大规模真实世界数据的问题。

**关键词**：移动网络数据集, 4G/5G测量, 射线追踪校准, 环境感知学习, 传播建模, 城市级数据

## 3 点简述
- 核心问题：移动网络分析、规划和优化的机器学习常受限于缺乏大规模、全面的真实世界数据集。
- 方法要点：提供城市级开放数据集，结合被动宽带扫描仪观测和主动手机日志，支持网络侧和用户侧视图。
- 实验或效果：数据集包括基站部署描述符、高分辨率建筑和地形模型，支持环境感知学习、传播建模和射线追踪校准。

## 摘要（原文）

> Machine learning for mobile network analysis, planning, and optimization is often limited by the lack of large, comprehensive real-world datasets. This paper introduces the Vienna 4G/5G Drive-Test Dataset, a city-scale open dataset of georeferenced Long Term Evolution (LTE) and 5G New Radio (NR) measurements collected across Vienna, Austria. The dataset combines passive wideband scanner observations with active handset logs, providing complementary network-side and user-side views of deployed radio access networks. The measurements cover diverse urban and suburban settings and are aligned with time and location information to support consistent evaluation. For a representative subset of base stations (BSs), we provide inferred deployment descriptors, including estimated BS locations, sector azimuths, and antenna heights. The release further includes high-resolution building and terrain models, enabling geometry-conditioned learning and calibration of deterministic approaches such as ray tracing. To facilitate practical reuse, the data are organized into scanner, handset, estimated cell information, and city-model components, and the accompanying documentation describes the available fields and intended joins between them. The dataset enables reproducible benchmarking across environment-aware learning, propagation modeling, coverage analysis, and ray-tracing calibration workflows.


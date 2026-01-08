---
layout: default
title: Local Intrinsic Dimensionality of Ground Motion Data for Early Detection of Complex Catastrophic Slope Failure
---

# Local Intrinsic Dimensionality of Ground Motion Data for Early Detection of Complex Catastrophic Slope Failure
**arXiv**：[2601.03569v1](https://arxiv.org/abs/2601.03569) · [PDF](https://arxiv.org/pdf/2601.03569.pdf)  
**作者**：Yuansan Liu, Antoinette Tordesillas, James Bailey  

**一句话要点**：提出时空局部内在维度方法以提升滑坡早期检测精度与提前时间

**关键词**：滑坡检测, 局部内在维度, 时空建模, 异常检测, 地质灾害监测

## 3 点简述
- 核心问题：现有滑坡检测方法难以同时捕捉空间相关性与时间动态性，影响复杂滑坡的早期识别。
- 方法要点：扩展sLID，通过速度增强、贝叶斯空间融合和时间建模tLID，构建统一时空框架stLID。
- 实验或效果：stLID在检测精度和提前时间上均优于现有方法，验证了其有效性。

## 摘要（原文）

> Local Intrinsic Dimensionality (LID) has shown strong potential for identifying anomalies and outliers in high-dimensional data across a wide range of real-world applications, including landslide failure detection in granular media. Early and accurate identification of failure zones in landslide-prone areas is crucial for effective geohazard mitigation. While existing approaches typically rely on surface displacement data analyzed through statistical or machine learning techniques, they often fall short in capturing both the spatial correlations and temporal dynamics that are inherent in such data. To address this gap, we focus on ground-monitored landslides and introduce a novel approach that jointly incorporates spatial and temporal information, enabling the detection of complex landslides and including multiple successive failures occurring in distinct areas of the same slope. To be specific, our method builds upon an existing LID-based technique, known as sLID. We extend its capabilities in three key ways. (1) Kinematic enhancement: we incorporate velocity into the sLID computation to better capture short-term temporal dependencies and deformation rate relationships. (2) Spatial fusion: we apply Bayesian estimation to aggregate sLID values across spatial neighborhoods, effectively embedding spatial correlations into the LID scores. (3) Temporal modeling: we introduce a temporal variant, tLID, that learns long-term dynamics from time series data, providing a robust temporal representation of displacement behavior. Finally, we integrate both components into a unified framework, referred to as spatiotemporal LID (stLID), to identify samples that are anomalous in either or both dimensions. Extensive experiments show that stLID consistently outperforms existing methods in failure detection precision and lead-time.


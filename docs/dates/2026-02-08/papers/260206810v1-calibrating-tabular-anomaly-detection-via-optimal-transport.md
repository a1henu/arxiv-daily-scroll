---
layout: default
title: Calibrating Tabular Anomaly Detection via Optimal Transport
---

# Calibrating Tabular Anomaly Detection via Optimal Transport
**arXiv**：[2602.06810v1](https://arxiv.org/abs/2602.06810) · [PDF](https://arxiv.org/pdf/2602.06810.pdf)  
**作者**：Hangting Ye, He Zhao. Wei Fan, Xiaozhuang Song, Dandan Guo, Yi Chang, Hongyuan Zha  

**一句话要点**：提出CTAD框架，通过最优运输校准提升任意表格异常检测器的性能

**关键词**：表格异常检测, 最优运输, 模型无关校准, 后处理框架, 分布兼容性

## 3 点简述
- 表格数据异质性导致异常检测方法泛化性差，需校准以增强性能
- CTAD利用随机采样和K-means质心构建正常数据分布，通过最优运输距离测量测试样本的破坏程度进行校准
- 在34个数据集和7类检测器上验证，CTAD显著提升性能，无需额外调参

## 摘要（原文）

> Tabular anomaly detection (TAD) remains challenging due to the heterogeneity of tabular data: features lack natural relationships, vary widely in distribution and scale, and exhibit diverse types. Consequently, each TAD method makes implicit assumptions about anomaly patterns that work well on some datasets but fail on others, and no method consistently outperforms across diverse scenarios. We present CTAD (Calibrating Tabular Anomaly Detection), a model-agnostic post-processing framework that enhances any existing TAD detector through sample-specific calibration. Our approach characterizes normal data via two complementary distributions, i.e., an empirical distribution from random sampling and a structural distribution from K-means centroids, and measures how adding a test sample disrupts their compatibility using Optimal Transport (OT) distance. Normal samples maintain low disruption while anomalies cause high disruption, providing a calibration signal to amplify detection. We prove that OT distance has a lower bound proportional to the test sample's distance from centroids, and establish that anomalies systematically receive higher calibration scores than normals in expectation, explaining why the method generalizes across datasets. Extensive experiments on 34 diverse tabular datasets with 7 representative detectors spanning all major TAD categories (density estimation, classification, reconstruction, and isolation-based methods) demonstrate that CTAD consistently improves performance with statistical significance. Remarkably, CTAD enhances even state-of-the-art deep learning methods and shows robust performance across diverse hyperparameter settings, requiring no additional tuning for practical deployment.


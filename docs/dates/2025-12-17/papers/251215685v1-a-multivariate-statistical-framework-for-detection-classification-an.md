---
layout: default
title: A Multivariate Statistical Framework for Detection, Classification and Pre-localization of Anomalies in Water Distribution Networks
---

# A Multivariate Statistical Framework for Detection, Classification and Pre-localization of Anomalies in Water Distribution Networks
**arXiv**：[2512.15685v1](https://arxiv.org/abs/2512.15685) · [PDF](https://arxiv.org/pdf/2512.15685.pdf)  
**作者**：Oleg Melnikov, Yurii Dorofieiev, Yurii Shakhnovskiy, Huy Truong, Victoria Degeler  

**一句话要点**：提出SICAMS框架，基于多元统计分析检测、分类和初步定位供水管网异常。

**关键词**：供水管网异常检测, 多元统计分析, Hotelling's T²统计, 泄漏分类, 传感器数据白化, 粗粒度定位

## 3 点简述
- 核心问题：供水管网中异常（如泄漏、传感器故障）的检测、分类和初步定位。
- 方法要点：使用白化变换消除空间相关性，构建Hotelling's T²统计量进行假设检验，并开发启发式算法分类异常。
- 实验或效果：在BattLeDIM L-Town数据集上验证，显示高灵敏度和可靠性，适用于实际环境。

## 摘要（原文）

> This paper presents a unified framework, for the detection, classification, and preliminary localization of anomalies in water distribution networks using multivariate statistical analysis. The approach, termed SICAMS (Statistical Identification and Classification of Anomalies in Mahalanobis Space), processes heterogeneous pressure and flow sensor data through a whitening transformation to eliminate spatial correlations among measurements. Based on the transformed data, the Hotelling's $T^2$ statistic is constructed, enabling the formulation of anomaly detection as a statistical hypothesis test of network conformity to normal operating conditions. It is shown that Hotelling's $T^2$ statistic can serve as an integral indicator of the overall "health" of the system, exhibiting correlation with total leakage volume, and thereby enabling approximate estimation of water losses via a regression model. A heuristic algorithm is developed to analyze the $T^2$ time series and classify detected anomalies into abrupt leaks, incipient leaks, and sensor malfunctions. Furthermore, a coarse leak localization method is proposed, which ranks sensors according to their statistical contribution and employs Laplacian interpolation to approximate the affected region within the network. Application of the proposed framework to the BattLeDIM L-Town benchmark dataset demonstrates high sensitivity and reliability in leak detection, maintaining robust performance even under multiple leaks. These capabilities make the method applicable to real-world operational environments without the need for a calibrated hydraulic model.


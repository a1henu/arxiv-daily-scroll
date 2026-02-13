---
layout: default
title: Data-Driven Trajectory Imputation for Vessel Mobility Analysis
---

# Data-Driven Trajectory Imputation for Vessel Mobility Analysis
**arXiv**：[2602.11890v1](https://arxiv.org/abs/2602.11890) · [PDF](https://arxiv.org/pdf/2602.11890.pdf)  
**作者**：Giannis Spiliopoulos, Alexandros Troupiotis-Kapeliaris, Kostas Patroumpas, Nikolaos Liapis, Dimitrios Skoutas, Dimitris Zissis, Nikos Bikakis  

**一句话要点**：提出HABIT框架以解决船舶轨迹数据缺失问题

**关键词**：轨迹插补, 船舶轨迹分析, AIS数据处理, 数据驱动方法, 运动模式索引

## 3 点简述
- 船舶轨迹数据常因AIS覆盖限制或传输中断出现大间隙，影响分析准确性
- HABIT基于历史AIS数据提取、分析和索引运动模式，实现轻量可配置的轨迹插补
- 实验表明HABIT在精度上与基线方法相当，延迟更低，并考虑船舶特性和运动模式

## 摘要（原文）

> Modeling vessel activity at sea is critical for a wide range of applications, including route planning, transportation logistics, maritime safety, and environmental monitoring. Over the past two decades, the Automatic Identification System (AIS) has enabled real-time monitoring of hundreds of thousands of vessels, generating huge amounts of data daily. One major challenge in using AIS data is the presence of large gaps in vessel trajectories, often caused by coverage limitations or intentional transmission interruptions. These gaps can significantly degrade data quality, resulting in inaccurate or incomplete analysis. State-of-the-art imputation approaches have mainly been devised to tackle gaps in vehicle trajectories, even when the underlying road network is not considered. But the motion patterns of sailing vessels differ substantially, e.g., smooth turns, maneuvering near ports, or navigating in adverse weather conditions. In this application paper, we propose HABIT, a lightweight, configurable H3 Aggregation-Based Imputation framework for vessel Trajectories. This data-driven framework provides a valuable means to impute missing trajectory segments by extracting, analyzing, and indexing motion patterns from historical AIS data. Our empirical study over AIS data across various timeframes, densities, and vessel types reveals that HABIT produces maritime trajectory imputations performing comparably to baseline methods in terms of accuracy, while performing better in terms of latency while accounting for vessel characteristics and their motion patterns.


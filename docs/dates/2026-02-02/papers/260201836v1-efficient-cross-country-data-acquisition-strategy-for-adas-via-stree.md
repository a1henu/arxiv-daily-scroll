---
layout: default
title: Efficient Cross-Country Data Acquisition Strategy for ADAS via Street-View Imagery
---

# Efficient Cross-Country Data Acquisition Strategy for ADAS via Street-View Imagery
**arXiv**：[2602.01836v1](https://arxiv.org/abs/2602.01836) · [PDF](https://arxiv.org/pdf/2602.01836.pdf)  
**作者**：Yin Wu, Daniel Slieter, Carl Esselborn, Ahmed Abouelazm, Tsung Yuan Tseng, J. Marius Zöllner  

**一句话要点**：提出基于街景图像的跨国家ADAS数据采集策略，以解决传统方法成本高、效率低的问题

**关键词**：ADAS数据采集, 跨国家域适应, 街景图像分析, 兴趣点识别, 交通标志检测, 视觉基础模型

## 3 点简述
- 核心问题：跨国家部署ADAS面临法规、交通设施差异导致的域偏移，传统数据采集成本高
- 方法要点：利用公开街景图像识别兴趣点，提出基于视觉基础模型的KNN特征距离和视觉语言模型的视觉归因两种评分方法
- 实验效果：在交通标志检测任务中，仅用一半目标域数据即达到随机采样可比性能，成本分析显示大规模处理经济可行

## 摘要（原文）

> Deploying ADAS and ADS across countries remains challenging due to differences in legislation, traffic infrastructure, and visual conventions, which introduce domain shifts that degrade perception performance. Traditional cross-country data collection relies on extensive on-road driving, making it costly and inefficient to identify representative locations. To address this, we propose a street-view-guided data acquisition strategy that leverages publicly available imagery to identify places of interest (POI). Two POI scoring methods are introduced: a KNN-based feature distance approach using a vision foundation model, and a visual-attribution approach using a vision-language model. To enable repeatable evaluation, we adopt a collect-detect protocol and construct a co-located dataset by pairing the Zenseact Open Dataset with Mapillary street-view images. Experiments on traffic sign detection, a task particularly sensitive to cross-country variations in sign appearance, show that our approach achieves performance comparable to random sampling while using only half of the target-domain data. We further provide cost estimations for full-country analysis, demonstrating that large-scale street-view processing remains economically feasible. These results highlight the potential of street-view-guided data acquisition for efficient and cost-effective cross-country model adaptation.


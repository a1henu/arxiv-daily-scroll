---
layout: default
title: HeatPrompt: Zero-Shot Vision-Language Modeling of Urban Heat Demand from Satellite Images
---

# HeatPrompt: Zero-Shot Vision-Language Modeling of Urban Heat Demand from Satellite Images
**arXiv**：[2602.20066v1](https://arxiv.org/abs/2602.20066) · [PDF](https://arxiv.org/pdf/2602.20066.pdf)  
**作者**：Kundan Thota, Xuanhao Mu, Thorsten Schlachter, Veit Hagenmeyer  

**一句话要点**：提出HeatPrompt零样本视觉语言框架，利用卫星图像估计城市热需求以支持数据稀缺区域的热规划。

**关键词**：零样本学习, 视觉语言模型, 卫星图像分析, 热需求估计, 城市能源规划

## 3 点简述
- 核心问题：城市热需求地图缺乏详细建筑级数据，阻碍空间供暖脱碳。
- 方法要点：使用预训练视觉语言模型结合领域特定提示，从卫星图像提取热负荷相关视觉属性。
- 实验或效果：基于提取特征的回归模型相比基线提升R² 93.7%，减少MAE 30%，高影响令牌与高需求区对齐。

## 摘要（原文）

> Accurate heat-demand maps play a crucial role in decarbonizing space heating, yet most municipalities lack detailed building-level data needed to calculate them. We introduce HeatPrompt, a zero-shot vision-language energy modeling framework that estimates annual heat demand using semantic features extracted from satellite images, basic Geographic Information System (GIS), and building-level features. We feed pretrained Large Vision Language Models (VLMs) with a domain-specific prompt to act as an energy planner and extract the visual attributes such as roof age, building density, etc, from the RGB satellite image that correspond to the thermal load. A Multi-Layer Perceptron (MLP) regressor trained on these captions shows an $R^2$ uplift of 93.7% and shrinks the mean absolute error (MAE) by 30% compared to the baseline model. Qualitative analysis shows that high-impact tokens align with high-demand zones, offering lightweight support for heat planning in data-scarce regions.


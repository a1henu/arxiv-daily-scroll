---
layout: default
title: Pixel-Wise Multimodal Contrastive Learning for Remote Sensing Images
---

# Pixel-Wise Multimodal Contrastive Learning for Remote Sensing Images
**arXiv**：[2601.04127v1](https://arxiv.org/abs/2601.04127) · [PDF](https://arxiv.org/pdf/2601.04127.pdf)  
**作者**：Leandro Stival, Ricardo da Silva Torres, Helio Pedrini  

**一句话要点**：提出像素级多模态对比学习框架，以增强遥感图像时间序列的特征提取能力。

**关键词**：遥感图像时间序列, 像素级表示, 多模态对比学习, 自监督学习, 递归图, 植被指数

## 3 点简述
- 核心问题：现有深度学习模型处理卫星图像时间序列时，通常基于整图或完整序列，难以有效捕捉像素级变化。
- 方法要点：利用植被指数时间序列生成递归图作为二维表示，并设计像素级多模态对比学习（PIMC）进行自监督编码。
- 实验或效果：在PASTIS和EuroSAT数据集上验证，像素级预测和分类任务中优于现有方法，提升特征质量。

## 摘要（原文）

> Satellites continuously generate massive volumes of data, particularly for Earth observation, including satellite image time series (SITS). However, most deep learning models are designed to process either entire images or complete time series sequences to extract meaningful features for downstream tasks. In this study, we propose a novel multimodal approach that leverages pixel-wise two-dimensional (2D) representations to encode visual property variations from SITS more effectively. Specifically, we generate recurrence plots from pixel-based vegetation index time series (NDVI, EVI, and SAVI) as an alternative to using raw pixel values, creating more informative representations. Additionally, we introduce PIxel-wise Multimodal Contrastive (PIMC), a new multimodal self-supervision approach that produces effective encoders based on two-dimensional pixel time series representations and remote sensing imagery (RSI). To validate our approach, we assess its performance on three downstream tasks: pixel-level forecasting and classification using the PASTIS dataset, and land cover classification on the EuroSAT dataset. Moreover, we compare our results to state-of-the-art (SOTA) methods on all downstream tasks. Our experimental results show that the use of 2D representations significantly enhances feature extraction from SITS, while contrastive learning improves the quality of representations for both pixel time series and RSI. These findings suggest that our multimodal method outperforms existing models in various Earth observation tasks, establishing it as a robust self-supervision framework for processing both SITS and RSI. Code avaliable on


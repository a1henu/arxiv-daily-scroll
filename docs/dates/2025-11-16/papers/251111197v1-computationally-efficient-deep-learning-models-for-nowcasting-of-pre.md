---
layout: default
title: Computationally-efficient deep learning models for nowcasting of precipitation: A solution for the Weather4cast 2025 challenge
---

# Computationally-efficient deep learning models for nowcasting of precipitation: A solution for the Weather4cast 2025 challenge
**arXiv**：[2511.11197v1](https://arxiv.org/abs/2511.11197) · [PDF](https://arxiv.org/pdf/2511.11197.pdf)  
**作者**：Anushree Bhuskute, Kaushik Gopalan, Jeet Shah  

**一句话要点**：提出基于ConvGRU的迁移学习框架，用于Weather4cast 2025竞赛的短时降水预报。

**关键词**：短时降水预报, ConvGRU模型, 迁移学习, SEVIRI数据, 事件检测, 亮度温度预测

## 3 点简述
- 核心问题：短时降水预报，使用SEVIRI红外通道数据预测未来四小时降雨。
- 方法要点：采用两阶段训练，先预测亮度温度，再非线性映射到降雨率。
- 实验或效果：在累积降雨任务中获第二名，事件预测任务与基线模型表现相当。

## 摘要（原文）

> This study presents a transfer-learning framework based on Convolutional Gated Recurrent Units (ConvGRU) for short-term rainfall prediction in the Weather4Cast 2025 competition. A single SEVIRI infrared channel (10.8 μm wavelength) is used as input, which consists of four observations over a one-hour period. A two-stage training strategy is applied to generate rainfall estimates up to four hours ahead. In the first stage, ConvGRU is trained to forecast the brightness temperatures from SEVIRI, enabling the model to capture relevant spatiotemporal patterns. In the second stage, an empirically derived nonlinear transformation maps the predicted fields to OPERA-compatible rainfall rates.
>   For the event-prediction task, the transformed rainfall forecasts are processed using 3D event detection followed by spatiotemporal feature extraction to identify and characterize precipitation events. Our submission achieved 2nd place in the cumulative rainfall task. Further, the same model was used out-of-the-box for the event prediction task, and resulted in similar scores as the baseline model to the competition.


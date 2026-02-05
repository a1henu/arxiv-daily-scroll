---
layout: default
title: Legendre Memory Unit with A Multi-Slice Compensation Model for Short-Term Wind Speed Forecasting Based on Wind Farm Cluster Data
---

# Legendre Memory Unit with A Multi-Slice Compensation Model for Short-Term Wind Speed Forecasting Based on Wind Farm Cluster Data
**arXiv**：[2602.04782v1](https://arxiv.org/abs/2602.04782) · [PDF](https://arxiv.org/pdf/2602.04782.pdf)  
**作者**：Mumin Zhang, Haochen Zhang, Xin Zhi Khoo, Yilin Zhang, Nuo Chen, Ting Zhang, Junjie Tang  

**一句话要点**：提出WMF-CPK-MSLMU集成模型，基于风电场集群数据实现短期风速预测

**关键词**：风速预测, 风电场集群, Legendre记忆单元, 多切片补偿, 时空相关性, 集成模型

## 3 点简述
- 核心问题：风电场集群短期风速预测对电力系统稳定运行至关重要，需利用时空相关性。
- 方法要点：结合加权均值滤波去噪、Legendre记忆单元建模及基于Kendall秩相关系数的多切片补偿。
- 实验或效果：在不同风电场集群测试中，模型在准确性和鲁棒性上优于现有方法。

## 摘要（原文）

> With more wind farms clustered for integration, the short-term wind speed prediction of such wind farm clusters is critical for normal operation of power systems. This paper focuses on achieving accurate, fast, and robust wind speed prediction by full use of cluster data with spatial-temporal correlation. First, weighted mean filtering (WMF) is applied to denoise wind speed data at the single-farm level. The Legendre memory unit (LMU) is then innovatively applied for the wind speed prediction, in combination with the Compensating Parameter based on Kendall rank correlation coefficient (CPK) of wind farm cluster data, to construct the multi-slice LMU (MSLMU). Finally, an innovative ensemble model WMF-CPK-MSLMU is proposed herein, with three key blocks: data pre-processing, forecasting, and multi-slice compensation. Advantages include: 1) LMU jointly models linear and nonlinear dependencies among farms to capture spatial-temporal correlations through backpropagation; 2) MSLMU enhances forecasting by using CPK-derived weights instead of random initialization, allowing spatial correlations to fully activate hidden nodes across clustered wind farms.; 3) CPK adaptively weights the compensation model in MSLMU and complements missing data spatially, to facilitate the whole model highly accurate and robust. Test results on different wind farm clusters indicate the effectiveness and superiority of proposed ensemble model WMF-CPK-MSLMU in the short-term prediction of wind farm clusters compared to the existing models.


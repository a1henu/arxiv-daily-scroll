---
layout: default
title: STIPP: Space-time in situ postprocessing over the French Alps using proper scoring rules
---

# STIPP: Space-time in situ postprocessing over the French Alps using proper scoring rules
**arXiv**：[2601.02882v1](https://arxiv.org/abs/2601.02882) · [PDF](https://arxiv.org/pdf/2601.02882.pdf)  
**作者**：David Landry, Isabelle Gouttevin, Hugo Merizen, Claire Monteleoni, Anastase Charantonis  

**一句话要点**：提出STIPP模型，通过时空联合预测提升站点网络天气预报的准确性和一致性。

**关键词**：时空后处理, 天气预测, 生成建模, 适当评分规则, 站点网络, 集合预测

## 3 点简述
- 核心问题：传统数值预报或数据驱动模型在站点尺度上精度不足，且统计后处理常破坏时空相关性。
- 方法要点：STIPP结合生成建模和多元适当评分规则，实现时空一致的联合预测，仅需六小时确定性预报输入。
- 实验或效果：相比基线方法，在温度、风、湿度和降水预报上准确性提高，支持小时级集合预测。

## 摘要（原文）

> We propose Space-time in situ postprocessing (STIPP), a machine learning model that generates spatio-temporally consistent weather forecasts for a network of station locations. Gridded forecasts from classical numerical weather prediction or data-driven models often lack the necessary precision due to unresolved local effects. Typical statistical postprocessing methods correct these biases, but often degrade spatio-temporal correlation structures in doing so. Recent works based on generative modeling successfully improve spatial correlation structures but have to forecast every lead time independently. In contrast, STIPP makes joint spatio-temporal forecasts which have increased accuracy for surface temperature, wind, relative humidity and precipitation when compared to baseline methods. It makes hourly ensemble predictions given only a six-hourly deterministic forecast, blending the boundaries of postprocessing and temporal interpolation. By leveraging a multivariate proper scoring rule for training, STIPP contributes to ongoing work data-driven atmospheric models supervised only with distribution marginals.


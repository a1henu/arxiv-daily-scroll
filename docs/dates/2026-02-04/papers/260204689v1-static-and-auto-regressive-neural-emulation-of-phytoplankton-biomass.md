---
layout: default
title: Static and auto-regressive neural emulation of phytoplankton biomass dynamics from physical predictors in the global ocean
---

# Static and auto-regressive neural emulation of phytoplankton biomass dynamics from physical predictors in the global ocean
**arXiv**：[2602.04689v1](https://arxiv.org/abs/2602.04689) · [PDF](https://arxiv.org/pdf/2602.04689.pdf)  
**作者**：Mahima Lakra, Ronan Fablet, Lucas Drumetz, Etienne Pauthenet, Elodie Martinez  

**一句话要点**：提出静态与自回归UNet模型，基于物理预测因子重建和短期预测全球海洋浮游植物生物量动态

**关键词**：浮游植物动态模拟, UNet架构, 自回归预测, 海洋物理预测因子, 深度学习应用, 全球海洋监测

## 3 点简述
- 核心问题：浮游植物动态模拟受限于参数化不足、数据稀疏和海洋过程复杂性，传统模型难以准确预测。
- 方法要点：采用UNet架构，结合卫星观测和环境数据，优于CNN、ConvLSTM和4CastNet，并测试自回归版本以改进时间预测。
- 实验或效果：UNet能再现季节和年际模式，自回归模型在短期预测（≤5个月）有效，但长期性能下降，低估低频变化幅度。

## 摘要（原文）

> Phytoplankton is the basis of marine food webs, driving both ecological processes and global biogeochemical cycles. Despite their ecological and climatic significance, accurately simulating phytoplankton dynamics remains a major challenge for biogeochemical numerical models due to limited parameterizations, sparse observational data, and the complexity of oceanic processes. Here, we explore how deep learning models can be used to address these limitations predicting the spatio-temporal distribution of phytoplankton biomass in the global ocean based on satellite observations and environmental conditions. First, we investigate several deep learning architectures. Among the tested models, the UNet architecture stands out for its ability to reproduce the seasonal and interannual patterns of phytoplankton biomass more accurately than other models like CNNs, ConvLSTM, and 4CastNet. When using one to two months of environmental data as input, UNet performs better, although it tends to underestimate the amplitude of low-frequency changes in phytoplankton biomass. Thus, to improve predictions over time, an auto-regressive version of UNet was also tested, where the model uses its own previous predictions to forecast future conditions. This approach works well for short-term forecasts (up to five months), though its performance decreases for longer time scales. Overall, our study shows that combining ocean physical predictors with deep learning allows for reconstruction and short-term prediction of phytoplankton dynamics. These models could become powerful tools for monitoring ocean health and supporting marine ecosystem management, especially in the context of climate change.


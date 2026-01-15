---
layout: default
title: Searth Transformer: A Transformer Architecture Incorporating Earth's Geospheric Physical Priors for Global Mid-Range Weather Forecasting
---

# Searth Transformer: A Transformer Architecture Incorporating Earth's Geospheric Physical Priors for Global Mid-Range Weather Forecasting
**arXiv**：[2601.09467v1](https://arxiv.org/abs/2601.09467) · [PDF](https://arxiv.org/pdf/2601.09467.pdf)  
**作者**：Tianye Li, Qi Liu, Hao Li, Lei Chen, Wencong Cheng, Fei Zheng, Xiangao Xia, Ya Wang, Gang Huang, Weiwei Wang, Xuan Tong, Ziqing Zu, Yi Fang, Shenming Fu, Jiang Jiang, Haochen Li, Mingxing Li, Jiangjiang Xia  

**一句话要点**：提出Searth Transformer，结合地球物理先验和接力自回归微调，用于全球中程天气预报。

**关键词**：全球天气预报, Transformer架构, 物理先验, 接力自回归微调, 地球系统科学

## 3 点简述
- 现有Transformer模型忽略地球球面几何和纬向周期性，导致信息交换不物理一致。
- Searth Transformer通过窗口自注意力融入纬向周期性和经向边界，实现物理一致的全局信息交换。
- YanTian模型在1度分辨率下精度优于HRES，计算成本降低约200倍，Z500技能预报时间达10.3天。

## 摘要（原文）

> Accurate global medium-range weather forecasting is fundamental to Earth system science. Most existing Transformer-based forecasting models adopt vision-centric architectures that neglect the Earth's spherical geometry and zonal periodicity. In addition, conventional autoregressive training is computationally expensive and limits forecast horizons due to error accumulation. To address these challenges, we propose the Shifted Earth Transformer (Searth Transformer), a physics-informed architecture that incorporates zonal periodicity and meridional boundaries into window-based self-attention for physically consistent global information exchange. We further introduce a Relay Autoregressive (RAR) fine-tuning strategy that enables learning long-range atmospheric evolution under constrained memory and computational budgets. Based on these methods, we develop YanTian, a global medium-range weather forecasting model. YanTian achieves higher accuracy than the high-resolution forecast of the European Centre for Medium-Range Weather Forecasts and performs competitively with state-of-the-art AI models at one-degree resolution, while requiring roughly 200 times lower computational cost than standard autoregressive fine-tuning. Furthermore, YanTian attains a longer skillful forecast lead time for Z500 (10.3 days) than HRES (9 days). Beyond weather forecasting, this work establishes a robust algorithmic foundation for predictive modeling of complex global-scale geophysical circulation systems, offering new pathways for Earth system science.


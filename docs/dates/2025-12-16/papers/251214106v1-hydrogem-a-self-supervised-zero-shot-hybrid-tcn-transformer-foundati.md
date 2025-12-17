---
layout: default
title: HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
**arXiv**：[2512.14106v1](https://arxiv.org/abs/2512.14106) · [PDF](https://arxiv.org/pdf/2512.14106.pdf)  
**作者**：Ijaz Ul Haq, Byung Suk Lee, Julia N. Perdrial, David Baude  

**一句话要点**：提出HydroGEM基础模型以解决大陆尺度河流流量数据质量控制的自动化难题

**关键词**：河流流量质量控制, 自监督学习, TCN-Transformer混合架构, 零样本迁移, 基础模型, 水文监测

## 3 点简述
- 核心问题：实时河流监测网络数据量大，远程传感器质量控制依赖人工，效率低下。
- 方法要点：采用自监督预训练与合成异常微调，结合TCN-Transformer混合架构捕获时空模式。
- 实验或效果：在合成测试中F1达0.792，零样本迁移至加拿大站点F1为0.586，优于现有方法。

## 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.


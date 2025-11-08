---
layout: default
title: Landslide Hazard Mapping with Geospatial Foundation Models: Geographical Generalizability, Data Scarcity, and Band Adaptability
---

# Landslide Hazard Mapping with Geospatial Foundation Models: Geographical Generalizability, Data Scarcity, and Band Adaptability
**arXiv**：[2511.04474v1](https://arxiv.org/abs/2511.04474) · [PDF](https://arxiv.org/pdf/2511.04474.pdf)  
**作者**：Wenwen Li, Sizhe Wang, Hyunho Lee, Chenyan Lu, Sujit Roy, Rahul Ramachandran, Chia-Yu Hsu  

**一句话要点**：提出地理空间基础模型框架以解决滑坡灾害制图中的泛化与数据稀缺问题

**关键词**：滑坡灾害制图, 地理空间基础模型, 泛化性分析, 数据稀缺适应, 遥感图像处理

## 3 点简述
- 核心问题：传统深度学习模型在跨传感器、区域及数据稀缺时性能下降
- 方法要点：基于Prithvi-EO-2.0构建三轴分析框架，结合预训练与微调
- 实验或效果：模型在泛化性、光谱适应性和标签稀缺下优于多种基线模型

## 摘要（原文）

> Landslides cause severe damage to lives, infrastructure, and the environment,
> making accurate and timely mapping essential for disaster preparedness and
> response. However, conventional deep learning models often struggle when
> applied across different sensors, regions, or under conditions of limited
> training data. To address these challenges, we present a three-axis analytical
> framework of sensor, label, and domain for adapting geospatial foundation
> models (GeoFMs), focusing on Prithvi-EO-2.0 for landslide mapping. Through a
> series of experiments, we show that it consistently outperforms task-specific
> CNNs (U-Net, U-Net++), vision transformers (Segformer, SwinV2-B), and other
> GeoFMs (TerraMind, SatMAE). The model, built on global pretraining,
> self-supervision, and adaptable fine-tuning, proved resilient to spectral
> variation, maintained accuracy under label scarcity, and generalized more
> reliably across diverse datasets and geographic settings. Alongside these
> strengths, we also highlight remaining challenges such as computational cost
> and the limited availability of reusable AI-ready training data for landslide
> research. Overall, our study positions GeoFMs as a step toward more robust and
> scalable approaches for landslide risk reduction and environmental monitoring.


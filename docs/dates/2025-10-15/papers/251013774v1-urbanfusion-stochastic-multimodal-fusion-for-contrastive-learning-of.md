---
layout: default
title: UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations
---

# UrbanFusion: Stochastic Multimodal Fusion for Contrastive Learning of Robust Spatial Representations
**arXiv**：[2510.13774v1](https://arxiv.org/abs/2510.13774) · [PDF](https://arxiv.org/pdf/2510.13774.pdf)  
**作者**：Dominik J. Mühlematter, Lin Che, Ye Hong, Martin Raubal, Nina Wiedemann  

**一句话要点**：提出UrbanFusion模型，通过随机多模态融合学习稳健空间表示以预测城市现象

**关键词**：空间表示学习, 多模态融合, 地理人工智能, 城市预测, Transformer模型

## 3 点简述
- 核心问题：现有空间基础模型模态有限且缺乏多模态融合能力，难以整合地理数据预测城市现象
- 方法要点：使用模态特定编码器和Transformer融合模块，集成街景、遥感等多模态输入
- 实验或效果：在41个任务和56个城市评估中，优于先进模型，泛化能力强且支持灵活模态输入

## 摘要（原文）

> Forecasting urban phenomena such as housing prices and public health
> indicators requires the effective integration of various geospatial data.
> Current methods primarily utilize task-specific models, while recent foundation
> models for spatial representations often support only limited modalities and
> lack multimodal fusion capabilities. To overcome these challenges, we present
> UrbanFusion, a Geo-Foundation Model (GeoFM) that features Stochastic Multimodal
> Fusion (SMF). The framework employs modality-specific encoders to process
> different types of inputs, including street view imagery, remote sensing data,
> cartographic maps, and points of interest (POIs) data. These multimodal inputs
> are integrated via a Transformer-based fusion module that learns unified
> representations. An extensive evaluation across 41 tasks in 56 cities worldwide
> demonstrates UrbanFusion's strong generalization and predictive performance
> compared to state-of-the-art GeoAI models. Specifically, it 1) outperforms
> prior foundation models on location-encoding, 2) allows multimodal input during
> inference, and 3) generalizes well to regions unseen during training.
> UrbanFusion can flexibly utilize any subset of available modalities for a given
> location during both pretraining and inference, enabling broad applicability
> across diverse data availability scenarios. All source code is available at
> https://github.com/DominikM198/UrbanFusion.


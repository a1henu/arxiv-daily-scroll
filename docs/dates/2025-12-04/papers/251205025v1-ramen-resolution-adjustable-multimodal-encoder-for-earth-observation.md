---
layout: default
title: RAMEN: Resolution-Adjustable Multimodal Encoder for Earth Observation
---

# RAMEN: Resolution-Adjustable Multimodal Encoder for Earth Observation
**arXiv**：[2512.05025v1](https://arxiv.org/abs/2512.05025) · [PDF](https://arxiv.org/pdf/2512.05025.pdf)  
**作者**：Nicolas Houdré, Diego Marcos, Hugo Riffaud de Turckheim, Dino Ienco, Laurent Wendling, Camille Kurtz, Sylvain Lobry  

**一句话要点**：提出RAMEN以解决地球观测中多模态数据分辨率固定和传感器依赖的表示学习问题。

**关键词**：地球观测, 多模态编码器, 分辨率可调, 传感器无关, 表示学习, Transformer

## 3 点简述
- 核心问题：现有基础模型对固定输入分辨率或传感器特定编码器的依赖，限制了跨异构地球观测模态的泛化能力。
- 方法要点：RAMEN作为分辨率可调的多模态编码器，以传感器无关方式学习共享视觉表示，将空间分辨率定义为可控输出参数。
- 实验或效果：在PANGAEA基准测试中，RAMEN优于更大规模的最先进模型，有效迁移到已知和未见传感器配置。

## 摘要（原文）

> Earth observation (EO) data spans a wide range of spatial, spectral, and temporal resolutions, from high-resolution optical imagery to low resolution multispectral products or radar time series. While recent foundation models have improved multimodal integration for learning meaningful representations, they often expect fixed input resolutions or are based on sensor-specific encoders limiting generalization across heterogeneous EO modalities. To overcome these limitations we introduce RAMEN, a resolution-adjustable multimodal encoder that learns a shared visual representation across EO data in a fully sensor-agnostic manner. RAMEN treats the modality and spatial and temporal resolutions as key input data features, enabling coherent analysis across modalities within a unified latent space. Its main methodological contribution is to define spatial resolution as a controllable output parameter, giving users direct control over the desired level of detail at inference and allowing explicit trade-offs between spatial precision and computational cost. We train a single, unified transformer encoder reconstructing masked multimodal EO data drawn from diverse sources, ensuring generalization across sensors and resolutions. Once pretrained, RAMEN transfers effectively to both known and unseen sensor configurations and outperforms larger state-of-the-art models on the community-standard PANGAEA benchmark, containing various multi-sensor and multi-resolution downstream tasks. Our code and pretrained model are available at https://github.com/nicolashoudre/RAMEN.


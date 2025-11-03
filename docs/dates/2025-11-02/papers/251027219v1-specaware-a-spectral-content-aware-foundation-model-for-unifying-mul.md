---
layout: default
title: SpecAware: A Spectral-Content Aware Foundation Model for Unifying Multi-Sensor Learning in Hyperspectral Remote Sensing Mapping
---

# SpecAware: A Spectral-Content Aware Foundation Model for Unifying Multi-Sensor Learning in Hyperspectral Remote Sensing Mapping
**arXiv**：[2510.27219v1](https://arxiv.org/abs/2510.27219) · [PDF](https://arxiv.org/pdf/2510.27219.pdf)  
**作者**：Renjie Ji, Xue Wang, Chao Niu, Wen Zhang, Yong Mei, Kun Tan  

**一句话要点**：提出SpecAware以统一多传感器高光谱遥感映射中的学习问题

**关键词**：高光谱成像, 多传感器学习, 基础模型, 元属性融合, 超网络编码, 遥感映射

## 3 点简述
- 高光谱数据异质性阻碍通用模型开发，现有方法忽视传感器元属性指导
- 设计元内容感知模块和超嵌入模块，动态生成条件编码以处理可变光谱通道
- 在六个数据集上验证，在土地覆盖分割、变化检测和场景分类中表现优异

## 摘要（原文）

> Hyperspectral imaging (HSI) is a vital tool for fine-grained land-use and
> land-cover (LULC) mapping. However, the inherent heterogeneity of HSI data has
> long posed a major barrier to developing generalized models via joint training.
> Although HSI foundation models have shown promise for different downstream
> tasks, the existing approaches typically overlook the critical guiding role of
> sensor meta-attributes, and struggle with multi-sensor training, limiting their
> transferability. To address these challenges, we propose SpecAware, which is a
> novel hyperspectral spectral-content aware foundation model for unifying
> multi-sensor learning for HSI mapping. We also constructed the Hyper-400K
> dataset to facilitate this research, which is a new large-scale, high-quality
> benchmark dataset with over 400k image patches from diverse airborne AVIRIS
> sensors. The core of SpecAware is a two-step hypernetwork-driven encoding
> process for HSI data. Firstly, we designed a meta-content aware module to
> generate a unique conditional input for each HSI patch, tailored to each
> spectral band of every sample by fusing the sensor meta-attributes and its own
> image content. Secondly, we designed the HyperEmbedding module, where a
> sample-conditioned hypernetwork dynamically generates a pair of matrix factors
> for channel-wise encoding, consisting of adaptive spatial pattern extraction
> and latent semantic feature re-projection. Thus, SpecAware gains the ability to
> perceive and interpret spatial-spectral features across diverse scenes and
> sensors. This, in turn, allows SpecAware to adaptively process a variable
> number of spectral channels, establishing a unified framework for joint
> pre-training. Extensive experiments on six datasets demonstrate that SpecAware
> can learn superior feature representations, excelling in land-cover semantic
> segmentation classification, change detection, and scene classification.


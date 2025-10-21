---
layout: default
title: Towards a Generalizable Fusion Architecture for Multimodal Object Detection
---

# Towards a Generalizable Fusion Architecture for Multimodal Object Detection
**arXiv**：[2510.17078v1](https://arxiv.org/abs/2510.17078) · [PDF](https://arxiv.org/pdf/2510.17078.pdf)  
**作者**：Jad Berjawi, Yoann Dupas, Christophe C'erin  

**一句话要点**：提出FMCAF架构以增强RGB与红外图像融合，提升多模态目标检测的泛化性。

**关键词**：多模态目标检测, 图像融合, 跨注意力机制, 频域滤波, 泛化性提升

## 3 点简述
- 多模态目标检测在挑战条件下依赖多传感器互补，但传统方法泛化性不足。
- FMCAF结合频域滤波与跨注意力融合，抑制冗余特征并促进模态间特征共享。
- 在LLVIP和VEDAI数据集上，FMCAF优于传统融合方法，提升mAP@50指标。

## 摘要（原文）

> Multimodal object detection improves robustness in chal- lenging conditions
> by leveraging complementary cues from multiple sensor modalities. We introduce
> Filtered Multi- Modal Cross Attention Fusion (FMCAF), a preprocess- ing
> architecture designed to enhance the fusion of RGB and infrared (IR) inputs.
> FMCAF combines a frequency- domain filtering block (Freq-Filter) to suppress
> redun- dant spectral features with a cross-attention-based fusion module (MCAF)
> to improve intermodal feature sharing. Unlike approaches tailored to specific
> datasets, FMCAF aims for generalizability, improving performance across
> different multimodal challenges without requiring dataset- specific tuning. On
> LLVIP (low-light pedestrian detec- tion) and VEDAI (aerial vehicle detection),
> FMCAF outper- forms traditional fusion (concatenation), achieving +13.9% mAP@50
> on VEDAI and +1.1% on LLVIP. These results support the potential of FMCAF as a
> flexible foundation for robust multimodal fusion in future detection pipelines.


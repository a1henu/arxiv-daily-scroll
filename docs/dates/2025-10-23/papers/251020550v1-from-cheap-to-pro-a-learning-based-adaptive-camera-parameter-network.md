---
layout: default
title: From Cheap to Pro: A Learning-based Adaptive Camera Parameter Network for Professional-Style Imaging
---

# From Cheap to Pro: A Learning-based Adaptive Camera Parameter Network for Professional-Style Imaging
**arXiv**：[2510.20550v1](https://arxiv.org/abs/2510.20550) · [PDF](https://arxiv.org/pdf/2510.20550.pdf)  
**作者**：Fuchen Li, Yansong Du, Wenbo Cheng, Xiaoxia Zhou, Sen Yin  

**一句话要点**：提出ACamera-Net以解决消费级相机在复杂光照下图像质量不稳定的问题

**关键词**：相机参数调整, 图像质量增强, 实时推理, 边缘设备, 自适应网络

## 3 点简述
- 消费级相机在低光、高动态范围等复杂光照下易出现曝光不足和色彩偏差
- 设计轻量级网络直接预测RAW输入的曝光和白平衡参数，无需额外增强模块
- 实验表明模型提升图像质量并稳定感知输出，优于传统自动模式和基线方法

## 摘要（原文）

> Consumer-grade camera systems often struggle to maintain stable image quality
> under complex illumination conditions such as low light, high dynamic range,
> and backlighting, as well as spatial color temperature variation. These issues
> lead to underexposure, color casts, and tonal inconsistency, which degrade the
> performance of downstream vision tasks. To address this, we propose
> ACamera-Net, a lightweight and scene-adaptive camera parameter adjustment
> network that directly predicts optimal exposure and white balance from RAW
> inputs. The framework consists of two modules: ACamera-Exposure, which
> estimates ISO to alleviate underexposure and contrast loss, and ACamera-Color,
> which predicts correlated color temperature and gain factors for improved color
> consistency. Optimized for real-time inference on edge devices, ACamera-Net can
> be seamlessly integrated into imaging pipelines. Trained on diverse real-world
> data with annotated references, the model generalizes well across lighting
> conditions. Extensive experiments demonstrate that ACamera-Net consistently
> enhances image quality and stabilizes perception outputs, outperforming
> conventional auto modes and lightweight baselines without relying on additional
> image enhancement modules.


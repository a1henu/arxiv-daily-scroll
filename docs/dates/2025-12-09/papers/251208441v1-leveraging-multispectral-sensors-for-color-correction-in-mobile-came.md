---
layout: default
title: Leveraging Multispectral Sensors for Color Correction in Mobile Cameras
---

# Leveraging Multispectral Sensors for Color Correction in Mobile Cameras
**arXiv**：[2512.08441v1](https://arxiv.org/abs/2512.08441) · [PDF](https://arxiv.org/pdf/2512.08441.pdf)  
**作者**：Luca Cogo, Marco Buzzelli, Simone Bianco, Javier Vazquez-Corral, Raimondo Schettini  

**一句话要点**：提出统一学习框架，利用多光谱传感器提升移动相机色彩校正精度

**关键词**：多光谱成像, 色彩校正, 端到端学习, 移动相机, 传感器融合, 图像处理

## 3 点简述
- 核心问题：现有方法多阶段处理色彩校正，早期丢弃多光谱数据，导致信息利用不足
- 方法要点：构建端到端学习框架，联合高分辨率RGB与低分辨率多光谱传感器数据，统一模型处理
- 实验或效果：通过重构两种先进架构验证，在自建数据集上实验，色彩误差降低达50%

## 摘要（原文）

> Recent advances in snapshot multispectral (MS) imaging have enabled compact, low-cost spectral sensors for consumer and mobile devices. By capturing richer spectral information than conventional RGB sensors, these systems can enhance key imaging tasks, including color correction. However, most existing methods treat the color correction pipeline in separate stages, often discarding MS data early in the process. We propose a unified, learning-based framework that (i) performs end-to-end color correction and (ii) jointly leverages data from a high-resolution RGB sensor and an auxiliary low-resolution MS sensor. Our approach integrates the full pipeline within a single model, producing coherent and color-accurate outputs. We demonstrate the flexibility and generality of our framework by refactoring two different state-of-the-art image-to-image architectures. To support training and evaluation, we construct a dedicated dataset by aggregating and repurposing publicly available spectral datasets, rendering under multiple RGB camera sensitivities. Extensive experiments show that our approach improves color accuracy and stability, reducing error by up to 50% compared to RGB-only and MS-driven baselines. Datasets, code, and models will be made available upon acceptance.


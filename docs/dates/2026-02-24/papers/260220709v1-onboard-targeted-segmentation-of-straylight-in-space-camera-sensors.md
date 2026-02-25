---
layout: default
title: Onboard-Targeted Segmentation of Straylight in Space Camera Sensors
---

# Onboard-Targeted Segmentation of Straylight in Space Camera Sensors
**arXiv**：[2602.20709v1](https://arxiv.org/abs/2602.20709) · [PDF](https://arxiv.org/pdf/2602.20709.pdf)  
**作者**：Riccardo Gallon, Fabian Schiemenz, Alessandra Menicucci, Eberhard Gill  

**一句话要点**：提出基于AI的星载相机杂散光语义分割方法，针对资源受限硬件部署。

**关键词**：语义分割, 星载相机, 杂散光检测, 资源受限硬件, 预训练泛化, 系统级评估

## 3 点简述
- 核心问题：分割太阳引起的星载相机视场外杂散光，处理空间数据稀缺。
- 方法要点：使用DeepLabV3与MobileNetV3，通过Flare7k++预训练提升泛化能力。
- 实验或效果：开发系统级评估指标，针对星载导航管道接口优化性能。

## 摘要（原文）

> This study details an artificial intelligence (AI)-based methodology for the semantic segmentation of space camera faults. Specifically, we address the segmentation of straylight effects induced by solar presence around the camera's Field of View (FoV). Anomalous images are sourced from our published dataset. Our approach emphasizes generalization across diverse flare textures, leveraging pre-training on a public dataset (Flare7k++) including flares in various non-space contexts to mitigate the scarcity of realistic space-specific data. A DeepLabV3 model with MobileNetV3 backbone performs the segmentation task. The model design targets deployment in spacecraft resource-constrained hardware. Finally, based on a proposed interface between our model and the onboard navigation pipeline, we develop custom metrics to assess the model's performance in the system-level context.


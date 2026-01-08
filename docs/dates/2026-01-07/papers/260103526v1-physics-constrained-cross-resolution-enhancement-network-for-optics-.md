---
layout: default
title: Physics-Constrained Cross-Resolution Enhancement Network for Optics-Guided Thermal UAV Image Super-Resolution
---

# Physics-Constrained Cross-Resolution Enhancement Network for Optics-Guided Thermal UAV Image Super-Resolution
**arXiv**：[2601.03526v1](https://arxiv.org/abs/2601.03526) · [PDF](https://arxiv.org/pdf/2601.03526.pdf)  
**作者**：Zhicheng Zhao, Fengjiao Peng, Jinquan Yan, Wei Lu, Chenglong Li, Jin Tang  

**一句话要点**：提出PCNet以解决光学引导热成像无人机图像超分辨率中的物理不一致性问题

**关键词**：热成像超分辨率, 跨模态增强, 物理约束, 无人机图像, 光学引导

## 3 点简述
- 现有方法压缩光学特征导致高频信息丢失和物理不一致伪影
- PCNet通过跨分辨率互增强模块和物理驱动热传导模块优化特征交互与物理约束
- 在VGTSR2.0和DroneVehicle数据集上显著提升重建质量和下游任务性能

## 摘要（原文）

> Optics-guided thermal UAV image super-resolution has attracted significant research interest due to its potential in all-weather monitoring applications. However, existing methods typically compress optical features to match thermal feature dimensions for cross-modal alignment and fusion, which not only causes the loss of high-frequency information that is beneficial for thermal super-resolution, but also introduces physically inconsistent artifacts such as texture distortions and edge blurring by overlooking differences in the imaging physics between modalities. To address these challenges, we propose PCNet to achieve cross-resolution mutual enhancement between optical and thermal modalities, while physically constraining the optical guidance process via thermal conduction to enable robust thermal UAV image super-resolution. In particular, we design a Cross-Resolution Mutual Enhancement Module (CRME) to jointly optimize thermal image super-resolution and optical-to-thermal modality conversion, facilitating effective bidirectional feature interaction across resolutions while preserving high-frequency optical priors. Moreover, we propose a Physics-Driven Thermal Conduction Module (PDTM) that incorporates two-dimensional heat conduction into optical guidance, modeling spatially-varying heat conduction properties to prevent inconsistent artifacts. In addition, we introduce a temperature consistency loss that enforces regional distribution consistency and boundary gradient smoothness to ensure generated thermal images align with real-world thermal radiation principles. Extensive experiments on VGTSR2.0 and DroneVehicle datasets demonstrate that PCNet significantly outperforms state-of-the-art methods on both reconstruction quality and downstream tasks including semantic segmentation and object detection.


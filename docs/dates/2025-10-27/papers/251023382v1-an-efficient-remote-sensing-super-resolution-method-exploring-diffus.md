---
layout: default
title: An Efficient Remote Sensing Super Resolution Method Exploring Diffusion Priors and Multi-Modal Constraints for Crop Type Mapping
---

# An Efficient Remote Sensing Super Resolution Method Exploring Diffusion Priors and Multi-Modal Constraints for Crop Type Mapping
**arXiv**：[2510.23382v1](https://arxiv.org/abs/2510.23382) · [PDF](https://arxiv.org/pdf/2510.23382.pdf)  
**作者**：Songxi Yang, Tang Sui, Qunying Huang  

**一句话要点**：提出高效遥感超分辨率方法LSSR，利用扩散先验和多模态约束提升作物类型制图

**关键词**：遥感超分辨率, 扩散模型, 多模态约束, 作物类型制图, 高效推理, 傅里叶损失

## 3 点简述
- 核心问题：扩散模型在遥感超分辨率中训练资源高、推理慢，且辅助信息利用不足。
- 方法要点：基于预训练Stable Diffusion，集成多模态注意力与适配器，优化傅里叶NDVI损失。
- 实验效果：在作物边界恢复和分类任务中达到SOTA，推理高效且下游任务表现优异。

## 摘要（原文）

> Super resolution offers a way to harness medium even lowresolution but
> historically valuable remote sensing image archives. Generative models,
> especially diffusion models, have recently been applied to remote sensing super
> resolution (RSSR), yet several challenges exist. First, diffusion models are
> effective but require expensive training from scratch resources and have slow
> inference speeds. Second, current methods have limited utilization of auxiliary
> information as real-world constraints to reconstruct scientifically realistic
> images. Finally, most current methods lack evaluation on downstream tasks. In
> this study, we present a efficient LSSR framework for RSSR, supported by a new
> multimodal dataset of paired 30 m Landsat 8 and 10 m Sentinel 2 imagery. Built
> on frozen pretrained Stable Diffusion, LSSR integrates crossmodal attention
> with auxiliary knowledge (Digital Elevation Model, land cover, month) and
> Synthetic Aperture Radar guidance, enhanced by adapters and a tailored Fourier
> NDVI loss to balance spatial details and spectral fidelity. Extensive
> experiments demonstrate that LSSR significantly improves crop boundary
> delineation and recovery, achieving state-of-the-art performance with Peak
> Signal-to-Noise Ratio/Structural Similarity Index Measure of 32.63/0.84 (RGB)
> and 23.99/0.78 (IR), and the lowest NDVI Mean Squared Error (0.042), while
> maintaining efficient inference (0.39 sec/image). Moreover, LSSR transfers
> effectively to NASA Harmonized Landsat and Sentinel (HLS) super resolution,
> yielding more reliable crop classification (F1: 0.86) than Sentinel-2 (F1:
> 0.85). These results highlight the potential of RSSR to advance precision
> agriculture.


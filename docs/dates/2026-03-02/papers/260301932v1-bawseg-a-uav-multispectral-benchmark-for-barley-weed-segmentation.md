---
layout: default
title: BAWSeg: A UAV Multispectral Benchmark for Barley Weed Segmentation
---

# BAWSeg: A UAV Multispectral Benchmark for Barley Weed Segmentation
**arXiv**：[2603.01932v1](https://arxiv.org/abs/2603.01932) · [PDF](https://arxiv.org/pdf/2603.01932.pdf)  
**作者**：Haitian Wang, Xinyu Wang, Muhammad Ibrahim, Dustin Severtson, Ajmal Mian  

**一句话要点**：提出VISA双流分割网络以解决无人机多光谱图像中作物与杂草像素级分割的挑战

**关键词**：无人机多光谱分割, 杂草检测, 双流网络, 注意力机制, 农业计算机视觉, 数据集基准

## 3 点简述
- 核心问题：现有方法依赖阈值化植被指数或单流网络，在辐射漂移和混合像素下鲁棒性差，对小杂草簇不敏感。
- 方法要点：VISA采用双流网络，分别处理辐射流和指数流，通过注意力机制融合，提升分割精度和效率。
- 实验或效果：在BAWSeg数据集上，VISA达到75.6% mIoU，优于基线，并在跨地块和跨年测试中保持稳定性能。

## 摘要（原文）

> Accurate weed mapping in cereal fields requires pixel-level segmentation from UAV imagery that remains reliable across fields, seasons, and illumination. Existing multispectral pipelines often depend on thresholded vegetation indices, which are brittle under radiometric drift and mixed crop--weed pixels, or on single-stream CNN and Transformer backbones that ingest stacked bands and indices, where radiance cues and normalized index cues interfere and reduce sensitivity to small weed clusters embedded in crop canopies. We propose VISA (Vegetation-Index and Spectral Attention), a two-stream segmentation network that decouples these cues and fuses them at native resolution. The radiance stream learns from calibrated five-band reflectance using residual spectral-spatial attention to preserve fine textures and row boundaries that are attenuated by ratio indices. The index stream operates on vegetation-index maps with windowed self-attention to model local structure efficiently, state-space layers to propagate field-scale context without quadratic attention cost, and Slot Attention to form stable region descriptors that improve discrimination of sparse weeds under canopy mixing. To support supervised training and deployment-oriented evaluation, we introduce BAWSeg, a four-year UAV multispectral dataset collected over commercial barley paddocks in Western Australia, providing radiometrically calibrated blue, green, red, red edge, and near-infrared orthomosaics, derived vegetation indices, and dense crop, weed, and other labels with leakage-free block splits. On BAWSeg, VISA achieves 75.6% mIoU and 63.5% weed IoU with 22.8M parameters, outperforming a multispectral SegFormer-B1 baseline by 1.2 mIoU and 1.9 weed IoU. Under cross-plot and cross-year protocols, VISA maintains 71.2% and 69.2% mIoU, respectively. The BAWSeg data, VISA code, and trained models will be released upon publication.


---
layout: default
title: MCD-Net: A Lightweight Deep Learning Baseline for Optical-Only Moraine Segmentation
---

# MCD-Net: A Lightweight Deep Learning Baseline for Optical-Only Moraine Segmentation
**arXiv**：[2601.02091v1](https://arxiv.org/abs/2601.02091) · [PDF](https://arxiv.org/pdf/2601.02091.pdf)  
**作者**：Zhehuan Cao, Fiseha Berhanu Tesema, Ping Fu, Jianfeng Ren, Ahmed Nasr  

**一句话要点**：提出MCD-Net轻量级基线，用于仅光学图像的冰碛物分割，以解决高分辨率DEM稀缺和光学对比度弱的问题。

**关键词**：冰碛物分割, 轻量级网络, 光学图像, 注意力机制, 冰川监测, 公开数据集

## 3 点简述
- 核心问题：冰川冰碛物自动分割受限于光学图像对比度弱和高分辨率DEM可用性不足。
- 方法要点：集成MobileNetV2编码器、CBAM注意力模块和DeepLabV3+解码器，构建轻量级网络。
- 实验或效果：在自建大规模数据集上，mIoU达62.3%，计算成本降低超60%，证明仅光学图像可提供可靠分割。

## 摘要（原文）

> Glacial segmentation is essential for reconstructing past glacier dynamics and evaluating climate-driven landscape change. However, weak optical contrast and the limited availability of high-resolution DEMs hinder automated mapping. This study introduces the first large-scale optical-only moraine segmentation dataset, comprising 3,340 manually annotated high-resolution images from Google Earth covering glaciated regions of Sichuan and Yunnan, China. We develop MCD-Net, a lightweight baseline that integrates a MobileNetV2 encoder, a Convolutional Block Attention Module (CBAM), and a DeepLabV3+ decoder. Benchmarking against deeper backbones (ResNet152, Xception) shows that MCD-Net achieves 62.3\% mean Intersection over Union (mIoU) and 72.8\% Dice coefficient while reducing computational cost by more than 60\%. Although ridge delineation remains constrained by sub-pixel width and spectral ambiguity, the results demonstrate that optical imagery alone can provide reliable moraine-body segmentation. The dataset and code are publicly available at https://github.com/Lyra-alpha/MCD-Net, establishing a reproducible benchmark for moraine-specific segmentation and offering a deployable baseline for high-altitude glacial monitoring.


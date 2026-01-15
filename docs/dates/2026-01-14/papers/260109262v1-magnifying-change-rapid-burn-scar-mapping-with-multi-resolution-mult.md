---
layout: default
title: Magnifying change: Rapid burn scar mapping with multi-resolution, multi-source satellite imagery
---

# Magnifying change: Rapid burn scar mapping with multi-resolution, multi-source satellite imagery
**arXiv**：[2601.09262v1](https://arxiv.org/abs/2601.09262) · [PDF](https://arxiv.org/pdf/2601.09262.pdf)  
**作者**：Maria Sdraka, Dimitrios Michail, Ioannis Papoutsis  

**一句话要点**：提出BAM-MRCD模型，利用多分辨率多源卫星影像快速绘制野火燃烧疤痕图

**关键词**：野火燃烧疤痕制图, 多源卫星影像融合, 深度学习变化检测, 时空分辨率提升, 快速灾害响应

## 3 点简述
- 问题：卫星影像中光谱变化不规则且空间异质，高分辨率数据与高频重访难以兼顾
- 方法：融合MODIS和Sentinel-2数据，通过多分辨率多源深度学习实现时空高分辨率制图
- 效果：准确检测小规模野火，超越现有变化检测模型和基线，代码数据已开源

## 摘要（原文）

> Delineating wildfire affected areas using satellite imagery remains challenging due to irregular and spatially heterogeneous spectral changes across the electromagnetic spectrum. While recent deep learning approaches achieve high accuracy when high-resolution multispectral data are available, their applicability in operational settings, where a quick delineation of the burn scar shortly after a wildfire incident is required, is limited by the trade-off between spatial resolution and temporal revisit frequency of current satellite systems. To address this limitation, we propose a novel deep learning model, namely BAM-MRCD, which employs multi-resolution, multi-source satellite imagery (MODIS and Sentinel-2) for the timely production of detailed burnt area maps with high spatial and temporal resolution. Our model manages to detect even small scale wildfires with high accuracy, surpassing similar change detection models as well as solid baselines. All data and code are available in the GitHub repository: https://github.com/Orion-AI-Lab/BAM-MRCD.


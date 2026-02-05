---
layout: default
title: Enabling Real-Time Colonoscopic Polyp Segmentation on Commodity CPUs via Ultra-Lightweight Architecture
---

# Enabling Real-Time Colonoscopic Polyp Segmentation on Commodity CPUs via Ultra-Lightweight Architecture
**arXiv**：[2602.04381v1](https://arxiv.org/abs/2602.04381) · [PDF](https://arxiv.org/pdf/2602.04381.pdf)  
**作者**：Weihao Gao, Zhuo Deng, Zheng Gong, Lan Ma  

**一句话要点**：提出UltraSeg超轻量架构，实现结肠镜息肉分割在CPU上的实时部署

**关键词**：结肠镜息肉分割, 超轻量架构, 实时计算, CPU部署, 医学图像分割, 资源受限环境

## 3 点简述
- 核心问题：高精度分割模型依赖GPU，难以在资源受限的初级医院或移动设备部署。
- 方法要点：通过联合优化编码器-解码器宽度、约束扩张卷积和跨层轻量融合，压缩参数至<0.3M。
- 实验或效果：在CPU单核上达90 FPS，Dice分数保留U-Net的94%以上，参数仅为其0.4%。

## 摘要（原文）

> Early detection of colorectal cancer hinges on real-time, accurate polyp identification and resection. Yet current high-precision segmentation models rely on GPUs, making them impractical to deploy in primary hospitals, mobile endoscopy units, or capsule robots. To bridge this gap, we present the UltraSeg family, operating in an extreme-compression regime (<0.3 M parameters). UltraSeg-108K (0.108 M parameters) is optimized for single-center data, while UltraSeg-130K (0.13 M parameters) generalizes to multi-center, multi-modal images. By jointly optimizing encoder-decoder widths, incorporating constrained dilated convolutions to enlarge receptive fields, and integrating a cross-layer lightweight fusion module, the models achieve 90 FPS on a single CPU core without sacrificing accuracy. Evaluated on seven public datasets, UltraSeg retains >94% of the Dice score of a 31 M-parameter U-Net while utilizing only 0.4% of its parameters, establishing a strong, clinically viable baseline for the extreme-compression domain and offering an immediately deployable solution for resource-constrained settings. This work provides not only a CPU-native solution for colonoscopy but also a reproducible blueprint for broader minimally invasive surgical vision applications. Source code is publicly available to ensure reproducibility and facilitate future benchmarking.


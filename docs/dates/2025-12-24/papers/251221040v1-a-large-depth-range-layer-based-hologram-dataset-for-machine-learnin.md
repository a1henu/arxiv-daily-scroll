---
layout: default
title: A Large-Depth-Range Layer-Based Hologram Dataset for Machine Learning-Based 3D Computer-Generated Holography
---

# A Large-Depth-Range Layer-Based Hologram Dataset for Machine Learning-Based 3D Computer-Generated Holography
**arXiv**：[2512.21040v1](https://arxiv.org/abs/2512.21040) · [PDF](https://arxiv.org/pdf/2512.21040.pdf)  
**作者**：Jaehong Lee, You Chan No, YoungWoo Kim, Duksu Kim  

**一句话要点**：提出KOREATECH-CGH数据集和振幅投影技术，以解决机器学习全息术中的高质量数据稀缺问题

**关键词**：计算机生成全息术, 机器学习数据集, 振幅投影, 深度范围扩展, 全息图重建, RGB-D图像

## 3 点简述
- 核心问题：机器学习全息术因缺乏大规模高质量全息图数据集而受限
- 方法要点：发布包含6000对RGB-D图像和复杂全息图的数据集，并引入振幅投影技术提升大深度范围全息图质量
- 实验或效果：振幅投影技术使重建保真度达27.01 dB PSNR和0.87 SSIM，优于现有方法，并通过ML模型验证数据集实用性

## 摘要（原文）

> Machine learning-based computer-generated holography (ML-CGH) has advanced rapidly in recent years, yet progress is constrained by the limited availability of high-quality, large-scale hologram datasets. To address this, we present KOREATECH-CGH, a publicly available dataset comprising 6,000 pairs of RGB-D images and complex holograms across resolutions ranging from 256*256 to 2048*2048, with depth ranges extending to the theoretical limits of the angular spectrum method for wide 3D scene coverage. To improve hologram quality at large depth ranges, we introduce amplitude projection, a post-processing technique that replaces amplitude components of hologram wavefields at each depth layer while preserving phase. This approach enhances reconstruction fidelity, achieving 27.01 dB PSNR and 0.87 SSIM, surpassing a recent optimized silhouette-masking layer-based method by 2.03 dB and 0.04 SSIM, respectively. We further validate the utility of KOREATECH-CGH through experiments on hologram generation and super-resolution using state-of-the-art ML models, confirming its applicability for training and evaluating next-generation ML-CGH systems.


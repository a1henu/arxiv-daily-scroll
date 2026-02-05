---
layout: default
title: Interactive Spatial-Frequency Fusion Mamba for Multi-Modal Image Fusion
---

# Interactive Spatial-Frequency Fusion Mamba for Multi-Modal Image Fusion
**arXiv**：[2602.04405v1](https://arxiv.org/abs/2602.04405) · [PDF](https://arxiv.org/pdf/2602.04405.pdf)  
**作者**：Yixin Zhu, Long Lv, Pingping Zhang, Xuehu Liu, Tongdan Tang, Feng Tian, Weibing Sun, Huchuan Lu  

**一句话要点**：提出交互式空间-频率融合Mamba框架以增强多模态图像融合效果

**关键词**：多模态图像融合, 空间-频率融合, Mamba模型, 长程依赖建模, 频率域特征, 交互式融合

## 3 点简述
- 多模态图像融合中空间-频率融合缺乏交互，影响特征互补性
- 引入Mamba建模长程依赖，多尺度频率融合和交互式空间-频率融合模块
- 在六个数据集上实验验证优于现有方法，代码已开源

## 摘要（原文）

> Multi-Modal Image Fusion (MMIF) aims to combine images from different modalities to produce fused images, retaining texture details and preserving significant information. Recently, some MMIF methods incorporate frequency domain information to enhance spatial features. However, these methods typically rely on simple serial or parallel spatial-frequency fusion without interaction. In this paper, we propose a novel Interactive Spatial-Frequency Fusion Mamba (ISFM) framework for MMIF. Specifically, we begin with a Modality-Specific Extractor (MSE) to extract features from different modalities. It models long-range dependencies across the image with linear computational complexity. To effectively leverage frequency information, we then propose a Multi-scale Frequency Fusion (MFF). It adaptively integrates low-frequency and high-frequency components across multiple scales, enabling robust representations of frequency features. More importantly, we further propose an Interactive Spatial-Frequency Fusion (ISF). It incorporates frequency features to guide spatial features across modalities, enhancing complementary representations. Extensive experiments are conducted on six MMIF datasets. The experimental results demonstrate that our ISFM can achieve better performances than other state-of-the-art methods. The source code is available at https://github.com/Namn23/ISFM.


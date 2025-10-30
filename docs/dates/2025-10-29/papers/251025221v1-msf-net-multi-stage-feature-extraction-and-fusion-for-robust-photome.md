---
layout: default
title: MSF-Net: Multi-Stage Feature Extraction and Fusion for Robust Photometric Stereo
---

# MSF-Net: Multi-Stage Feature Extraction and Fusion for Robust Photometric Stereo
**arXiv**：[2510.25221v1](https://arxiv.org/abs/2510.25221) · [PDF](https://arxiv.org/pdf/2510.25221.pdf)  
**作者**：Shiyu Qin, Zhihao Cai, Kaixuan Wang, Lin Qi, Junyu Dong  

**一句话要点**：提出MSF-Net以解决光度立体中多阶段特征提取与融合不足的问题

**关键词**：光度立体, 多阶段特征提取, 特征融合, 表面法线估计, 深度学习

## 3 点简述
- 现有学习模型在光度立体中难以准确捕获多阶段特征并促进特征交互
- 引入多阶段特征提取与选择性更新策略，结合特征融合模块提升特征质量
- 在DiLiGenT基准测试中，表面法线估计精度显著优于现有最优方法

## 摘要（原文）

> Photometric stereo is a technique aimed at determining surface normals
> through the utilization of shading cues derived from images taken under
> different lighting conditions. However, existing learning-based approaches
> often fail to accurately capture features at multiple stages and do not
> adequately promote interaction between these features. Consequently, these
> models tend to extract redundant features, especially in areas with intricate
> details such as wrinkles and edges. To tackle these issues, we propose MSF-Net,
> a novel framework for extracting information at multiple stages, paired with
> selective update strategy, aiming to extract high-quality feature information,
> which is critical for accurate normal construction. Additionally, we have
> developed a feature fusion module to improve the interplay among different
> features. Experimental results on the DiLiGenT benchmark show that our proposed
> MSF-Net significantly surpasses previous state-of-the-art methods in the
> accuracy of surface normal estimation.


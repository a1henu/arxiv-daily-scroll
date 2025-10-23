---
layout: default
title: Seabed-Net: A multi-task network for joint bathymetry estimation and seabed classification from remote sensing imagery in shallow waters
---

# Seabed-Net: A multi-task network for joint bathymetry estimation and seabed classification from remote sensing imagery in shallow waters
**arXiv**：[2510.19329v1](https://arxiv.org/abs/2510.19329) · [PDF](https://arxiv.org/pdf/2510.19329.pdf)  
**作者**：Panagiotis Agrafiotis, Begüm Demir  

**一句话要点**：提出Seabed-Net多任务网络，联合估计浅水区水深和海底分类。

**关键词**：多任务学习, 水深估计, 海底分类, 遥感图像, 浅水区映射, 注意力融合

## 3 点简述
- 现有方法孤立处理水深估计和海底分类，无法利用任务间交互优势。
- 采用双分支编码器、注意力特征融合和动态任务权重，实现多任务学习。
- 在异质海岸评估中，显著降低RMSE并提高分类精度，增强空间一致性。

## 摘要（原文）

> Accurate, detailed, and regularly updated bathymetry, coupled with complex
> semantic content, is essential for under-mapped shallow-water environments
> facing increasing climatological and anthropogenic pressures. However, existing
> approaches that derive either depth or seabed classes from remote sensing
> imagery treat these tasks in isolation, forfeiting the mutual benefits of their
> interaction and hindering the broader adoption of deep learning methods. To
> address these limitations, we introduce Seabed-Net, a unified multi-task
> framework that simultaneously predicts bathymetry and pixel-based seabed
> classification from remote sensing imagery of various resolutions. Seabed-Net
> employs dual-branch encoders for bathymetry estimation and pixel-based seabed
> classification, integrates cross-task features via an Attention Feature Fusion
> module and a windowed Swin-Transformer fusion block, and balances objectives
> through dynamic task uncertainty weighting. In extensive evaluations at two
> heterogeneous coastal sites, it consistently outperforms traditional empirical
> models and traditional machine learning regression methods, achieving up to
> 75\% lower RMSE. It also reduces bathymetric RMSE by 10-30\% compared to
> state-of-the-art single-task and multi-task baselines and improves seabed
> classification accuracy up to 8\%. Qualitative analyses further demonstrate
> enhanced spatial consistency, sharper habitat boundaries, and corrected depth
> biases in low-contrast regions. These results confirm that jointly modeling
> depth with both substrate and seabed habitats yields synergistic gains,
> offering a robust, open solution for integrated shallow-water mapping. Code and
> pretrained weights are available at https://github.com/pagraf/Seabed-Net.


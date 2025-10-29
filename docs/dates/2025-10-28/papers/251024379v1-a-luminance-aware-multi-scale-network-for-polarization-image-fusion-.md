---
layout: default
title: A Luminance-Aware Multi-Scale Network for Polarization Image Fusion with a Multi-Scene Dataset
---

# A Luminance-Aware Multi-Scale Network for Polarization Image Fusion with a Multi-Scene Dataset
**arXiv**：[2510.24379v1](https://arxiv.org/abs/2510.24379) · [PDF](https://arxiv.org/pdf/2510.24379.pdf)  
**作者**：Zhuangfan Huang, Xiaosong Li, Gao Wang, Tao Ye, Haishu Tan, Huafeng Li  

**一句话要点**：提出亮度感知多尺度网络以解决偏振图像融合在复杂光照下的对比度差异问题

**关键词**：偏振图像融合, 多尺度网络, 亮度感知, 自注意力机制, 数据集构建, 非线性校正

## 3 点简述
- 核心问题：偏振图像融合中S0和DOLP图像存在固有对比度差异，影响复杂光照下的特征互补。
- 方法要点：设计多尺度空间权重矩阵和亮度增强模块，动态注入亮度信息并实现非线性校正。
- 实验或效果：在MSP等数据集上，MS-SSIM和SD指标平均提升8.57%至63.53%，优于现有方法。

## 摘要（原文）

> Polarization image fusion combines S0 and DOLP images to reveal surface
> roughness and material properties through complementary texture features, which
> has important applications in camouflage recognition, tissue pathology
> analysis, surface defect detection and other fields. To intergrate
> coL-Splementary information from different polarized images in complex
> luminance environment, we propose a luminance-aware multi-scale network (MLSN).
> In the encoder stage, we propose a multi-scale spatial weight matrix through a
> brightness-branch , which dynamically weighted inject the luminance into the
> feature maps, solving the problem of inherent contrast difference in polarized
> images. The global-local feature fusion mechanism is designed at the bottleneck
> layer to perform windowed self-attention computation, to balance the global
> context and local details through residual linking in the feature dimension
> restructuring stage. In the decoder stage, to further improve the adaptability
> to complex lighting, we propose a Brightness-Enhancement module, establishing
> the mapping relationship between luminance distribution and texture features,
> realizing the nonlinear luminance correction of the fusion result. We also
> present MSP, an 1000 pairs of polarized images that covers 17 types of indoor
> and outdoor complex lighting scenes. MSP provides four-direction polarization
> raw maps, solving the scarcity of high-quality datasets in polarization image
> fusion. Extensive experiment on MSP, PIF and GAND datasets verify that the
> proposed MLSN outperms the state-of-the-art methods in subjective and objective
> evaluations, and the MS-SSIM and SD metircs are higher than the average values
> of other methods by 8.57%, 60.64%, 10.26%, 63.53%, 22.21%, and 54.31%,
> respectively. The source code and dataset is avalable at
> https://github.com/1hzf/MLS-UNet.


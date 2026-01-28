---
layout: default
title: WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration
---

# WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration
**arXiv**：[2601.19753v1](https://arxiv.org/abs/2601.19753) · [PDF](https://arxiv.org/pdf/2601.19753.pdf)  
**作者**：Xinrui Zhang, Yufeng Wang, Shuangkang Fang, Zesheng Wang, Dacheng Qi, Wenrui Ding  

**一句话要点**：提出WaterClear-GS，将水下光学特性融入3D高斯泼溅，实现水下重建与恢复。

**关键词**：水下3D重建, 高斯泼溅, 光学特性建模, 实时渲染, 图像恢复

## 3 点简述
- 核心问题：水下3D重建受波长衰减和散射影响，现有方法渲染慢且颜色恢复差。
- 方法要点：基于3D高斯泼溅，集成局部衰减和散射，无需辅助网络，采用双分支优化策略。
- 实验或效果：在标准基准和新数据集上，实现实时渲染，在新视角合成和水下图像恢复任务中表现优异。

## 摘要（原文）

> Underwater 3D reconstruction and appearance restoration are hindered by the complex optical properties of water, such as wavelength-dependent attenuation and scattering. Existing Neural Radiance Fields (NeRF)-based methods struggle with slow rendering speeds and suboptimal color restoration, while 3D Gaussian Splatting (3DGS) inherently lacks the capability to model complex volumetric scattering effects. To address these issues, we introduce WaterClear-GS, the first pure 3DGS-based framework that explicitly integrates underwater optical properties of local attenuation and scattering into Gaussian primitives, eliminating the need for an auxiliary medium network. Our method employs a dual-branch optimization strategy to ensure underwater photometric consistency while naturally recovering water-free appearances. This strategy is enhanced by depth-guided geometry regularization and perception-driven image loss, together with exposure constraints, spatially-adaptive regularization, and physically guided spectral regularization, which collectively enforce local 3D coherence and maintain natural visual perception. Experiments on standard benchmarks and our newly collected dataset demonstrate that WaterClear-GS achieves outstanding performance on both novel view synthesis (NVS) and underwater image restoration (UIR) tasks, while maintaining real-time rendering. The code will be available at https://buaaxrzhang.github.io/WaterClear-GS/.


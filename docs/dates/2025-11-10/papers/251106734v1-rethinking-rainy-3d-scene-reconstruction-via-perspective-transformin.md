---
layout: default
title: Rethinking Rainy 3D Scene Reconstruction via Perspective Transforming and Brightness Tuning
---

# Rethinking Rainy 3D Scene Reconstruction via Perspective Transforming and Brightness Tuning
**arXiv**：[2511.06734v1](https://arxiv.org/abs/2511.06734) · [PDF](https://arxiv.org/pdf/2511.06734.pdf)  
**作者**：Qianfeng Yang, Xiang Chen, Pengpeng Li, Qiyuan Guan, Guiyue Jin, Jiyu Jin  

**一句话要点**：提出REVR-GSNet框架和OmniRain3D数据集，以解决雨天多视图图像导致的3D场景重建不准确问题

**关键词**：3D场景重建, 多视图图像去雨, 高斯溅射, 数据集构建, 亮度增强, 雨痕消除

## 3 点简述
- 核心问题：雨天导致多视图图像质量下降，影响3D场景重建的准确性和完整性
- 方法要点：通过递归亮度增强、高斯基元优化和GS引导雨痕消除，实现端到端重建
- 实验或效果：基于OmniRain3D数据集验证，方法有效提升雨天场景重建质量

## 摘要（原文）

> Rain degrades the visual quality of multi-view images, which are essential
> for 3D scene reconstruction, resulting in inaccurate and incomplete
> reconstruction results. Existing datasets often overlook two critical
> characteristics of real rainy 3D scenes: the viewpoint-dependent variation in
> the appearance of rain streaks caused by their projection onto 2D images, and
> the reduction in ambient brightness resulting from cloud coverage during
> rainfall. To improve data realism, we construct a new dataset named OmniRain3D
> that incorporates perspective heterogeneity and brightness dynamicity, enabling
> more faithful simulation of rain degradation in 3D scenes. Based on this
> dataset, we propose an end-to-end reconstruction framework named REVR-GSNet
> (Rain Elimination and Visibility Recovery for 3D Gaussian Splatting).
> Specifically, REVR-GSNet integrates recursive brightness enhancement, Gaussian
> primitive optimization, and GS-guided rain elimination into a unified
> architecture through joint alternating optimization, achieving high-fidelity
> reconstruction of clean 3D scenes from rain-degraded inputs. Extensive
> experiments show the effectiveness of our dataset and method. Our dataset and
> method provide a foundation for future research on multi-view image deraining
> and rainy 3D scene reconstruction.


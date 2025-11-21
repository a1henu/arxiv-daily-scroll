---
layout: default
title: Clustered Error Correction with Grouped 4D Gaussian Splatting
---

# Clustered Error Correction with Grouped 4D Gaussian Splatting
**arXiv**：[2511.16112v1](https://arxiv.org/abs/2511.16112) · [PDF](https://arxiv.org/pdf/2511.16112.pdf)  
**作者**：Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee  

**一句话要点**：提出聚类误差校正与分组4D高斯泼溅以改进动态场景重建

**关键词**：4D高斯泼溅, 动态场景重建, 误差聚类, 时间一致性, 渲染质量, 像素对应

## 3 点简述
- 现有4D高斯泼溅方法在动态场景重建中难以处理像素对应模糊和动态区域密度不足问题
- 引入椭圆误差聚类和误差校正泼溅添加，通过颜色一致性指导缺失颜色或遮挡校正
- 在多个数据集上验证，提升时间一致性和渲染质量，PSNR提高0.39dB

## 摘要（原文）

> Existing 4D Gaussian Splatting (4DGS) methods struggle to accurately reconstruct dynamic scenes, often failing to resolve ambiguous pixel correspondences and inadequate densification in dynamic regions. We address these issues by introducing a novel method composed of two key components: (1) Elliptical Error Clustering and Error Correcting Splat Addition that pinpoints dynamic areas to improve and initialize fitting splats, and (2) Grouped 4D Gaussian Splatting that improves consistency of mapping between splats and represented dynamic objects. Specifically, we classify rendering errors into missing-color and occlusion types, then apply targeted corrections via backprojection or foreground splitting guided by cross-view color consistency. Evaluations on Neural 3D Video and Technicolor datasets demonstrate that our approach significantly improves temporal consistency and achieves state-of-the-art perceptual rendering quality, improving 0.39dB of PSNR on the Technicolor Light Field dataset. Our visualization shows improved alignment between splats and dynamic objects, and the error correction method's capability to identify errors and properly initialize new splats. Our implementation details and source code are available at https://github.com/tho-kn/cem-4dgs.


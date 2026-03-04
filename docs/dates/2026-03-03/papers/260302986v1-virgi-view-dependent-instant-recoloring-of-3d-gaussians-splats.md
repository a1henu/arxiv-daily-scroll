---
layout: default
title: VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats
---

# VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats
**arXiv**：[2603.02986v1](https://arxiv.org/abs/2603.02986) · [PDF](https://arxiv.org/pdf/2603.02986.pdf)  
**作者**：Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer  

**一句话要点**：提出VIRGi方法，通过分离颜色组件和多视图训练，实现3D高斯溅射场景的快速重着色

**关键词**：3D高斯溅射, 场景重着色, 视点依赖效果, 多视图训练, 实时编辑, 神经辐射场

## 3 点简述
- 核心问题：3D高斯溅射缺乏高效且逼真的场景外观编辑方法，难以保持视点依赖效果。
- 方法要点：引入新架构分离漫反射和视点依赖颜色，采用多视图训练策略提升重建精度。
- 实验或效果：仅需一张手动编辑图像，通过微调MLP权重，在2秒内传播颜色编辑，支持实时交互。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently transformed the fields of novel view synthesis and 3D reconstruction due to its ability to accurately model complex 3D scenes and its unprecedented rendering performance. However, a significant challenge persists: the absence of an efficient and photorealistic method for editing the appearance of the scene's content. In this paper we introduce VIRGi, a novel approach for rapidly editing the color of scenes modeled by 3DGS while preserving view-dependent effects such as specular highlights. Key to our method are a novel architecture that separates color into diffuse and view-dependent components, and a multi-view training strategy that integrates image patches from multiple viewpoints. Improving over the conventional single-view batch training, our 3DGS representation provides more accurate reconstruction and serves as a solid representation for the recoloring task. For 3DGS recoloring, we then introduce a rapid scheme requiring only one manually edited image of the scene from the end-user. By fine-tuning the weights of a single MLP, alongside a module for single-shot segmentation of the editable area, the color edits are seamlessly propagated to the entire scene in just two seconds, facilitating real-time interaction and providing control over the strength of the view-dependent effects. An exhaustive validation on diverse datasets demonstrates significant quantitative and qualitative advancements over competitors based on Neural Radiance Fields representations.


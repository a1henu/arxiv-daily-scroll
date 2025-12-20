---
layout: default
title: Multi-scale Attention-Guided Intrinsic Decomposition and Rendering Pass Prediction for Facial Images
---

# Multi-scale Attention-Guided Intrinsic Decomposition and Rendering Pass Prediction for Facial Images
**arXiv**：[2512.16511v1](https://arxiv.org/abs/2512.16511) · [PDF](https://arxiv.org/pdf/2512.16511.pdf)  
**作者**：Hossein Javidnia  

**一句话要点**：提出MAGINet以解决无约束光照下人脸图像的本征分解问题，用于真实感重光照和数字孪生

**关键词**：人脸本征分解, 多尺度注意力网络, 渲染通道预测, 真实感重光照, 数字孪生

## 3 点简述
- 核心问题：无约束光照下人脸图像的本征分解，是真实感重光照和高保真数字孪生的前提
- 方法要点：MAGINet采用多尺度注意力引导网络预测归一化漫反射反照率，结合RefinementNet和Pix2PixHD预测完整渲染通道
- 实验或效果：在FFHQ-UV-Intrinsics数据集上训练，实现最先进的漫反射反照率估计，并提升完整渲染堆栈的保真度

## 摘要（原文）

> Accurate intrinsic decomposition of face images under unconstrained lighting is a prerequisite for photorealistic relighting, high-fidelity digital doubles, and augmented-reality effects. This paper introduces MAGINet, a Multi-scale Attention-Guided Intrinsics Network that predicts a $512\times512$ light-normalized diffuse albedo map from a single RGB portrait. MAGINet employs hierarchical residual encoding, spatial-and-channel attention in a bottleneck, and adaptive multi-scale feature fusion in the decoder, yielding sharper albedo boundaries and stronger lighting invariance than prior U-Net variants. The initial albedo prediction is upsampled to $1024\times1024$ and refined by a lightweight three-layer CNN (RefinementNet). Conditioned on this refined albedo, a Pix2PixHD-based translator then predicts a comprehensive set of five additional physically based rendering passes: ambient occlusion, surface normal, specular reflectance, translucency, and raw diffuse colour (with residual lighting). Together with the refined albedo, these six passes form the complete intrinsic decomposition. Trained with a combination of masked-MSE, VGG, edge, and patch-LPIPS losses on the FFHQ-UV-Intrinsics dataset, the full pipeline achieves state-of-the-art performance for diffuse albedo estimation and demonstrates significantly improved fidelity for the complete rendering stack compared to prior methods. The resulting passes enable high-quality relighting and material editing of real faces.


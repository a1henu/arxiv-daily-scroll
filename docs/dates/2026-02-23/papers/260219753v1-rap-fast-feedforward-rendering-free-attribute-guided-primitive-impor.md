---
layout: default
title: RAP: Fast Feedforward Rendering-Free Attribute-Guided Primitive Importance Score Prediction for Efficient 3D Gaussian Splatting Processing
---

# RAP: Fast Feedforward Rendering-Free Attribute-Guided Primitive Importance Score Prediction for Efficient 3D Gaussian Splatting Processing
**arXiv**：[2602.19753v1](https://arxiv.org/abs/2602.19753) · [PDF](https://arxiv.org/pdf/2602.19753.pdf)  
**作者**：Kaifa Yang, Qi Yang, Yiling Xu, Zhu Li  

**一句话要点**：提出RAP方法以解决3D高斯泼溅中基于渲染的重要性预测效率低问题

**关键词**：3D高斯泼溅, 重要性预测, 渲染无关方法, 属性引导, MLP预测, 场景压缩

## 3 点简述
- 核心问题：3D高斯泼溅中基于渲染的重要性预测方法计算慢、依赖视图选择，限制可扩展性。
- 方法要点：RAP通过高斯属性和局部统计直接预测重要性，避免渲染计算，使用MLP和正则化训练。
- 实验或效果：RAP在少量场景训练后能泛化到未见数据，集成到重建、压缩和传输流程中。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a leading technology for high-quality 3D scene reconstruction. However, the iterative refinement and densification process leads to the generation of a large number of primitives, each contributing to the reconstruction to a substantially different extent. Estimating primitive importance is thus crucial, both for removing redundancy during reconstruction and for enabling efficient compression and transmission. Existing methods typically rely on rendering-based analyses, where each primitive is evaluated through its contribution across multiple camera viewpoints. However, such methods are sensitive to the number and selection of views, rely on specialized differentiable rasterizers, and have long calculation times that grow linearly with view count, making them difficult to integrate as plug-and-play modules and limiting scalability and generalization. To address these issues, we propose RAP, a fast feedforward rendering-free attribute-guided method for efficient importance score prediction in 3DGS. RAP infers primitive significance directly from intrinsic Gaussian attributes and local neighborhood statistics, avoiding rendering-based or visibility-dependent computations. A compact MLP predicts per-primitive importance scores using rendering loss, pruning-aware loss, and significance distribution regularization. After training on a small set of scenes, RAP generalizes effectively to unseen data and can be seamlessly integrated into reconstruction, compression, and transmission pipelines. Our code is publicly available at https://github.com/yyyykf/RAP.


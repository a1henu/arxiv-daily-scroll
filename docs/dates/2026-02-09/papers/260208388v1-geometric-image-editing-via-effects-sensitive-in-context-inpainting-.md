---
layout: default
title: Geometric Image Editing via Effects-Sensitive In-Context Inpainting with Diffusion Transformers
---

# Geometric Image Editing via Effects-Sensitive In-Context Inpainting with Diffusion Transformers
**arXiv**：[2602.08388v1](https://arxiv.org/abs/2602.08388) · [PDF](https://arxiv.org/pdf/2602.08388.pdf)  
**作者**：Shuo Zhang, Wenzhuo Wu, Huayu Zhang, Jiarong Cheng, Xianghao Zang, Chao Ban, Hao Sun, Zhongjiang He, Tianwei Cao, Kongming Liang, Zhanyu Ma  

**一句话要点**：提出GeoEdit框架，通过扩散变换器实现几何图像编辑，解决复杂场景中几何变换和光影效果建模的挑战。

**关键词**：几何图像编辑, 扩散变换器, 光影效果建模, 上下文生成, 大规模数据集

## 3 点简述
- 核心问题：现有方法难以准确处理几何变换（如平移、旋转、缩放）和复杂光影效果，导致编辑结果不真实。
- 方法要点：利用扩散变换器模块进行上下文生成，集成几何变换，并引入Effects-Sensitive Attention增强光影建模。
- 实验或效果：在公开基准测试中，GeoEdit在视觉质量、几何准确性和真实感方面优于现有方法，并构建了大规模数据集RS-Objects支持训练。

## 摘要（原文）

> Recent advances in diffusion models have significantly improved image editing. However, challenges persist in handling geometric transformations, such as translation, rotation, and scaling, particularly in complex scenes. Existing approaches suffer from two main limitations: (1) difficulty in achieving accurate geometric editing of object translation, rotation, and scaling; (2) inadequate modeling of intricate lighting and shadow effects, leading to unrealistic results. To address these issues, we propose GeoEdit, a framework that leverages in-context generation through a diffusion transformer module, which integrates geometric transformations for precise object edits. Moreover, we introduce Effects-Sensitive Attention, which enhances the modeling of intricate lighting and shadow effects for improved realism. To further support training, we construct RS-Objects, a large-scale geometric editing dataset containing over 120,000 high-quality image pairs, enabling the model to learn precise geometric editing while generating realistic lighting and shadows. Extensive experiments on public benchmarks demonstrate that GeoEdit consistently outperforms state-of-the-art methods in terms of visual quality, geometric accuracy, and realism.


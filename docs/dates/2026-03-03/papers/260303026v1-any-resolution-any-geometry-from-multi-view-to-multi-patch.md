---
layout: default
title: Any Resolution Any Geometry: From Multi-View To Multi-Patch
---

# Any Resolution Any Geometry: From Multi-View To Multi-Patch
**arXiv**：[2603.03026v1](https://arxiv.org/abs/2603.03026) · [PDF](https://arxiv.org/pdf/2603.03026.pdf)  
**作者**：Wenqing Cui, Zhenyu Li, Mykola Lavreniuk, Jian Shi, Ramzi Idoughi, Xiangjun Tang, Peter Wonka  

**一句话要点**：提出超分辨率几何变换器以解决单目高分辨率深度-法线联合估计的全局一致性难题

**关键词**：单目深度估计, 表面法线估计, 多块变换器, 高分辨率几何, 跨域泛化, 几何细化

## 3 点简述
- 核心问题：高分辨率几何估计中局部细节与全局一致性的权衡困难
- 方法要点：基于多块变换器，通过跨块注意力增强全局几何推理
- 实验或效果：在UnrealStereo4K上实现深度和法线估计的SOTA性能，提升精度和稳定性

## 摘要（原文）

> Joint estimation of surface normals and depth is essential for holistic 3D scene understanding, yet high-resolution prediction remains difficult due to the trade-off between preserving fine local detail and maintaining global consistency. To address this challenge, we propose the Ultra Resolution Geometry Transformer (URGT), which adapts the Visual Geometry Grounded Transformer (VGGT) into a unified multi-patch transformer for monocular high-resolution depth--normal estimation. A single high-resolution image is partitioned into patches that are augmented with coarse depth and normal priors from pre-trained models, and jointly processed in a single forward pass to predict refined geometric outputs. Global coherence is enforced through cross-patch attention, which enables long-range geometric reasoning and seamless propagation of information across patches within a shared backbone. To further enhance spatial robustness, we introduce a GridMix patch sampling strategy that probabilistically samples grid configurations during training, improving inter-patch consistency and generalization. Our method achieves state-of-the-art results on UnrealStereo4K, jointly improving depth and normal estimation, reducing AbsRel from 0.0582 to 0.0291, RMSE from 2.17 to 1.31, and lowering mean angular error from 23.36 degrees to 18.51 degrees, while producing sharper and more stable geometry. The proposed multi-patch framework also demonstrates strong zero-shot and cross-domain generalization and scales effectively to very high resolutions, offering an efficient and extensible solution for high-quality geometry refinement.


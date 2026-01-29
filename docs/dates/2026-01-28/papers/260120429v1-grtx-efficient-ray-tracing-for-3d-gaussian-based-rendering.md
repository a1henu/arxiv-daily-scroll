---
layout: default
title: GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering
---

# GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering
**arXiv**：[2601.20429v1](https://arxiv.org/abs/2601.20429) · [PDF](https://arxiv.org/pdf/2601.20429.pdf)  
**作者**：Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  

**一句话要点**：提出GRTX优化以提升3D高斯渲染的射线追踪效率

**关键词**：3D高斯渲染, 射线追踪优化, 加速结构, 硬件支持, 渲染性能

## 3 点简述
- 核心问题：现有高斯射线追踪方法存在加速结构臃肿和节点遍历冗余，导致性能低下。
- 方法要点：通过射线空间变换将各向异性高斯视为单位球体，构建精简加速结构；硬件支持遍历检查点，减少多轮追踪中的冗余节点访问。
- 实验或效果：相比基线方法显著提升射线追踪性能，硬件成本可忽略。

## 摘要（原文）

> 3D Gaussian Splatting has gained widespread adoption across diverse applications due to its exceptional rendering performance and visual quality. While most existing methods rely on rasterization to render Gaussians, recent research has started investigating ray tracing approaches to overcome the fundamental limitations inherent in rasterization. However, current Gaussian ray tracing methods suffer from inefficiencies such as bloated acceleration structures and redundant node traversals, which greatly degrade ray tracing performance.
>   In this work, we present GRTX, a set of software and hardware optimizations that enable efficient ray tracing for 3D Gaussian-based rendering. First, we introduce a novel approach for constructing streamlined acceleration structures for Gaussian primitives. Our key insight is that anisotropic Gaussians can be treated as unit spheres through ray space transformations, which substantially reduces BVH size and traversal overhead. Second, we propose dedicated hardware support for traversal checkpointing within ray tracing units. This eliminates redundant node visits during multi-round tracing by resuming traversal from checkpointed nodes rather than restarting from the root node in each subsequent round. Our evaluation shows that GRTX significantly improves ray tracing performance compared to the baseline ray tracing method with a negligible hardware cost.


---
layout: default
title: Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy
---

# Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy
**arXiv**：[2601.22026v1](https://arxiv.org/abs/2601.22026) · [PDF](https://arxiv.org/pdf/2601.22026.pdf)  
**作者**：Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  

**一句话要点**：提出混合注视点路径追踪与外围高斯泼溅方法，用于交互式沉浸式解剖可视化。

**关键词**：体积医学可视化, 混合渲染, 注视点渲染, 高斯泼溅, 交互式可视化, 路径追踪

## 3 点简述
- 核心问题：传统2D切片和现有体积渲染方法在交互性和计算成本上存在限制，影响医学可视化效果。
- 方法要点：结合流式注视点路径追踪和轻量级高斯泼溅近似，优化外围模型生成并支持实时更新。
- 实验或效果：相比直接路径追踪和高斯泼溅，该方法在视觉质量与交互性间取得平衡，外围模型再生时间小于一秒。

## 摘要（原文）

> Volumetric medical imaging offers great potential for understanding complex pathologies. Yet, traditional 2D slices provide little support for interpreting spatial relationships, forcing users to mentally reconstruct anatomy into three dimensions. Direct volumetric path tracing and VR rendering can improve perception but are computationally expensive, while precomputed representations, like Gaussian Splatting, require planning ahead. Both approaches limit interactive use.
>   We propose a hybrid rendering approach for high-quality, interactive, and immersive anatomical visualization. Our method combines streamed foveated path tracing with a lightweight Gaussian Splatting approximation of the periphery. The peripheral model generation is optimized with volume data and continuously refined using foveal renderings, enabling interactive updates. Depth-guided reprojection further improves robustness to latency and allows users to balance fidelity with refresh rate.
>   We compare our method against direct path tracing and Gaussian Splatting. Our results highlight how their combination can preserve strengths in visual quality while re-generating the peripheral model in under a second, eliminating extensive preprocessing and approximations. This opens new options for interactive medical visualization.


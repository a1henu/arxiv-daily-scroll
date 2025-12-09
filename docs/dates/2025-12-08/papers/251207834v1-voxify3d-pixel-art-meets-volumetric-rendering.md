---
layout: default
title: Voxify3D: Pixel Art Meets Volumetric Rendering
---

# Voxify3D: Pixel Art Meets Volumetric Rendering
**arXiv**：[2512.07834v1](https://arxiv.org/abs/2512.07834) · [PDF](https://arxiv.org/pdf/2512.07834.pdf)  
**作者**：Yi-Chuan Huang, Jiewen Chan, Hao-Jen Chien, Yu-Lun Liu  

**一句话要点**：提出Voxify3D框架，通过可微分两阶段优化解决3D网格到体素艺术的自动生成难题。

**关键词**：体素艺术生成, 可微分渲染, 离散优化, 语义保持, 像素艺术监督, 调色板约束

## 3 点简述
- 核心问题：体素艺术自动生成需平衡几何抽象、语义保持和离散颜色一致性，现有方法难以兼顾。
- 方法要点：结合正交像素艺术监督、基于补丁的CLIP对齐和调色板约束Gumbel-Softmax量化，实现端到端优化。
- 实验或效果：在多样角色上表现优异（CLIP-IQA 37.12，用户偏好77.90%），支持可控抽象（2-8颜色，20x-50x分辨率）。

## 摘要（原文）

> Voxel art is a distinctive stylization widely used in games and digital media, yet automated generation from 3D meshes remains challenging due to conflicting requirements of geometric abstraction, semantic preservation, and discrete color coherence. Existing methods either over-simplify geometry or fail to achieve the pixel-precise, palette-constrained aesthetics of voxel art. We introduce Voxify3D, a differentiable two-stage framework bridging 3D mesh optimization with 2D pixel art supervision. Our core innovation lies in the synergistic integration of three components: (1) orthographic pixel art supervision that eliminates perspective distortion for precise voxel-pixel alignment; (2) patch-based CLIP alignment that preserves semantics across discretization levels; (3) palette-constrained Gumbel-Softmax quantization enabling differentiable optimization over discrete color spaces with controllable palette strategies. This integration addresses fundamental challenges: semantic preservation under extreme discretization, pixel-art aesthetics through volumetric rendering, and end-to-end discrete optimization. Experiments show superior performance (37.12 CLIP-IQA, 77.90\% user preference) across diverse characters and controllable abstraction (2-8 colors, 20x-50x resolutions). Project page: https://yichuanh.github.io/Voxify-3D/


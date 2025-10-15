---
layout: default
title: UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal Rendering
---

# UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal Rendering
**arXiv**：[2510.12174v1](https://arxiv.org/abs/2510.12174) · [PDF](https://arxiv.org/pdf/2510.12174.pdf)  
**作者**：Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  

**一句话要点**：提出UniGS统一框架，实现高保真多模态3D重建，基于几何感知高斯溅射。

**关键词**：3D高斯溅射, 多模态渲染, 几何一致性, 可微光栅化, CUDA加速

## 3 点简述
- 核心问题：多模态3D重建中几何一致性与渲染效率的挑战。
- 方法要点：重新设计光栅化，使用可微光线-椭球相交优化深度和表面法线。
- 实验或效果：定量定性实验显示在所有模态上达到最先进重建精度。

## 摘要（原文）

> In this paper, we propose UniGS, a unified map representation and
> differentiable framework for high-fidelity multimodal 3D reconstruction based
> on 3D Gaussian Splatting. Our framework integrates a CUDA-accelerated
> rasterization pipeline capable of rendering photo-realistic RGB images,
> geometrically accurate depth maps, consistent surface normals, and semantic
> logits simultaneously. We redesign the rasterization to render depth via
> differentiable ray-ellipsoid intersection rather than using Gaussian centers,
> enabling effective optimization of rotation and scale attribute through
> analytic depth gradients. Furthermore, we derive the analytic gradient
> formulation for surface normal rendering, ensuring geometric consistency among
> reconstructed 3D scenes. To improve computational and storage efficiency, we
> introduce a learnable attribute that enables differentiable pruning of
> Gaussians with minimal contribution during training. Quantitative and
> qualitative experiments demonstrate state-of-the-art reconstruction accuracy
> across all modalities, validating the efficacy of our geometry-aware paradigm.
> Source code and multimodal viewer will be available on GitHub.


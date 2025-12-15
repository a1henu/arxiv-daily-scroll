---
layout: default
title: Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance
---

# Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance
**arXiv**：[2512.11800v1](https://arxiv.org/abs/2512.11800) · [PDF](https://arxiv.org/pdf/2512.11800.pdf)  
**作者**：Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  

**一句话要点**：提出基于矩的3D高斯溅射方法，以解决复杂半透明物体渲染中的体积遮挡问题。

**关键词**：3D高斯溅射, 体积渲染, 矩方法, 透射率计算, 光栅化渲染, 半透明物体

## 3 点简述
- 3D高斯溅射依赖简化混合，难以渲染重叠半透明物体。
- 利用统计矩表征密度分布，实现无排序的高精度透射率计算。
- 方法提升重建和渲染质量，无需光线追踪或像素排序。

## 摘要（原文）

> The recent success of 3D Gaussian Splatting (3DGS) has reshaped novel view synthesis by enabling fast optimization and real-time rendering of high-quality radiance fields. However, it relies on simplified, order-dependent alpha blending and coarse approximations of the density integral within the rasterizer, thereby limiting its ability to render complex, overlapping semi-transparent objects. In this paper, we extend rasterization-based rendering of 3D Gaussian representations with a novel method for high-fidelity transmittance computation, entirely avoiding the need for ray tracing or per-pixel sample sorting. Building on prior work in moment-based order-independent transparency, our key idea is to characterize the density distribution along each camera ray with a compact and continuous representation based on statistical moments. To this end, we analytically derive and compute a set of per-pixel moments from all contributing 3D Gaussians. From these moments, a continuous transmittance function is reconstructed for each ray, which is then independently sampled within each Gaussian. As a result, our method bridges the gap between rasterization and physical accuracy by modeling light attenuation in complex translucent media, significantly improving overall reconstruction and rendering quality.


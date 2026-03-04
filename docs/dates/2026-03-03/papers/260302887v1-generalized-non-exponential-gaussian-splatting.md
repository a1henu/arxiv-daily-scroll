---
layout: default
title: Generalized non-exponential Gaussian splatting
---

# Generalized non-exponential Gaussian splatting
**arXiv**：[2603.02887v1](https://arxiv.org/abs/2603.02887) · [PDF](https://arxiv.org/pdf/2603.02887.pdf)  
**作者**：Sébastien Speierer, Adrian Jarabo  

**一句话要点**：提出非指数高斯泼溅以扩展3D高斯泼溅的物理渲染模型，减少过绘制并提升渲染速度。

**关键词**：3D高斯泼溅, 非指数辐射传输, 物理渲染, 过绘制优化, 渲染加速

## 3 点简述
- 核心问题：3D高斯泼溅基于指数透射率，限制了物理渲染模型的通用性。
- 方法要点：推广图像形成模型至非指数透射率，引入二次透射率定义亚线性、线性和超线性版本。
- 实验或效果：在复杂真实场景中，新变体质量相似但减少过绘制，渲染速度提升高达4倍。

## 摘要（原文）

> In this work we generalize 3D Gaussian splatting (3DGS) to a wider family of physically-based alpha-blending operators. 3DGS has become the standard de-facto for radiance field rendering and reconstruction, given its flexibility and efficiency. At its core, it is based on alpha-blending sorted semitransparent primitives, which in the limit converges to the classic radiative transfer function with exponential transmittance. Inspired by recent research on non-exponential radiative transfer, we generalize the image formation model of 3DGS to non-exponential regimes. Based on this generalization, we use a quadratic transmittance to define sub-linear, linear, and super-linear versions of 3DGS, which exhibit faster-than-exponential decay. We demonstrate that these new non-exponential variants achieve similar quality than the original 3DGS but significantly reduce the number of overdraws, which result on speed-ups of up to $4\times$ in complex real-world captures, on a ray-tracing-based renderer.


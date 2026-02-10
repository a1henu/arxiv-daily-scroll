---
layout: default
title: Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering
---

# Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering
**arXiv**：[2602.08724v1](https://arxiv.org/abs/2602.08724) · [PDF](https://arxiv.org/pdf/2602.08724.pdf)  
**作者**：Geng Lin, Matthias Zwicker  

**一句话要点**：提出RotLight旋转捕获设置以解决逆渲染中反照率估计的模糊性问题

**关键词**：逆渲染, 反照率估计, 高斯溅射, 光照建模, 场景分解

## 3 点简述
- 核心问题：逆渲染中反照率估计存在模糊性，导致颜色不准确和阴影残留
- 方法要点：通过物体旋转捕获减少模糊性，并引入代理网格改进光照追踪和全局光照处理
- 实验或效果：在合成和真实数据集上实现更优反照率估计，同时保持计算效率

## 摘要（原文）

> Inverse rendering aims to decompose a scene into its geometry, material properties and light conditions under a certain rendering model. It has wide applications like view synthesis, relighting, and scene editing. In recent years, inverse rendering methods have been inspired by view synthesis approaches like neural radiance fields and Gaussian splatting, which are capable of efficiently decomposing a scene into its geometry and radiance. They then further estimate the material and lighting that lead to the observed scene radiance. However, the latter step is highly ambiguous and prior works suffer from inaccurate color and baked shadows in their albedo estimation albeit their regularization. To this end, we propose RotLight, a simple capturing setup, to address the ambiguity. Compared to a usual capture, RotLight only requires the object to be rotated several times during the process. We show that as few as two rotations is effective in reducing artifacts. To further improve 2DGS-based inverse rendering, we additionally introduce a proxy mesh that not only allows accurate incident light tracing, but also enables a residual constraint and improves global illumination handling. We demonstrate with both synthetic and real world datasets that our method achieves superior albedo estimation while keeping efficient computation.


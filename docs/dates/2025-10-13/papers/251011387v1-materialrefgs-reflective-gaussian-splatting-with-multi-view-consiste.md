---
layout: default
title: MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference
---

# MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference
**arXiv**：[2510.11387v1](https://arxiv.org/abs/2510.11387) · [PDF](https://arxiv.org/pdf/2510.11387.pdf)  
**作者**：Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  

**一句话要点**：提出多视角一致材料推断方法以提升高斯溅射中的反射建模

**关键词**：高斯溅射, 材料推断, 多视角一致性, 反射建模, 新视角合成

## 3 点简述
- 核心问题：高斯溅射中材料推断缺乏约束，导致光照锯齿和泛化性差。
- 方法要点：强制多视角一致材料映射，并利用光变追踪高反射区域。
- 实验效果：在基准测试中实现新视角合成的最先进渲染质量。

## 摘要（原文）

> Modeling reflections from 2D images is essential for photorealistic rendering
> and novel view synthesis. Recent approaches enhance Gaussian primitives with
> reflection-related material attributes to enable physically based rendering
> (PBR) with Gaussian Splatting. However, the material inference often lacks
> sufficient constraints, especially under limited environment modeling,
> resulting in illumination aliasing and reduced generalization. In this work, we
> revisit the problem from a multi-view perspective and show that multi-view
> consistent material inference with more physically-based environment modeling
> is key to learning accurate reflections with Gaussian Splatting. To this end,
> we enforce 2D Gaussians to produce multi-view consistent material maps during
> deferred shading. We also track photometric variations across views to identify
> highly reflective regions, which serve as strong priors for reflection strength
> terms. To handle indirect illumination caused by inter-object occlusions, we
> further introduce an environment modeling strategy through ray tracing with
> 2DGS, enabling photorealistic rendering of indirect radiance. Experiments on
> widely used benchmarks show that our method faithfully recovers both
> illumination and geometry, achieving state-of-the-art rendering quality in
> novel views synthesis.


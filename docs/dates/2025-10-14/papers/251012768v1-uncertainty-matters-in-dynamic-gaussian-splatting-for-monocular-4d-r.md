---
layout: default
title: Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D Reconstruction
---

# Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D Reconstruction
**arXiv**：[2510.12768v1](https://arxiv.org/abs/2510.12768) · [PDF](https://arxiv.org/pdf/2510.12768.pdf)  
**作者**：Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  

**一句话要点**：提出USplat4D框架，通过不确定性建模提升单目4D动态重建质量

**关键词**：动态高斯泼溅, 不确定性建模, 单目4D重建, 时空图优化, 运动漂移抑制

## 3 点简述
- 核心问题：单目动态3D重建存在遮挡和极端视角下的模糊性，导致运动漂移和合成质量下降。
- 方法要点：引入时间变化的高斯不确定性估计，构建时空图进行不确定性感知优化。
- 实验或效果：在真实和合成数据集上验证，模型在遮挡下几何更稳定，极端视角合成质量高。

## 摘要（原文）

> Reconstructing dynamic 3D scenes from monocular input is fundamentally
> under-constrained, with ambiguities arising from occlusion and extreme novel
> views. While dynamic Gaussian Splatting offers an efficient representation,
> vanilla models optimize all Gaussian primitives uniformly, ignoring whether
> they are well or poorly observed. This limitation leads to motion drifts under
> occlusion and degraded synthesis when extrapolating to unseen views. We argue
> that uncertainty matters: Gaussians with recurring observations across views
> and time act as reliable anchors to guide motion, whereas those with limited
> visibility are treated as less reliable. To this end, we introduce USplat4D, a
> novel Uncertainty-aware dynamic Gaussian Splatting framework that propagates
> reliable motion cues to enhance 4D reconstruction. Our key insight is to
> estimate time-varying per-Gaussian uncertainty and leverages it to construct a
> spatio-temporal graph for uncertainty-aware optimization. Experiments on
> diverse real and synthetic datasets show that explicitly modeling uncertainty
> consistently improves dynamic Gaussian Splatting models, yielding more stable
> geometry under occlusion and high-quality synthesis at extreme viewpoints.


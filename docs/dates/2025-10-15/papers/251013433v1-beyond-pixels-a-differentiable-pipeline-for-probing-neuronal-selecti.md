---
layout: default
title: Beyond Pixels: A Differentiable Pipeline for Probing Neuronal Selectivity in 3D
---

# Beyond Pixels: A Differentiable Pipeline for Probing Neuronal Selectivity in 3D
**arXiv**：[2510.13433v1](https://arxiv.org/abs/2510.13433) · [PDF](https://arxiv.org/pdf/2510.13433.pdf)  
**作者**：Pavithra Elumalai, Mohammad Bashiri, Goirik Chakrabarty, Suhas Shrinivasan, Fabian H. Sinz  

**一句话要点**：提出可微分渲染管道以在3D中探索神经元选择性

**关键词**：可微分渲染, 神经元选择性, 3D场景理解, 逆图形学, 系统神经科学

## 3 点简述
- 核心问题：现有方法基于2D像素，难以分离神经元对物理场景属性的选择性。
- 方法要点：使用可微分渲染优化可变形网格，参数化变形以最大化神经元响应。
- 实验或效果：应用于猴子V4区模型，探索神经元对姿态和光照等3D因素的选择性。

## 摘要（原文）

> Visual perception relies on inference of 3D scene properties such as shape,
> pose, and lighting. To understand how visual sensory neurons enable robust
> perception, it is crucial to characterize their selectivity to such physically
> interpretable factors. However, current approaches mainly operate on 2D pixels,
> making it difficult to isolate selectivity for physical scene properties. To
> address this limitation, we introduce a differentiable rendering pipeline that
> optimizes deformable meshes to obtain MEIs directly in 3D. The method
> parameterizes mesh deformations with radial basis functions and learns offsets
> and scales that maximize neuronal responses while enforcing geometric
> regularity. Applied to models of monkey area V4, our approach enables probing
> neuronal selectivity to interpretable 3D factors such as pose and lighting.
> This approach bridges inverse graphics with systems neuroscience, offering a
> way to probe neural selectivity with physically grounded, 3D stimuli beyond
> conventional pixel-based methods.


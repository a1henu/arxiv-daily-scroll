---
layout: default
title: FreeArt3D: Training-Free Articulated Object Generation using 3D Diffusion
---

# FreeArt3D: Training-Free Articulated Object Generation using 3D Diffusion
**arXiv**：[2510.25765v1](https://arxiv.org/abs/2510.25765) · [PDF](https://arxiv.org/pdf/2510.25765.pdf)  
**作者**：Chuhao Chen, Isabella Liu, Xinyue Wei, Hao Su, Minghua Liu  

**一句话要点**：提出FreeArt3D框架，利用预训练静态3D扩散模型生成铰接3D对象，无需额外训练。

**关键词**：铰接对象生成, 3D扩散模型, Score Distillation Sampling, 训练自由优化, 4D生成, 几何纹理联合优化

## 3 点简述
- 核心问题：铰接3D对象生成依赖密集视图监督或产生粗糙几何，难以扩展。
- 方法要点：将Score Distillation Sampling扩展至3D-to-4D，联合优化几何、纹理和铰接参数。
- 实验或效果：生成高保真几何与纹理，准确预测运动结构，泛化性强且快速完成。

## 摘要（原文）

> Articulated 3D objects are central to many applications in robotics, AR/VR,
> and animation. Recent approaches to modeling such objects either rely on
> optimization-based reconstruction pipelines that require dense-view supervision
> or on feed-forward generative models that produce coarse geometric
> approximations and often overlook surface texture. In contrast, open-world 3D
> generation of static objects has achieved remarkable success, especially with
> the advent of native 3D diffusion models such as Trellis. However, extending
> these methods to articulated objects by training native 3D diffusion models
> poses significant challenges. In this work, we present FreeArt3D, a
> training-free framework for articulated 3D object generation. Instead of
> training a new model on limited articulated data, FreeArt3D repurposes a
> pre-trained static 3D diffusion model (e.g., Trellis) as a powerful shape
> prior. It extends Score Distillation Sampling (SDS) into the 3D-to-4D domain by
> treating articulation as an additional generative dimension. Given a few images
> captured in different articulation states, FreeArt3D jointly optimizes the
> object's geometry, texture, and articulation parameters without requiring
> task-specific training or access to large-scale articulated datasets. Our
> method generates high-fidelity geometry and textures, accurately predicts
> underlying kinematic structures, and generalizes well across diverse object
> categories. Despite following a per-instance optimization paradigm, FreeArt3D
> completes in minutes and significantly outperforms prior state-of-the-art
> approaches in both quality and versatility.


---
layout: default
title: GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction
---

# GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction
**arXiv**：[2602.24161v1](https://arxiv.org/abs/2602.24161) · [PDF](https://arxiv.org/pdf/2602.24161.pdf)  
**作者**：Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  

**一句话要点**：提出几何感知扩散框架，从单张肖像重建高保真4D头部化身

**关键词**：4D头部化身重建, 几何感知扩散, 3D高斯化身, 表情编码, 单张肖像重建, 实时渲染

## 3 点简述
- 核心问题：单张肖像重建4D头部化身时，现有方法依赖2D先验，几何一致性差
- 方法要点：联合合成肖像与表面法线，结合姿态无关编码器，融入3D高斯化身
- 实验或效果：在视觉质量、表情保真度和跨身份泛化上优于先进方法，支持实时渲染

## 摘要（原文）

> Reconstructing photorealistic and animatable 4D head avatars from a single portrait image remains a fundamental challenge in computer vision. While diffusion models have enabled remarkable progress in image and video generation for avatar reconstruction, existing methods primarily rely on 2D priors and struggle to achieve consistent 3D geometry. We propose a novel framework that leverages geometry-aware diffusion to learn strong geometry priors for high-fidelity head avatar reconstruction. Our approach jointly synthesizes portrait images and corresponding surface normals, while a pose-free expression encoder captures implicit expression representations. Both synthesized images and expression latents are incorporated into 3D Gaussian-based avatars, enabling photorealistic rendering with accurate geometry. Extensive experiments demonstrate that our method substantially outperforms state-of-the-art approaches in visual quality, expression fidelity, and cross-identity generalization, while supporting real-time rendering.


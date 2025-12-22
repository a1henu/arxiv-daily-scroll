---
layout: default
title: 3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework
---

# 3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework
**arXiv**：[2512.17459v1](https://arxiv.org/abs/2512.17459) · [PDF](https://arxiv.org/pdf/2512.17459.pdf)  
**作者**：Tobias Sautter, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  

**一句话要点**：提出3D-RE-GEN框架，通过组合生成方法从单图像重建室内场景的纹理3D网格，满足艺术家需求。

**关键词**：3D场景重建, 纹理网格生成, 单图像重建, 室内场景, 生成模型, 空间优化

## 3 点简述
- 核心问题：现有纹理网格场景重建方法存在对象分解错误、空间关系不准确和背景缺失，难以满足艺术家工作流需求。
- 方法要点：集成资产检测、重建和放置模型，采用生成模型处理遮挡对象，并通过4-DoF优化对齐对象与地面平面。
- 实验或效果：在单图像3D场景重建中达到先进性能，生成连贯、可修改的场景，支持视觉效果和游戏开发。

## 摘要（原文）

> Recent advances in 3D scene generation produce visually appealing output, but current representations hinder artists' workflows that require modifiable 3D textured mesh scenes for visual effects and game development. Despite significant advances, current textured mesh scene reconstruction methods are far from artist ready, suffering from incorrect object decomposition, inaccurate spatial relationships, and missing backgrounds. We present 3D-RE-GEN, a compositional framework that reconstructs a single image into textured 3D objects and a background. We show that combining state of the art models from specific domains achieves state of the art scene reconstruction performance, addressing artists' requirements.
>   Our reconstruction pipeline integrates models for asset detection, reconstruction, and placement, pushing certain models beyond their originally intended domains. Obtaining occluded objects is treated as an image editing task with generative models to infer and reconstruct with scene level reasoning under consistent lighting and geometry. Unlike current methods, 3D-RE-GEN generates a comprehensive background that spatially constrains objects during optimization and provides a foundation for realistic lighting and simulation tasks in visual effects and games. To obtain physically realistic layouts, we employ a novel 4-DoF differentiable optimization that aligns reconstructed objects with the estimated ground plane. 3D-RE-GEN~achieves state of the art performance in single image 3D scene reconstruction, producing coherent, modifiable scenes through compositional generation guided by precise camera recovery and spatial optimization.


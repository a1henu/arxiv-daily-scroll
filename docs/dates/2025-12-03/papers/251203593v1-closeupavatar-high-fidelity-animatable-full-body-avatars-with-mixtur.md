---
layout: default
title: CloseUpAvatar: High-Fidelity Animatable Full-Body Avatars with Mixture of Multi-Scale Textures
---

# CloseUpAvatar: High-Fidelity Animatable Full-Body Avatars with Mixture of Multi-Scale Textures
**arXiv**：[2512.03593v1](https://arxiv.org/abs/2512.03593) · [PDF](https://arxiv.org/pdf/2512.03593.pdf)  
**作者**：David Svitov, Pietro Morerio, Lourdes Agapito, Alessio Del Bue  

**一句话要点**：提出CloseUpAvatar以解决多尺度相机运动下高保真可动画全身虚拟人渲染问题

**关键词**：全身虚拟人, 多尺度纹理, 相机距离自适应, 高保真渲染, 可动画表示

## 3 点简述
- 核心问题：现有方法在广范围相机位姿下渲染质量下降，尤其在近景时细节不足
- 方法要点：使用多尺度纹理混合表示，根据相机距离自动切换高低频纹理以调整渲染质量
- 实验或效果：在ActorsHQ数据集上验证，渲染质量与速度优于现有方法，支持广范围相机位姿

## 摘要（原文）

> We present a CloseUpAvatar - a novel approach for articulated human avatar representation dealing with more general camera motions, while preserving rendering quality for close-up views. CloseUpAvatar represents an avatar as a set of textured planes with two sets of learnable textures for low and high-frequency detail. The method automatically switches to high-frequency textures only for cameras positioned close to the avatar's surface and gradually reduces their impact as the camera moves farther away. Such parametrization of the avatar enables CloseUpAvatar to adjust rendering quality based on camera distance ensuring realistic rendering across a wider range of camera orientations than previous approaches. We provide experiments using the ActorsHQ dataset with high-resolution input images. CloseUpAvatar demonstrates both qualitative and quantitative improvements over existing methods in rendering from novel wide range camera positions, while maintaining high FPS by limiting the number of required primitives.


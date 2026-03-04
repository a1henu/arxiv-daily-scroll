---
layout: default
title: R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild
---

# R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild
**arXiv**：[2603.02801v1](https://arxiv.org/abs/2603.02801) · [PDF](https://arxiv.org/pdf/2603.02801.pdf)  
**作者**：Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  

**一句话要点**：提出R3GW方法，实现野外户外场景的可重光照3D高斯表示

**关键词**：3D高斯溅射, 可重光照表示, 户外场景重建, 基于物理的渲染, 新视图合成

## 3 点简述
- 核心问题：3D高斯溅射无法建模光照，不适用于重光照任务，且在野外多变光照下重建困难
- 方法要点：将场景分为可重光照前景和非反射背景，结合基于物理的渲染与3D高斯表示建模光照效果
- 实验或效果：在NeRF-OSR数据集上实现先进性能，支持任意光照下的真实感新视图合成，并减少天空-前景边界伪影

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has established itself as a leading technique for 3D reconstruction and novel view synthesis of static scenes, achieving outstanding rendering quality and fast training. However, the method does not explicitly model the scene illumination, making it unsuitable for relighting tasks. Furthermore, 3DGS struggles to reconstruct scenes captured in the wild by unconstrained photo collections featuring changing lighting conditions. In this paper, we present R3GW, a novel method that learns a relightable 3DGS representation of an outdoor scene captured in the wild. Our approach separates the scene into a relightable foreground and a non-reflective background (the sky), using two distinct sets of Gaussians. R3GW models view-dependent lighting effects in the foreground reflections by combining Physically Based Rendering with the 3DGS scene representation in a varying illumination setting. We evaluate our method quantitatively and qualitatively on the NeRF-OSR dataset, offering state-of-the-art performance and enhanced support for physically-based relighting of unconstrained scenes. Our method synthesizes photorealistic novel views under arbitrary illumination conditions. Additionally, our representation of the sky mitigates depth reconstruction artifacts, improving rendering quality at the sky-foreground boundary

